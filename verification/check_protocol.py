"""Reproduce the ideal weak-SWAP protocol checks using Python's standard library."""

import itertools
import math
import random
from fractions import Fraction


def transition(retained, weight, dimension, strength):
    """Return the success probability and increase in target population."""
    fresh = weight + (1 - weight) / dimension
    background = (1 - weight) / dimension
    overlap = retained * fresh + (1 - retained) * background
    success = 1 - 2 * strength * (1 - strength) * (1 - overlap)
    interference = 2 * retained * weight * (1 - retained)
    gain = strength * ((1 - strength) * interference - strength * (retained - fresh))
    return success, gain / success


def streaming_cost(dimension, weight, target_error):
    """Return the first target-crossing stage and its expected raw-copy cost."""
    fresh = weight + (1 - weight) / dimension
    advantage = weight + fresh - 1
    if not 0 < target_error < 1 - fresh or advantage <= 0:
        raise ValueError("Expected a nontrivial target in the positive-advantage regime.")

    attenuation = advantage / (2 * weight)
    retained = fresh
    survival = 1.0
    attempt_cost = 1.0
    renewal_cost = 1.0
    steps = 0
    while 1 - retained > target_error:
        interference = 2 * retained * weight * (1 - retained)
        strength = attenuation * interference / (interference + retained - fresh)
        success, gain = transition(retained, weight, dimension, strength)
        assert 0 < success <= 1
        assert gain > 0
        attempt_cost += survival
        survival *= success
        renewal_cost = (renewal_cost + 1) / success
        retained += gain
        steps += 1
    # A trial draws a seed and a sample for every stage it reaches. Independent
    # restarts multiply the expected trial cost by the inverse success probability.
    assert math.isclose(renewal_cost, attempt_cost / survival, rel_tol=1e-9)
    return steps, renewal_cost, 1 - retained


def mixed_state(direction, population):
    """Build the input density matrix from a complex unit vector."""
    side_population = (1 - population) / (len(direction) - 1)
    return [
        [
            side_population * (i == j)
            + (population - side_population) * amplitude * other.conjugate()
            for j, other in enumerate(direction)
        ]
        for i, amplitude in enumerate(direction)
    ]


def direct_filter(stored, fresh, strength):
    """Apply the two-register operator by tensor indices, then trace one register."""
    dimension = len(stored)
    filtered = [[0j for _ in range(dimension)] for _ in range(dimension)]
    identity = 1 - strength
    for i, j, k in itertools.product(range(dimension), repeat=3):
        ket = ((i, k, identity), (k, i, strength))
        bra = ((j, k, identity), (k, j, strength))
        for (a, b, left), (c, d, right) in itertools.product(ket, bra):
            filtered[i][j] += left * right * stored[a][c] * fresh[b][d]
    return filtered


def check_filter():
    rng = random.Random(1729)
    largest_error = 0.0
    for dimension in (2, 3, 5):
        for _ in range(40):
            arbitrary = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(dimension)]
            norm = math.sqrt(sum(abs(amplitude) ** 2 for amplitude in arbitrary))
            direction = [amplitude / norm for amplitude in arbitrary]
            weight = rng.uniform(0.05, 0.95)
            fresh_population = weight + (1 - weight) / dimension
            retained = rng.uniform(fresh_population, 1)
            strength = rng.uniform(0, 0.5)
            stored, fresh = mixed_state(direction, retained), mixed_state(direction, fresh_population)
            observed = direct_filter(stored, fresh, strength)
            success, gain = transition(retained, weight, dimension, strength)
            expected = mixed_state(direction, retained + gain)
            for i, j in itertools.product(range(dimension), repeat=2):
                largest_error = max(largest_error, abs(observed[i][j] - success * expected[i][j]))
    assert largest_error < 3e-14
    print(f"120 complex-direction matrix checks: maximum entry error {largest_error:.2e}")


def check_strong_projection():
    for dimension in (2, 3, 16):
        for weight in (0.2, 0.5, 0.8):
            fresh = weight + (1 - weight) / dimension
            linear = 2 * weight - 1
            ceiling = (linear + math.sqrt(linear**2 + 8 * weight * fresh)) / (4 * weight)
            assert fresh < ceiling < 1
            retained = fresh
            for _ in range(300):
                _, gain = transition(retained, weight, dimension, 0.5)
                retained += gain
                assert retained <= ceiling + 1e-13
            assert math.isclose(retained, ceiling, rel_tol=1e-13)
    print("Strong-projection trajectories converge to the predicted subunit ceiling.")


def check_restart_examples():
    expected = [(2, 15, 19.7054), (16, 30, 47.0813), (10**6, 33, 53.3002)]
    print("Dimension | accepted stages | expected copies | measure-and-prepare lower bound")
    for dimension, expected_steps, expected_cost in expected:
        target = Fraction(1, 100)
        steps, cost, attained = streaming_cost(dimension, 0.8, float(target))
        lower_bound = (dimension - 1) / target - dimension
        assert steps == expected_steps
        assert math.isclose(cost, expected_cost, abs_tol=5e-5)
        assert attained <= target
        assert cost < lower_bound
        print(f"{dimension:9d} | {steps:15d} | {cost:15.4f} | {str(lower_bound):>33}")


def check_accuracy_scaling():
    for weight in (0.65, 0.8):
        for dimension in (2, 16, 10**6):
            fresh = weight + (1 - weight) / dimension
            coefficient = (1 - fresh) / (weight + fresh - 1) ** 2
            for error in (1e-3, 1e-4):
                _, cost, _ = streaming_cost(dimension, weight, error)
                assert error * cost < 1.02 * (1 - weight) / (2 * weight - 1) ** 2
            assert math.isclose(error * cost, coefficient, rel_tol=0.04)
    print("Scaled cost agrees with the predicted coefficient across the dimension grid.")


if __name__ == "__main__":
    check_filter()
    check_strong_projection()
    check_restart_examples()
    check_accuracy_scaling()
