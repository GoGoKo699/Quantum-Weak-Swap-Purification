# Model and results

The task is to output a qudit close to an unknown pure state when independent noisy copies arrive sequentially. The protocol can keep a quantum register from one arrival to the next. It consumes each incoming copy once.

## Input, output and resources

Let $`P=|\psi\rangle\langle\psi|`$ be an unknown rank-one projector on a system of dimension $`d\ge 2`$. Every fresh copy has density operator

```math
\sigma=sP+(1-s)I/d,\qquad 0<s<1.
```

The dimension and signal weight $`s`$ are known. Put $`p=s+(1-s)/d`$ and $`q=(1-s)/d`$. The target population of a fresh state is $`p`$. The desired output density operator $`\rho`$ obeys $`\operatorname{Tr}(P\rho)\ge 1-\epsilon`$ for every $`P`$. This overlap is the squared fidelity convention when the target is pure.

The protocol retains one data qudit between arrivals. It may operate jointly on this qudit and the current fresh one, with a disposable control qubit prepared and measured each round. It keeps the herald and scalar schedule in a classical record. It uses no prior description of $`P`$. Every fresh copy counts, including the initial copy of each failed attempt. The basic sample guarantee assumes ideal gates, perfect control and noiseless storage. The [storage model](robustness.md) treats depolarization explicitly.

## Results

The [weak SWAP measurement](weak-swap.md) compares the stored copy with the incoming one and returns a success flag. Conditioned on success, the stored state stays in the family with one distinguished eigenvalue $`r`$ at $`P`$ and a flat orthogonal spectrum. The measurement strength may be scheduled from the known initial signal weight and the number of successful steps in the current attempt.

Let $`N_\epsilon`$ be the random number of raw copies consumed until an output with infidelity at most $`\epsilon`$ is returned. If $`s+p>1`$, a one-register schedule gives

```math
\lim_{\epsilon\to0}\epsilon\,\mathbb E[N_\epsilon]
=\frac{1-p}{(s+p-1)^2}.
```

In terms of the input weight, the condition is $`s>(d-1)/(2d-1)`$. For fixed $`s>1/2`$ the bound $`\mathbb E[N_\epsilon]=O_s(1/\epsilon)`$ holds uniformly over all $`d\ge 2`$. The equality gives the constant of the specified schedule. The [sample-cost proof](sample-cost.md) accounts for rejected rounds and distinguishes expected sample cost from coherence time.

A [measure-and-prepare receiver](measure-prepare.md) must use at least $`(d-1)/\epsilon-d`$ copies in expectation on average over Haar-random targets. This includes receivers with collective measurements and variable stopping times, provided the final state is prepared entirely from a classical transcript. A worst-case infidelity guarantee implies the same lower bound on worst-case expected sample usage. A hybrid receiver that keeps an incoming quantum system for output after consulting the record lies outside this benchmark.

The protocol makes the same target-oriented comparison in every basis. Its content is the coherence retained in the state and the SWAP measurement, together with a decreasing measurement strength that lets this coherence accumulate with a small restart cost.
