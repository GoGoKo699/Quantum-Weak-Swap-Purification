# Measure-and-prepare benchmark

A measure-and-prepare protocol receives copies, collects a classical transcript and prepares its output from that transcript. It may measure copies collectively and decide when to stop using earlier outcomes. Any quantum system entering the final preparation is independent of the target conditioned on the transcript, except through the prepared guess. This benchmark permits all transcript lengths and all guesses.

## The per-transcript bound

First allow access to ideal pure copies of $`|\psi\rangle`$ drawn from the invariant Haar distribution. A completed transcript stopping at $`n`$ copies has an effect $`E`$ on those copies. Its probability on input $`\psi`$ is $`\mathrm{Tr}(E P^{\otimes n})`$ for $`P=|\psi\rangle\langle\psi|`$. Adaptivity is included in the effect, which can be viewed as part of a joint instrument on the first $`n`$ inputs.

Let $`\Pi_n`$ be the symmetric projector on $`n`$ qudits, and $`D_n=\binom{n+d-1}{d-1}`$ its rank. The unweighted Haar average of the input is $`\Pi_n/D_n`$. For a pure guess $`|\phi\rangle`$, the overlap-weighted moment is

```math
\int P^{\otimes n}|\langle\phi|\psi\rangle|^2\,d\psi
=\frac{(I\otimes\langle\phi|)\Pi_{n+1}(I\otimes|\phi\rangle)}{D_{n+1}}
\ \le\ \frac{\Pi_n}{D_{n+1}} .
```

The contraction is supported on the symmetric $`n`$-copy space and is bounded by the identity there, because $`\Pi_{n+1}`$ is an orthogonal projector. Pairing with the positive effect shows that the conditional average fidelity on this transcript is at most $`D_n/D_{n+1}=(n+1)/(n+d)`$. Linearity gives the same bound for a mixed guess.

## Stopping and noisy inputs

Average over the stopping transcript. If $`N`$ is the number of input copies, the Haar-average infidelity is at least

```math
\mathbb E\!\left[\frac{d-1}{N+d}\right]
\ \ge\ \frac{d-1}{\mathbb E[N]+d}.
```

The last step is Jensen's inequality. The per-transcript bound also applies to a selected success event when it is expressed in terms of the sample count conditioned on that event. For the benchmark here the process returns an output almost surely, and all copies consumed are included in $`N`$.

A pure-source receiver can simulate a depolarized-source receiver by sending each input through the specified depolarizing channel. Consequently the same lower bound applies to the noisy input model. If the required output infidelity is at most $`\epsilon`$ for every direction, its Haar average is at most $`\epsilon`$, so the average sample cost is at least $`(d-1)/\epsilon-d`$.

The fixed-length pure-state estimation result is due to [Bruß and Macchiavello](../references/RELATED_WORK.md). The per-outcome argument is what permits the variable-stopping comparison here. This benchmark leaves room for hybrid strategies in which the final output retains quantum information from one of the source copies.
