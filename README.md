# Quantum Weak-Swap Purification

How much quantum memory does it take to recover an unknown pure state from noisy copies arriving one at a time? A **weak SWAP measurement** purifies the state while holding just one data register between arrivals. Each accepted step uses a fresh copy and makes the retained state purer. The measurement gets weaker as the retained state improves.

For a fixed depolarizing signal weight greater than one half, the protocol uses an expected number of fresh copies proportional to the inverse target infidelity, with a constant independent of the state dimension. This count includes all failed attempts. A round uses the retained register, one incoming register, and a disposable control qubit. The output is a physical state on the retained system.

| Dimension | Target infidelity | Weak-SWAP expected copies | Measure-and-prepare lower bound |
| --- | ---: | ---: | ---: |
| 2 | 0.01 | 19.7 | 98 |
| 16 | 0.01 | 47.1 | 1,484 |

These are ideal-model calculations at signal weight 0.80. The benchmark permits collective measurements and adaptive stopping, then prepares the output from the classical record. See [the benchmark and its scope](science/measure-prepare.md).

## Run the weak SWAP protocol

1. **Plan the accepted stages.** Given the dimension `d`, signal weight `s` and target infidelity, start from the fresh-copy overlap `p = s + (1 − s)/d`. When `s + p > 1`, use `η = (s + p − 1)/(2s)` in the [strength schedule](science/sample-cost.md#schedule-and-accepted-trajectory). Precompute the strengths and the stopping stage using the [accepted-state update](science/weak-swap.md#one-round). The controller tracks the modeled overlap by counting consecutive successes in the current attempt.
2. **Load one copy and filter each arrival.** Put the first raw copy in memory. For each next copy, initialize a control qubit to zero and apply `Ry(2 arcsin(sqrt(u)))` at the strength `u` for the current stage. SWAP the two data registers conditioned on control one, undo the rotation and measure the control in the zero–one basis.
3. **Keep or restart.** On zero, discard the incoming register, keep the stored qudit and advance one stage. On one, discard both registers and start the schedule again with the next raw copy. Return the stored qudit as soon as the modeled infidelity meets the target, including immediately after loading if the raw copy already qualifies. The control bit governs the schedule. The data qudit stays unmeasured.

Each filter uses one controlled register SWAP and a disposable control. Count every raw copy, including those used on failed attempts. The [worked first step](learning/TUTORIAL.md#work-through-the-first-step) gives an example with `d = 2` and `s = 0.8`.

## Read the science

- [Model and results](science/model.md) defines the input stream, the output guarantee and the resource counts.
- [The weak SWAP instrument](science/weak-swap.md) derives the exact update and explains the fidelity ceiling of repeatedly projecting onto the symmetric subspace.
- [Sample cost](science/sample-cost.md) proves the scaling, including failed attempts and the dimension-uniform bound.
- [Storage noise](science/robustness.md) analyzes an independent depolarization model for the retained system.
- [Related work](references/RELATED_WORK.md) compares the protocol with recursive and collective purification.

## Study and reproduce

Start with the [30-milestone map](learning/MILESTONES.md), the [Watrous bridge](learning/WATROUS_BRIDGE.md), or the [self-study tutorial](learning/TUTORIAL.md). The [reading guide](llms.txt) maps questions to proofs and checks.

Run the finite checks from the repository root with:

```bash
python3 verification/check_protocol.py
```

See the [verification guide](verification/README.md) for what the checks cover.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
