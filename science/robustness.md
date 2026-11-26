# Control and storage errors

Consider the one-register filter with input target population $`p=s+(1-s)/d`$ and a fixed $`0\lt s\lt 1`$. Write $`r`$ for the stored target population, $`e=1-r`$ for its infidelity, and $`b_d=1-1/d`$. Let $`F(r,u)`$ be the accepted population at SWAP strength $`u`$ and $`D(r,u)`$ its acceptance probability. With $`q=(1-s)/d`$, $`h=rp+(1-r)q`$, and $`X(r)=2rs(1-r)`$, the exact update is

```math
D(r,u)=1-2u(1-u)(1-h),\qquad
F(r,u)-r=\frac{uX(r)-u^2[X(r)+r-p]}{D(r,u)}.
```

## The storage-noise floor

After every accepted filter step, apply a depolarizing channel of fixed strength $`\lambda`$ to the stored qudit. The seed is a fresh input. Rejection discards both data registers and starts again. Count every use of a fresh copy. The accepted map including storage noise is

```math
F_\lambda(r,u)=(1-\lambda)F(r,u)+\lambda/d.
```

Within this family, for fixed $`d,s`$, the smallest achievable output infidelity satisfies

```math
\inf\epsilon_{\mathrm{out}}
=\frac{\sqrt{b_d(1-p)}}{s}\sqrt{\lambda}\,[1+o(1)]
\qquad(\lambda\downarrow0).
```

The same leading coefficient holds if the final accepted output is delivered before its associated storage channel. This result permits adaptive choices of $`u\in[0,1]`$ and any finite expected number of copies for each fixed $`\lambda`$.

Define $`g(r)=X(r)/(X(r)+r-p)`$ for $`p\le r\lt 1`$. Near $`r=1`$, improvement requires $`0\lt u\lt g(r)=O(e)`$, so $`D=1+O(e)`$ uniformly on the improving strengths. The numerator is maximized at $`u=g(r)/2`$. This gives

```math
\max_{0\le u\le1}\bigl(F(r,u)-r\bigr)
=\frac{s^2}{1-p}e^2+O(e^3).
```

The same expansion holds at $`u=g(r)/2`$. Also $`F(r,u)`$ is nondecreasing in $`r`$ for each fixed $`u`$. Put $`a=1-u`$ and $`D_0=a^2+u^2+2auq`$. Then $`F=[(a^2+2aup)r+u^2p]/[D_0+2ausr]`$. The numerator of its derivative is at least $`a^2D_0+2aup\,u^2(1-s)`$, which is nonnegative.

Let $`a_*=\sqrt{b_d(1-p)}/s`$. At $`r_-=1-(1-\delta)a_*\sqrt{\lambda}`$, for any fixed $`0\lt \delta\lt 1`$, the maximal noisy increment is strictly negative for small enough $`\lambda`$. The maximal ideal gain has leading term $`b_d(1-\delta)^2\lambda`$, while storage subtracts $`b_d\lambda+O(\lambda^{3/2})`$ from the gain. Monotonicity makes the interval $`r\le r_-`$ invariant for every control. The seed lies in that interval. A final step without storage noise can improve the population by at most $`O(\lambda)`$ beyond $`r_-`$, by monotonicity and the ideal gain bound at $`r_-`$.

For achievability use $`u=g(r)/2`$ and stop at infidelity at most $`(1+\delta)a_*\sqrt{\lambda}`$. Away from $`r=1`$ the ideal increment is strictly positive and dominates sufficiently small storage error. At small $`e`$ above the target, the ideal increment is $`[s^2/(1-p)+O(e)]e^2`$. Choose a small fixed cutoff so that its coefficient exceeds $`s^2/[(1-p)(1+\delta)^2]`$ by a positive constant. Then it dominates the storage loss uniformly up to the target. The increment has a positive minimum on the closed interval from seed to target for each fixed, sufficiently small $`\lambda`$. Finitely many consecutive accepted stages therefore reach the target, at finite expected cost upon restarting. Taking $`\delta`$ arbitrarily small proves the coefficient.

## Linear sample cost with a storage budget

When $`s+p\gt 1`$, choose the noiseless schedule parameter $`\eta_0=(s+p-1)/(2s)`$. For a target $`\epsilon`$, the expected raw-copy count remains $`O(1/\epsilon)`$ if $`\lambda\le\kappa\epsilon^2`$ for any fixed

```math
0\le\kappa\lt \frac{(s+p-1)^2}{b_d(1-p)}.
```

The following construction also allows unknown bounded relative errors in $`u`$. At stage $`k`$, request $`u=\eta_0 g(r_k)`$ and assume the implemented strength lies in $`[\eta_-g(r_k),\eta_+g(r_k)]`$ for fixed $`0\lt \eta_-\le\eta_0\le\eta_+\lt 1/2`$. The actual strength need not be known to the controller. The realized storage depolarization may be any value at most $`\Lambda`$ per accepted stage. Starting at $`r_0=p`$, compute a conservative population

```math
r_{k+1}=\min_{\eta\in[\eta_-,\eta_+]}F_\Lambda(r_k,\eta g(r_k)).
```

Monotonicity and the bound on depolarization guarantee that the actual accepted population is at least $`r_{k+1}`$. The acceptance probability is nondecreasing in $`r`$, so $`\underline D_k=\min_\eta D(r_k,\eta g(r_k))`$ bounds acceptance from below even when strengths vary between attempts.

Both minima can be evaluated at the endpoints of the strength interval. The denominator $`D`$ decreases for $`u\le1/2`$. The sign of the derivative of $`F-r`$ is the sign of $`X-2Tu+2(1-h)(r-p)u^2`$, where $`T=X+r-p`$. That numerator decreases over $`0\le u\le1/2`$ when $`r\ge p`$, so the filter gain can have an interior maximum but its minimum is at an endpoint.

Set

```math
C_{\min}=\min_{\eta\in[\eta_-,\eta_+]}
\frac{4\eta(1-\eta)s^2}{1-p},\qquad
B_{\max}=\max_{\eta\in[\eta_-,\eta_+]}4\eta s.
```

It suffices that $`C_{\min}\gt B_{\max}+\kappa b_d`$ and $`\Lambda\le\kappa\epsilon^2`$. This condition holds for a narrow enough interval around $`\eta_0`$ for any strict budget above. The ideal accepted gain and rejection probability are respectively $`C(\eta)e^2+O(e^3)`$ and $`B(\eta)e+O(e^2)`$, uniformly over the strength interval. For $`e_k=1-r_k\ge\epsilon`$, storage subtracts at most $`\kappa b_de_k^2`$. Hence at small $`e_k`$ there are constants $`c_0\gt b_0\gt 0`$ with

```math
e_{k+1}\le e_k(1-c_0e_k),\qquad
\underline D_k\ge1-b_0e_k.
```

On the fixed compact interval from the seed to this small-error region, the ideal gain is positive uniformly in the strength interval. The number of stages and expected copies to enter the region are bounded independently of sufficiently small $`\epsilon`$.

The deterministic sequence $`\widehat W_0=1`$, $`\widehat W_{k+1}=(\widehat W_k+1)/\underline D_k`$ bounds the expected sample cost uniformly over attempt histories. Reaching stage $`k`$ costs at most $`\widehat W_k`$ in conditional expectation and the final test costs one copy. The conditional probability of requiring another attempt is at most $`1-\underline D_k`$. Summing these bounds proves the recursion. For $`Z_k=e_k\widehat W_k`$, at sufficiently small $`e_k`$ this implies $`Z_{k+1}\le[1-(c_0-b_0)e_k]Z_k+2e_k`$. Thus $`Z_k`$ is bounded. When the target is first crossed, the ideal gain is at most quadratic, so $`e_{k+1}\ge e_k-O(e_k^2)\ge\epsilon/2`$ for small $`\epsilon`$. The resulting bound is $`\widehat W_{k+1}=O(1/\epsilon)`$.

The model assumes storage depolarization per accepted stage and a relative strength error that keeps the operator $`(1-u)I+uS`$. Control phase errors, false heralds, leakage, and variable idle times require their own models.
