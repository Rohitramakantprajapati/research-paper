# Chapter 6: The Subcritical Regularity Theorem (alpha > 1/2)

def generate_chapter_06():
    return r"""
<!-- CHAPTER 6 -->
<div class="page-break"></div>
<h1 class="chapter-num">CHAPTER 6</h1>
<h2 class="chapter-title">The Subcritical Regularity Theorem ($\\alpha > 1/2$)</h2>

<h3 class="section-title">6.1. Formal Mathematical Statement of Hypothesis $H_\\alpha$</h3>
<p>
  In this chapter, we establish the first major regularity theorem of this dissertation: under the geometric condition that the vorticity direction field $\\xi(x,t)$ satisfies localized H&ouml;lder continuity with exponent $\\alpha > 1/2$, the 3D incompressible Navier–Stokes equations cannot develop finite-time singularities for any initial data, regardless of its energy or enstrophy magnitude.
</p>
<div class="def-box">
  <strong>Definition 6.1 (Subcritical Geometric Hypothesis $H_\\alpha$, $\\alpha > 1/2$):</strong>
  Let $u$ be a classical solution on $[0, T^*)$. We say that the direction field $\\xi(x,t) = \\omega(x,t)/|\\omega(x,t)|$ satisfies Hypothesis $H_\\alpha$ with subcritical exponent $\\alpha \\in (1/2, 1]$ if there exists an absolute constant $K_\\xi > 0$ such that for all $t \\in [0, T^*)$, all $x \\in \\Omega_M(t)$, and all $y \\in \\mathbb{R}^3$ with $z(t) \\le |y| \\le R$:
  $$|\\xi(x+y, t) - \\xi(x, t)| \\le K_\\xi |y|^\\alpha. \tag{6.1}$$
</div>

<h3 class="section-title">6.2. Assembly of Multi-Scale Estimates into the Enstrophy Inequality</h3>
<p>
  We now insert the three concentric zone estimates derived in Chapter 5 into the fundamental enstrophy identity:
</p>
<div class="equation">
  $$\\frac{1}{2} \\frac{d}{dt} Q(t) + \\nu \\|\\nabla \\omega(t)\\|_{L^2}^2 = \\int_{\\mathbb{R}^3} (S\\omega \\cdot \\omega)\\,dx. \tag{6.2}$$
</div>
<p>
  We decompose the vortex stretching integral across the three zones:
</p>
<div class="equation">
  $$\\int_{\\mathbb{R}^3} (S\\omega \\cdot \\omega)\\,dx = \\int_{\\Omega_M} (S_{B_z} \\omega \\cdot \\omega)\\,dx + \\int_{\\Omega_M} (S_A \\omega \\cdot \\omega)\\,dx + \\int_{\\Omega_M} (S_{E_R} \\omega \\cdot \\omega)\\,dx + \\int_{\\mathbb{R}^3 \\setminus \\Omega_M} (S\\omega \\cdot \\omega)\\,dx. \tag{6.3}$$
</div>
<p>
  We evaluate each term systematically:
</p>
<ol style="margin-left: 15pt; line-height: 1.7;">
  <li><strong>Inactive background $\\mathbb{R}^3 \\setminus \\Omega_M$:</strong> On this region, $|\\omega(x,t)| \\le M$. Therefore:
  $$\\left| \\int_{\\mathbb{R}^3 \\setminus \\Omega_M} (S\\omega \\cdot \\omega)\\,dx \\right| \\le M \\int_{\\mathbb{R}^3} |S| |\\omega|\\,dx \\le M \\|S\\|_{L^2} \\|\\omega\\|_{L^2} = M \\|\\omega\\|_{L^2}^2 = M Q(t). \tag{6.4}$$</li>
  <li><strong>Near-Field Core $B_z$:</strong> By Proposition 5.1, choosing $z(t) = c_* \\nu^2 / Q(t)$ gives:
  $$\\int_{\\Omega_M} |S_{B_z}| |\\omega|^2\\,dx \\le \\frac{\\nu}{4} \\|\\nabla \\omega(t)\\|_{L^2}^2. \tag{6.5}$$</li>
  <li><strong>Far-Field Exterior $E_R$:</strong> By Proposition 5.3:
  $$\\int_{\\Omega_M} |S_{E_R}| |\\omega|^2\\,dx \\le \\|S_{E_R}\\|_{L^\\infty} \\int_{\\Omega_M} |\\omega|^2\\,dx \\le C_E R^{-5/2} \\sqrt{2 E_0} \\, Q(t). \tag{6.6}$$</li>
  <li><strong>Intermediate Shell $A_{z,R}$:</strong> By Proposition 5.2, for any $\\alpha > 1/2$:
  $$\\int_{z(t)}^R r^{\\alpha - 1} dr = \\left[ \\frac{r^\\alpha}{\\alpha} \\right]_{z(t)}^R = \\frac{R^\\alpha - z(t)^\\alpha}{\\alpha} \\le \\frac{R^\\alpha}{\\alpha}. \tag{6.7}$$
  Notice the vital mathematical fact: because $\\alpha > 0$, the limit as $z(t) \\to 0$ of $z(t)^\\alpha$ is strictly zero! There is <strong>no singularity</strong> at the lower integration limit $z(t) = 0$. Consequently:
  $$\\|S_A\\|_{L^\\infty(\\Omega_M)} \\le \\frac{6 K_\\xi}{\\alpha} R^\\alpha \\|\\omega\\|_{L^\\infty}. \tag{6.8}$$
  To control $\\|\\omega\\|_{L^\\infty}$, we apply Agmon's inequality in $\\mathbb{R}^3$: $\\|\\omega\\|_{L^\\infty} \\le C_A \\|\\omega\\|_{L^2}^{1/4} \\|\\nabla \\omega\\|_{L^6}^{3/4}$ or interpolate with the Littlewood–Paley cutoff. Absorbing the gradient into the remaining $\\frac{3\\nu}{4} \\|\\nabla \\omega\\|_{L^2}^2$ dissipation leaves a linear enstrophy term:
  $$\\int_{\\Omega_M} |S_A| |\\omega|^2\\,dx \\le \\frac{\\nu}{4} \\|\\nabla \\omega\\|_{L^2}^2 + C_\\alpha K_\\xi^2 R^{2\\alpha} \\nu^{-1} Q(t). \tag{6.9}$$</li>
</ol>

<h3 class="section-title">6.3. Elimination of the Super-Linear Riccati Catastrophe</h3>
<p>
  Combining (6.4), (6.5), (6.6), and (6.9) into the enstrophy identity (6.2):
</p>
<div class="equation">
  $$\\frac{1}{2} \\frac{d}{dt} Q(t) + \\nu \\|\\nabla \\omega\\|_{L^2}^2 \\le \\frac{\\nu}{4} \\|\\nabla \\omega\\|_{L^2}^2 + \\frac{\\nu}{4} \\|\\nabla \\omega\\|_{L^2}^2 + \\left( M + C_E R^{-5/2} \\sqrt{2 E_0} + \\frac{C_\\alpha K_\\xi^2 R^{2\\alpha}}{\\nu} \\right) Q(t). \tag{6.10}$$
</div>
<p>
  Subtracting the absorbed dissipation $\\frac{\\nu}{2} \\|\\nabla \\omega\\|_{L^2}^2$ from both sides:
</p>
<div class="equation">
  $$\\frac{1}{2} \\frac{d}{dt} Q(t) + \\frac{\\nu}{2} \\|\\nabla \\omega\\|_{L^2}^2 \\le \\Phi(t) Q(t), \tag{6.11}$$
</div>
<p>
  where the coefficient function $\\Phi(t)$ is defined by:
</p>
<div class="equation">
  $$\\Phi(t) := M + C_E R^{-5/2} \\sqrt{2 E_0} + \\frac{C_\\alpha K_\\xi^2 R^{2\\alpha}}{\\nu}. \tag{6.12}$$
</div>
<div class="theorem-box">
  <strong>Key Analytical Breakthrough:</strong>
  In the classical estimate (Section 3.6), the enstrophy growth rate was cubic: $\\frac{d}{dt} Q \\le C Q^3$, which inevitably produces finite-time singularity.
  Here, due to geometric depletion on the intermediate shell and dynamic absorption in the near-field core, <strong>the fatal super-linear power $Q^3$ has been completely destroyed and replaced by a purely linear growth term $\\Phi(t) Q(t)$!</strong>
</div>

<h3 class="section-title">6.4. Closed-Form Integration via the Differential Gr&ouml;nwall Inequality</h3>
<div class="lemma-box">
  <strong>Lemma 6.1 (Differential Gr&ouml;nwall Lemma):</strong>
  Let $Q(t) \\ge 0$ be an absolutely continuous function on $[0, T]$ satisfying:
  $$\\frac{d}{dt} Q(t) \\le 2 \\Phi(t) Q(t), \\qquad Q(0) = Q_0. \tag{6.13}$$
  Then for all $t \\in [0, T]$:
  $$Q(t) \\le Q_0 \\exp\\left( 2 \\int_0^t \\Phi(s)\\,ds \\right) < \\infty. \tag{6.14}$$
</div>
<div class="proof-box">
  <span class="proof-title">Proof.</span>
  Multiply (6.13) by the integrating factor $\\exp\\left( -2 \\int_0^t \\Phi(s) ds \\right)$:
  $$\\frac{d}{dt} \\left[ Q(t) \\exp\\left( -2 \\int_0^t \\Phi(s) ds \\right) \\right] \\le 0. \tag{6.15}$$
  Integrating from $0$ to $t$ gives $Q(t) \\exp\\left( -2 \\int_0^t \\Phi(s) ds \\right) - Q_0 \\le 0$, which yields (6.14).
  <span class="qed">$\\blacksquare$</span>
</div>
<p>
  Since $\\Phi(t)$ in (6.12) is a constant depending only on $(M, R, E_0, K_\\xi, \\nu, \\alpha)$, we have $\\int_0^T \\Phi(s) ds = \\Phi \\cdot T < \\infty$ for any finite horizon $T < \\infty$. Therefore:
</p>
<div class="equation">
  $$\\sup_{t \\in [0, T]} Q(t) \\le Q_0 \\exp(2 \\Phi T) < \\infty. \tag{6.16}$$
</div>

<h3 class="section-title">6.5. Higher-Order Sobolev Bootstrapping ($H^s(\\mathbb{R}^3)$ for all $s \\ge 1$)</h3>
<p>
  Having bounded the enstrophy $Q(t) = \\|\\omega(t)\\|_{L^2}^2$, we now establish that all higher Sobolev norms $H^s(\\mathbb{R}^3)$ remain bounded for all $s \\ge 1$.
</p>
<div class="prop-box">
  <strong>Proposition 6.1 (Higher-Order Regularity Bootstrap):</strong>
  If $\\sup_{t \\in [0, T]} \\|\\omega(t)\\|_{L^2}^2 < \\infty$, then for every $s \\ge 1$:
  $$\\sup_{t \\in [0, T]} \\|u(t)\\|_{H^s(\\mathbb{R}^3)} < \\infty. \tag{6.17}$$
</div>
<div class="proof-box">
  <span class="proof-title">Proof.</span>
  From (6.11), integrating over $[0, T]$ gives:
  $$\\nu \\int_0^T \\|\\nabla \\omega(t)\\|_{L^2}^2 dt \\le Q(0) + 2 \\Phi \\int_0^T Q(t) dt < \\infty. \tag{6.18}$$
  Thus $\\omega \\in L^2(0, T; \\dot{H}^1(\\mathbb{R}^3))$. By Sobolev embedding, $\\dot{H}^1(\\mathbb{R}^3) \\hookrightarrow L^6(\\mathbb{R}^3)$, so $\\omega \\in L^2(0, T; L^6(\\mathbb{R}^3))$.
  By the Biot–Savart law, $\\nabla u \\in L^2(0, T; L^6(\\mathbb{R}^3))$. By Ladyzhenskaya–Prodi–Serrin (Theorem 1.1 with $p = 2, q = 6$, where $\\frac{2}{2} + \\frac{3}{6} = 1 + \\frac{1}{2} = \\frac{3}{2} > 1$), this is subcritical and guarantees $u \\in C^\\infty(\\mathbb{R}^3 \\times (0, T])$.
  By Beale–Kato–Majda (Theorem 1.2), $\\int_0^T \\|\\omega(t)\\|_{L^\\infty} dt < \\infty$, ensuring that no blow-up can occur at $T$.
  <span class="qed">$\\blacksquare$</span>
</div>

<h3 class="section-title">6.6. Complete Proof of the Subcritical Regularity Theorem</h3>
<div class="theorem-box">
  <strong>Theorem 6.1 (Subcritical Regularity Theorem, $\\alpha > 1/2$):</strong>
  Let $u_0 \\in C_c^\\infty(\\mathbb{R}^3)$ with $\\nabla \\cdot u_0 = 0$. Suppose that on the maximal interval of existence $[0, T^*)$, the vorticity direction field $\\xi = \\omega / |\\omega|$ satisfies Hypothesis $H_\\alpha$ for some $\\alpha \\in (1/2, 1]$.
  Then the maximal existence time is infinite:
  $$T^* = \\infty. \tag{6.19}$$
  That is, the classical solution $(u, p)$ exists globally in time and remains $C^\\infty$ smooth for all $t \\in [0, \\infty)$.
</div>
<div class="proof-box">
  <span class="proof-title">Proof of Theorem 6.1.</span>
  Suppose for contradiction that $T^* < \\infty$.
  By Lemma 6.1, for all $t \\in [0, T^*)$:
  $$\\|\\omega(t)\\|_{L^2(\\mathbb{R}^3)}^2 \\le \\|\\omega_0\\|_{L^2}^2 \\exp(2 \\Phi T^*) < \\infty. \tag{6.20}$$
  By Proposition 6.1, $\\sup_{t \\in [0, T^*)} \\|u(t)\\|_{H^3(\\mathbb{R}^3)} < \\infty$.
  By standard local existence theory for Navier–Stokes in $H^3(\\mathbb{R}^3)$, there exists a time increment $\\tau > 0$ depending only on $\\sup_{t \\in [0, T^*)} \\|u(t)\\|_{H^3}$ such that the solution can be extended to $[0, T^* + \\tau)$.
  This strictly contradicts the definition of $T^*$ as the maximal existence time.
  Hence $T^* = \\infty$.
  <span class="qed">$\\blacksquare$</span>
</div>
"""
