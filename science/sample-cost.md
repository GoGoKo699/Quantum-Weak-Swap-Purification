# Expected sample cost

This proof uses the [accepted-state and success-probability equations](weak-swap.md). It accounts for the entire sequence of raw copies, including the ones discarded on unsuccessful attempts.

## Schedule and accepted trajectory

For a successful prefix with target population $`r`$, choose a constant $`\eta`$ in $`(0,1/2)`$ and use

```math
u(r)=\eta\,\frac{X}{X+r-p},\qquad X=2rs(1-r).
```

Start from $`r_0=p`$. The quantity $`u(r)`$ depends only on the modeled population, so the controller can precompute the schedule from $`d`$ and $`s`$. The exact accepted gain is $`u(r)(1-\eta)X/D>0`$ for $`p\le r<1`$. The accepted populations increase to one: a limit below one would have a strictly positive next gain by continuity.

Put $`e=1-r`$. With $`e\to0`$ at fixed $`d,s,\eta`$, the exact update and herald probability give

```math
e'=e-Ce^2+O(e^3),\qquad D=1-Be+O(e^2),
\qquad C=\frac{4\eta(1-\eta)s^2}{1-p},\quad B=4\eta s.
```

Indeed, $`u=2\eta s e/(1-p)+O(e^2)`$ and $`1-h=1-p+se`$. The accepted sequence satisfies $`1/e_{k+1}-1/e_k\to C`$, hence $`e_k\sim 1/(Ck)`$.

## Count the failures

Let $`W_k`$ be the expected raw copies from an empty register until the current attempt has passed $`k`$ filters. Then $`W_0=1`$. Starting from an empty register, it costs $`W_k`$ on average to reach the next filter, and one fresh copy to try it. On failure the device is empty again. Thus

```math
W_{k+1} =\frac{W_k+1}{D_k}
```

A failed filter consumes its incoming copy before its prefix is lost.

Set $`Z_k=e_k W_k`$. The recurrence gives

```math
Z_{k+1}
=\big[1-(C-B)e_k+O(e_k^2)\big]Z_k+e_k+O(e_k^2).
```

If $`C>B`$, this tends to $`1/(C-B)`$. For a direct bound, fix any small $`t>0`$. Eventually the coefficient of $`Z_k`$ lies between $`1-(C-B+t)e_k`$ and $`1-(C-B-t)e_k`$, and the additive term lies between $`(1-t)e_k`$ and $`(1+t)e_k`$. The two bounding recurrences converge to $`(1-t)/(C-B+t)`$ and $`(1+t)/(C-B-t)`$ because $`\sum_k e_k=\infty`$. Let $`t`$ tend to zero. At the first stage with $`e_k\le\epsilon`$, one also has $`e_k/\epsilon\to1`$ because the relative increment tends to zero.

The maximum of $`C-B`$ over the chosen scalar schedule parameter occurs at $`\eta=(s+p-1)/(2s)`$ if $`s+p>1`$. It equals $`(s+p-1)^2/(1-p)`$ there. This proves the coefficient in the [model](model.md). The optimization selects the best coefficient of this schedule family.

## Uniformity and physical cost

For fixed $`s>1/2`$, $`p`$ lies in the compact interval $`[s,(1+s)/2]`$. The selected $`\eta`$ stays positive and below one half on that interval, $`1-p`$ stays positive, and $`C-B`$ stays uniformly positive. Thus the expansions and the upper comparison for $`Z_k`$ hold uniformly once $`e`$ is below a fixed cutoff. On the initial compact region $`p\le r\le 1-e_{\rm cutoff}`$, the accepted gain has a positive minimum whenever the region is nonempty. It takes a uniformly bounded number of stages to reach the cutoff. Each stage there has success probability at least one half, so the initial expected cost and the scaled cost at cutoff are uniformly bounded. The small-error comparison then gives the claimed dimension-uniform $`O_s(1/\epsilon)`$ cost. The first stage crossing a sufficiently small target also has $`e_k\ge\epsilon/2`$ uniformly, by the quadratic size of the step and compactness of the initial region.

Every filter applies one controlled register SWAP, uses a disposable control, and passes the retained state to the next stage on success. The retained register occupies $`\lceil\log_2 d\rceil`$ data qubits in a binary encoding. The same number of qubits is needed for the live incoming register. Coherence must last through an entire successful prefix, whose length grows as the target infidelity shrinks. If a bounded sample budget is needed, truncating at a constant times the expected cost gives a heralded output with constant success probability by Markov's inequality.
