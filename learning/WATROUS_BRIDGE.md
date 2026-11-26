# From Watrous to weak-SWAP purification

A source delivers independent noisy specimens of the same unknown pure state.
Each new specimen interacts with the one already held. The goal is to
release a physical qudit with a larger target-state overlap, while counting
the specimens lost when a herald signals failure.

The selected educational anchor is **John Watrous, *The Theory of Quantum
Information***, Cambridge University Press, 2018. Section numbers refer to
the author's standard-layout manuscript, dated January 2018 in the preface.
The [author's textbook page](https://cs.uwaterloo.ca/~watrous/TQI/) links the
[manuscript contents](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf)
and each chapter. Follow the relevant reading while working through the
[30 milestones](MILESTONES.md) or the [worked tutorial](TUTORIAL.md).

## Targeted reading

| Project need | Watrous manuscript |
|---|---|
| Tensor products, trace identities, convexity and expectations | [Sections 1.1.2–1.1.3 and 1.2.1–1.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) |
| Density operators, mixed-state reductions and partial trace | [Sections 2.1.2–2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) |
| Completely positive maps, Kraus operators and measurement effects | [Sections 2.2.1–2.2.3 and 2.3.1–2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) |
| Fidelity with a pure target | [Section 3.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) |
| Permutation operators and the symmetric subspace | [Section 7.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf) |
| Haar measure and symmetric-projector moments | [Sections 7.2.1–7.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf) |

## Translation guide

| Watrous | Project |
|---|---|
| A unit column vector $`u`$ and its rank-one projector $`uu^*`$ | The unknown target ket and projector *P* |
| *F*(ρ,σ), the fidelity function | *r* = tr(*P*ρ), the square of Watrous's fidelity with pure target *P* |
| A permutation operator $`W_\pi`$ acting on tensor factors | *S* for the two-register transposition, with eigenspaces selected by $`P_{\rm sym}`$ and $`P_{\rm anti}`$ |
| A measurement effect and a completely positive branch | *K*†*K* gives the herald probability. The branch uses *K* and then a partial trace to give the physical output. |
| The symmetric projector on *n* registers | Πₙ, with dimension *D*ₙ, for Haar moments in the classical-output benchmark |

Watrous's treatment of “purifications” in §2.1.3 gives a way to represent a
mixed state as a marginal of a larger pure state. This project's task is
to use repeatedly supplied noisy specimens to increase the overlap of
one output with the unknown target. The partial trace is used to compute
the conditional marginal after the two-register interaction. [Model](../science/model.md)

## From the source to the mechanism

The foundational ingredients give a way to represent the experiment.
Permuting two identical register spaces defines SWAP, and the two
eigenspaces give the symmetric and antisymmetric projections. A
controlled operation followed by a measurement supplies a physical
branch. The project combines the two sectors within that branch, preserving
cross terms that can act on inputs of unequal purity. When the outgoing
register is discarded, these terms appear as products of operators in
the retained state. The [weak-SWAP derivation](../science/weak-swap.md)
shows the resulting gain and computes the ceiling of full sector projection.

The textbook's probability and convexity tools help turn a local gain
into a resource claim. The project determines how the filter should
weaken as the target is approached and counts failed attempts with a
renewal recurrence. This adds an asymptotic law for expected raw-copy
cost to the single-branch calculation. [Sample cost](../science/sample-cost.md)

For an estimate-and-prepare receiver, the uniform pure-state moment is a
symmetric projector divided by its dimension. The project bounds the
fidelity score separately for every measurement record, including records
that stop after different numbers of specimens. Convexity converts that
bound into a lower bound in terms of the expected number of copies.
[Measure and prepare](../science/measure-prepare.md)
