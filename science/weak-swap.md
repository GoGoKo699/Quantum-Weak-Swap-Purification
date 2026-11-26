# The weak SWAP instrument

Let $`S`$ swap the stored and fresh qudits. For a strength $`u`$ between zero and one half, prepare one control qubit as $`\sqrt{1-u}|0\rangle+\sqrt u|1\rangle`$. Apply $`S`$ controlled on the second term, undo the preparation, and measure the control. Accept the zero result. Discard the fresh register after success, and discard both data registers after failure. A new attempt starts by putting a new incoming copy in the retained register.

On success the data Kraus operator is

```math
K_u=(1-u)I+uS=P_{\rm sym}+(1-2u)P_{\rm anti},
\qquad P_{\rm sym}=(I+S)/2,\quad P_{\rm anti}=(I-S)/2.
```

Both projectors commute with identical unitary rotations of the two data registers. The control measurement interpolates from no measurement at $`u=0`$ to the usual symmetric projection at $`u=1/2`$.

## One round

Write the stored state before the round as $`\rho_r=rP+(1-r)(I-P)/(d-1)`$, with $`p\le r<1`$. Expanding $`K_u(\rho_r\otimes\sigma)K_u^\dagger`$ and tracing the second qudit gives the unnormalized retained output

```math
(1-u)^2\rho_r+u^2\sigma+u(1-u)(\rho_r\sigma+\sigma\rho_r).
```

The identities underlying the cross terms are $`\operatorname{Tr}_2[(A\otimes B)S]=AB`$ and $`\operatorname{Tr}_2[S(A\otimes B)]=BA`$. In particular, the output is still a mixture of $`P`$ and the maximally mixed state orthogonal to $`P`$.

Let $`h=\operatorname{Tr}(\rho_r\sigma)=rp+(1-r)q`$ and $`X=2rs(1-r)`$. Taking the trace and target overlap gives the probability $`D`$ of success and the new target population $`r'`$:

```math
\begin{aligned}
D(r,u)&=1-2u(1-u)(1-h),\\
r'-r&=\frac{u(1-u)X-u^2(r-p)}{D(r,u)}.
\end{aligned}
```

The gain contains a term linear in small $`u`$, from the cross terms, and a loss quadratic in $`u`$, from replacing part of the stored state with a fresh noisier copy. The linear gain also shrinks with $`1-r`$. Balancing these terms gives a measurement strength proportional to $`1-r`$ near the target.

## Why observing the symmetry sector changes the result

For the symmetric projection alone, $`r'-r`$ has the sign of $`2rs(1-r)-(r-p)`$. This expression is positive at $`r=p`$, negative at $`r=1`$, and vanishes at a unique point $`r_\star`$ between them. The symmetric-branch update is the increasing function $`(r+p+2rp)/(2(1+h))`$, so every iterate starting from $`p`$ stays at or below $`r_\star`$. To see monotonicity, write the function as $`[(1+2p)r+p]/[2(1+q+sr)]`$. The derivative has the sign of $`(1+2p)(1+q)-sp>0`$.

If the symmetry sector is recorded and used to accept with different probabilities, the two normalized target populations are

```math
r_+=\frac{r+p+2rp}{2(1+h)},\qquad
r_-=\frac{r+p-2rp}{2(1-h)}.
```

Since $`h\le\min(r,p)`$, one has $`2rp\ge h(r+p)`$ and therefore $`r_+\ge r_-`$. A mixture of these branches cannot give a larger target population than $`r_+`$. At an identical input, the two sectors have zero cross blocks. Once the stored and incoming eigenvalues differ, $`K_u`$ retains these blocks in the accepted state and the weak measurement can pass the strong-projection ceiling.
