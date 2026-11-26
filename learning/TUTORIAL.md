# Purifying one stored qudit

Suppose a source sends copies of a state whose orientation is unknown.
Each copy is prepared in the same depolarized state. You can hold onto one
qudit between arrivals and briefly interact it with the next copy. A useful
output is a physical state that better overlaps the unknown pure target.

## The two outcomes of a weak SWAP test

Call the pure target projector $`P`$. A fresh input is
$`\sigma=sP+(1-s)I/d`$, so its overlap with the target is
$`p=s+(1-s)/d`$. Call the stored overlap $`r`$. The
protocol learns from a classical success or failure bit, while a successful
step keeps the stored register as a quantum state.

Choose a strength $`u`$. Prepare a control with amplitudes
$`\sqrt{1-u}`$ and $`\sqrt u`$, apply a SWAP controlled on its
second basis state, undo the control preparation and measure. On the
successful outcome, the two amplitudes combine into the operator

```math
K_u=(1-u)I+uS=P_{\rm sym}+(1-2u)P_{\rm anti} .
```

Here $`S`$ is SWAP and $`P_{\rm sym},P_{\rm anti}`$ project onto the two SWAP
eigenspaces. The branch leaves the symmetric amplitude unchanged and
attenuates the antisymmetric amplitude. Applying the success operator
to both sides of the joint density operator preserves cross terms
between the sectors if they are present. With identically prepared
inputs those terms vanish. Once the stored state becomes purer than a
fresh copy, the terms affect how much target population the retained
register gains. [Circuit and derivation](../science/weak-swap.md)

## Work through the first step

Take a qubit, $`d=2`$, with $`s=0.8`$. The first raw
copy seeds the memory, so both input overlaps start at $`r=p=0.9`$.
The schedule chooses $`u=7/16`$ in this first step. Both states
have populations $`0.9`$ and $`0.1`$ along the unknown target
direction and its orthogonal complement. Their Hilbert–Schmidt overlap is
$`h=0.9^2+0.1^2=0.82`$. The herald probability is

```math
D=1-2u(1-u)(1-h)=0.91140625 .
```

On success, the retained target population is

```math
r'=0.9+\frac{u(1-u)\,2(0.9)(0.8)(0.1)}{D}
   \approx 0.938882 .
```

The denominator normalizes the successful branch. On failure, both inputs
are discarded and a new seed is drawn. Reaching the first success takes
$`2/D\approx2.194`$ raw copies on average. This first step uses
equal-quality inputs. Later steps pair the purer retained state with a
raw copy of overlap $`0.9`$, and a failure then loses the preceding
successful stages of that attempt. [Renewal cost](../science/sample-cost.md)

## Why the filter weakens

For $`r\gt p`$, the conditional gain contains a positive term
proportional to $`u(1-u)r(1-r)`$ and a loss term proportional to
$`u^2(r-p)`$. The factor $`1-r`$ shrinks as the stored state
approaches the target, while $`r-p`$ stays positive. Letting
$`u`$ shrink with $`1-r`$ keeps the gain positive.
The same adaptation makes failures rarer. [One-step update](../science/weak-swap.md)

Write $`e=1-r`$ for the current infidelity. Near the target,
one successful step improves $`e`$ by order $`e^2`$ and
fails with probability of order $`e`$. To find the total input
cost, let $`W_k`$ denote the expected number of copies to reach
stage $`k`$ starting with empty memory. If the next step succeeds
with probability $`D_k`$, then

```math
W_0=1,\qquad W_{k+1}=\frac{W_k+1}{D_k}.
```

Every attempt to advance one stage pays the cost of reaching the current
stage and drawing one more copy. A failed attempt requires both payments
again. For the stated input-quality regime, the exact recurrence has
expected cost proportional to $`1/\epsilon`$ at target infidelity
$`\epsilon`$. One coherent data register is held between arrivals.
The fresh register and one control qubit are needed during each step.
[Cost law and regime](../science/sample-cost.md)

## When storage weakens the state

Suppose the retained qudit is depolarized after every accepted filter.
A small storage depolarization of strength $`\lambda`$ subtracts
population of order $`\lambda`$ near the target, while a successful
filter adds population of order $`e^2`$. Balancing these terms gives
an infidelity floor of order $`\sqrt{\lambda}`$ in this model.
The inverse-infidelity sample law also survives when the storage
strength is bounded at a sufficiently small multiple of
$`\epsilon^2`$ and the implemented SWAP strength stays in the
proved relative-error interval. [Control and storage analysis](../science/robustness.md)

## What the comparison establishes

For $`d=16`$ and $`s=0.8`$, evaluating the ideal recurrence
at $`\epsilon=0.01`$ gives about 47.1 expected raw copies. A
procedure that measures its inputs and prepares a replacement from its
classical record needs at least 1,484 expected copies at the same accuracy.
The bound allows collective measurements and a variable stopping time.
That restriction concerns the final output. The weak-SWAP protocol
returns the quantum system that it retained through the interactions.
[Benchmark proof](../science/measure-prepare.md)

The [model](../science/model.md) states the resource conventions and
assumptions. The [30 milestones](MILESTONES.md) connect this example to
the full derivation, and the [verification guide](../verification/README.md)
explains how to reproduce the numerical check.
