# Quantum Weak-Swap Purification

How much quantum memory does it take to recover an unknown pure state from noisy copies arriving one at a time? A **weak SWAP measurement** purifies the state while holding just one data register between arrivals. Each accepted step uses a fresh copy and makes the retained state purer. The measurement gets weaker as the retained state improves.

For a fixed depolarizing signal weight greater than one half, the protocol uses an expected number of fresh copies proportional to the inverse target infidelity, with a constant independent of the state dimension. This count includes all failed attempts. A round uses the retained register, one incoming register, and a disposable control qubit. The output is a physical state on the retained system.

| Dimension | Target infidelity | Weak-SWAP expected copies | Measure-and-prepare lower bound |
| --- | ---: | ---: | ---: |
| 2 | 0.01 | 19.7 | 98 |
| 16 | 0.01 | 47.1 | 1,484 |

These are ideal-model calculations at signal weight 0.80. The benchmark permits collective measurements and adaptive stopping, then prepares the output from the classical record. See [the benchmark and its scope](science/measure-prepare.md).

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
