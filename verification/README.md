# Reproduce the numerical checks

Run from the repository root with Python 3:

```sh
python3 verification/check_protocol.py
```

The script uses only the standard library and a fixed random seed. It applies the two-register filter by tensor indices and traces out the fresh register for 120 complex input directions in dimensions 2, 3 and 5. It compares the result entry by entry with the closed-form state update. It also tests convergence to the ceiling for a strong projection and independently sums the expected per-attempt sample costs from the stage survival probabilities.

With input signal weight 0.8 and target infidelity 0.01, the script gives the following values. The expected copy count includes the initial copy of each attempt and every copy consumed before a restart.

| Dimension | Accepted steps to the target | Expected raw copies | Measure-and-prepare lower bound |
| ---: | ---: | ---: | ---: |
| 2 | 15 | 19.7054 | 98 |
| 16 | 30 | 47.0813 | 1,484 |
| 1,000,000 | 33 | 53.3002 | 98,999,900 |

A dimension grid at input weights 0.65 and 0.8 checks scaled cost against the analytic asymptotic coefficient. A separate calculation checks the storage-noise floor in dimension 16 at a per-stage depolarization of one part in one hundred million. These calculations illustrate the model and its analytic bounds. The dimension-uniform result follows from the proof. The table reports numerical model values.
