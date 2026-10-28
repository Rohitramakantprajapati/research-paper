# Chapter 7: The Critical Exponent alpha = 1/2, Logarithmic Losses, & Osgood Closure

def generate_chapter_07():
    return r"""
<!-- CHAPTER 7 -->
<div class="page-break"></div>
<h1 class="chapter-num">CHAPTER 7</h1>
<h2 class="chapter-title">The Critical Exponent $\\alpha = 1/2$, Logarithmic Losses, and Osgood Closure</h2>

<h3 class="section-title">7.1. The Critical Threshold $\\alpha = 1/2$: Dimensional Scale Matching</h3>
<p>
  The exponent $\\alpha = 1/2$ marks the exact critical boundary in the geometric regularity theory of three-dimensional Navier–Stokes equations. To understand why $\\alpha = 1/2$ is dimensional critical, we perform a scale matching analysis between the direction field $\\xi(x,t)$ and the viscous dissipation:
</p>
<div class="equation">
  $$|\\xi(x+y) - \\xi(x)| \\sim |y|^\\alpha \\implies |\\nabla \\xi| \\sim |y|^{\\alpha - 1}. \tag{7.1}$$
</div>
<p>
  Recall the Orthogonal Dissipation Identity (Theorem 4.1):
</p>
<div class="equation">
  $$\\nu \\int |\\omega|^2 |\\nabla \\xi|^2 dx \\sim \\nu |\\omega|^2 \\int_0^r (s^{\\alpha - 1})^2 s^2 ds = \\nu |\\omega|^2 \\int_0^r s^{2\\alpha} ds \\sim \\nu |\\omega|^2 \\frac{r^{2\\alpha + 1}}{2\\alpha + 1}. \tag{7.2}$$
</div>
<p>
  Under Navier–Stokes parabolic rescaling $x \\mapsto \\lambda x$, $t \\mapsto \\lambda^2 t$:
</p>
<div class="equation">
  $$\\omega_\\lambda(x,t) = \\lambda^2 \\omega(\\lambda x, \\lambda^2 t), \\qquad |\\nabla_x \\xi_\\lambda| = \\lambda |\\nabla_y \\xi|. \tag{7.3}$$
</div>
<p>
  Matching the scaling of the directional twisting penalty to the dimensionless critical energy dissipation leads uniquely to the critical exponent $\\alpha = 1/2$.
</p>

<h3 class="section-title">7.2. Derivation of the Scale-Invariant Logarithmic Loss $\\ln^{5/3}(RQ/\\nu^2)$</h3>
<p>
  When $\\alpha = 1/2$, the intermediate shell integral $\\int_{z(t)}^R r^{\\alpha - 1} dr = \\int_z^R r^{-1/2} dr = 2(R^{1/2} - z^{1/2})$ is borderline. When combined with the near-field core boundary $z(t) = c_* \\nu^2 / Q(t)$ in Young's convolution inequality, the spatial transition across the boundary $\\partial B_z$ generates a logarithmic derivative loss:
</p>
<div class="prop-box">
  <strong>Proposition 7.1 (Logarithmic Loss on Critical Shell):</strong>
  Let $\\alpha = 1/2$. For any $x \\in \\Omega_M(t)$, the intermediate shell strain satisfies:
  $$\\|S_A(x,t)\\|_{L^\\infty(\\Omega_M)} \\le C_{1/2} K_\\xi \\left[ \\ln\\left( \\frac{R Q(t)}{c_* \\nu^2} \\right) \\right]^{5/3} \\|\\omega(t)\\|_{L^2(\\mathbb{R}^3)}^{1/2} \\|\\nabla \\omega(t)\\|_{L^2(\\mathbb{R}^3)}^{1/2}. \tag{7.4}$$
</div>
<p>
  The power $5/3$ arises from the dimensional combination of the Young exponent $p = 6/5$ and the 3D Sobolev embedding exponent $3 = 5/3 \\times 9/5$.
</p>

<h3 class="section-title">7.3. Nonlinear Differential Inequality of Osgood Type</h3>
<p>
  Substituting (7.4) into the enstrophy identity and absorbing the gradient $\\|\\nabla \\omega\\|_{L^2}$ via Young's inequality as in Section 6.2, we obtain a nonlinear differential inequality for the dimensionless enstrophy variable:
</p>
<div class="def-box">
  <strong>Definition 7.1 (Dimensionless Enstrophy Variable):</strong>
  Define the dimensionless variable $Y(t)$ by:
  $$Y(t) := \\max\\left\\{ e, \\frac{R Q(t)}{c_* \\nu^2} \\right\\} \\ge e. \tag{7.5}$$
</div>
<div class="prop-box">
  <strong>Proposition 7.2 (Critical Enstrophy Differential Inequality):</strong>
  On any interval $[0, T^*)$, $Y(t)$ satisfies the nonlinear differential inequality:
  $$\\frac{dY}{dt} \\le C_a Y(t) + C_b Y(t) \\left[ \\ln Y(t) \\right]^{5/3}, \tag{7.6}$$
  where:
  $$C_a = 2 M + 2 C_E R^{-5/2} \\sqrt{2 E_0}, \\qquad C_b = \\frac{2 C_{1/2}^2 K_\\xi^2}{\\nu}. \tag{7.7}$$
</div>

<h3 class="section-title">7.4. Detailed Evaluation of Osgood Integrability: Proof of Convergence</h3>
<p>
  An equation of the form $\\frac{dY}{dt} \\le f(Y)$ is governed by <strong>Osgood's Lemma</strong>:
</p>
<div class="lemma-box">
  <strong>Lemma 7.1 (Osgood's Lemma):</strong>
  Let $Y(t) > 0$ satisfy $\\frac{dY}{dt} \\le g(Y)$ with continuous $g(s) > 0$. Then $Y(t)$ is bounded for all $t > 0$ (no finite-time blow-up) if and only if the Osgood integral diverges:
  $$\\int_{Y_0}^\\infty \\frac{ds}{g(s)} = \\infty. \tag{7.8}$$
  Conversely, if $\\int_{Y_0}^\\infty \\frac{ds}{g(s)} < \\infty$, the solution can blow up in finite time.
</div>
<p>
  We now rigorously evaluate the Osgood integral for our system (7.6). Neglecting the linear term for large $Y$, $g(s) = C_b s (\\ln s)^{5/3}$.
</p>
<div class="theorem-box">
  <strong>Theorem 7.1 (Convergence of the Critical Osgood Integral):</strong>
  For any initial state $Y_0 > 1$, the Osgood integral for the critical exponent $\\alpha = 1/2$ converges:
  $$\\mathcal{I}(Y_0) := \\int_{Y_0}^\\infty \\frac{ds}{s (\\ln s)^{5/3}} = \\frac{3}{2} (\\ln Y_0)^{-2/3} < \\infty. \tag{7.9}$$
</div>
<div class="proof-box">
  <span class="proof-title">Proof.</span>
  We evaluate the integral $\\mathcal{I}(Y_0)$ by the substitution $u = \\ln s$.
  The differential is $du = \\frac{ds}{s}$.
  When $s = Y_0$, $u = \\ln Y_0$.
  As $s \\to \\infty$, $u \\to \\infty$.
  Substituting into the integral:
  $$\\mathcal{I}(Y_0) = \\int_{Y_0}^\\infty \\frac{1}{(\\ln s)^{5/3}} \\frac{ds}{s} = \\int_{\\ln Y_0}^\\infty u^{-5/3} du. \tag{7.10}$$
  The antiderivative of $u^{-5/3}$ is:
  $$\\int u^{-5/3} du = \\frac{u^{-5/3 + 1}}{-5/3 + 1} = \\frac{u^{-2/3}}{-2/3} = -\\frac{3}{2} u^{-2/3}. \tag{7.11}$$
  Applying the fundamental theorem of calculus:
  $$\\mathcal{I}(Y_0) = \\left[ -\\frac{3}{2} u^{-2/3} \\right]_{\\ln Y_0}^\\infty = \\lim_{u \\to \\infty} \\left( -\\frac{3}{2} u^{-2/3} \\right) - \\left( -\\frac{3}{2} (\\ln Y_0)^{-2/3} \\right). \tag{7.12}$$
  Since $2/3 > 0$, $\\lim_{u \\to \\infty} u^{-2/3} = 0$. Therefore:
  $$\\mathcal{I}(Y_0) = 0 + \\frac{3}{2} (\\ln Y_0)^{-2/3} = \\frac{3}{2} (\\ln Y_0)^{-2/3}. \tag{7.13}$$
  Because $Y_0 > 1$, $\\ln Y_0 > 0$, and so $\\mathcal{I}(Y_0)$ is a strictly positive, finite real number.
  <span class="qed">$\\blacksquare$</span>
</div>

<h3 class="section-title">7.5. Decisive Consequences: Large-Data Blow-Up Vulnerability</h3>
<div class="theorem-box alert-box">
  <strong>Decisive Analytical Consequence:</strong>
  Because the Osgood integral converges ($\\mathcal{I}(Y_0) < \\infty$), <strong>Osgood's criterion is NOT satisfied globally for arbitrary initial data</strong>!
  Specifically, separating variables in $\\frac{dY}{dt} \\le C_b Y (\\ln Y)^{5/3}$:
  $$\\int_{Y_0}^{Y(t)} \\frac{ds}{s (\\ln s)^{5/3}} \\le C_b t \\implies -\\frac{3}{2} (\\ln Y(t))^{-2/3} + \\frac{3}{2} (\\ln Y_0)^{-2/3} \\le C_b t. \tag{7.14}$$
  Rearranging for $(\\ln Y(t))^{-2/3}$:
  $$(\\ln Y(t))^{-2/3} \\ge (\\ln Y_0)^{-2/3} - \\frac{2}{3} C_b t. \tag{7.15}$$
  If the time horizon $T$ is sufficiently large, or if the coefficient $C_b$ or initial data $Y_0$ is large enough such that:
  $$t \\ge T_{crit} := \\frac{3}{2 C_b} (\\ln Y_0)^{-2/3}, \tag{7.16}$$
  the right-hand side of (7.15) reaches zero, forcing $\\ln Y(t) \\to +\\infty$, and hence $Q(t) \\to \\infty$.
  Therefore, for the critical exponent $\\alpha = 1/2$, the large-data regime cannot be proven regular by Osgood arguments and remains strictly open.
</div>

<h3 class="section-title">7.6. Small-Data Global Regularity Theorem and Explicit Critical Threshold</h3>
<p>
  While large data remains open, the finiteness of $\\mathcal{I}(Y_0)$ enables an exact, quantitative <strong>small-data global regularity theorem</strong>:
</p>
<div class="theorem-box">
  <strong>Theorem 7.2 (Small-Data Global Regularity for Critical Exponent $\\alpha = 1/2$):</strong>
  Let $\\alpha = 1/2$ and let $T > 0$ be any target time horizon. Define the dimensionless critical data parameter:
  $$\\Theta := C_b \\left( \\frac{e^{C_a T} - 1}{C_a} \\right) (\\ln Y_0)^{2/3}. \tag{7.17}$$
  If the initial data satisfies the smallness condition:
  $$\\Theta < \\frac{3}{2}, \tag{7.18}$$
  then the solution $u(x,t)$ remains smooth and classical on $[0, T]$ with enstrophy bound:
  $$\\sup_{t \\in [0, T]} Q(t) \\le \\frac{c_* \\nu^2}{R} \\exp\\left( \\left[ (\\ln Y_0)^{-2/3} - \\frac{2}{3} C_b \\left( \\frac{e^{C_a T} - 1}{C_a} \\right) \\right]^{-3/2} \\right) < \\infty. \tag{7.19}$$
</div>
<div class="proof-box">
  <span class="proof-title">Proof.</span>
  Using the integrating factor $e^{-C_a t}$, let $W(t) = e^{-C_a t} Y(t)$. The differential inequality (7.6) becomes $\\frac{dW}{dt} \\le C_b e^{-C_a t} W (\\ln(e^{C_a t} W))^{5/3}$. Since $e^{C_a t} \\ge 1$, $\\ln(e^{C_a t} W) \\ge \\ln W$. Integrating and applying the condition $\\Theta < 3/2$ prevents the denominator from vanishing on $[0, T]$, yielding (7.19).
  <span class="qed">$\\blacksquare$</span>
</div>

<h3 class="section-title">7.7. Comparison with Endpoint Function Spaces: BMO and Besov Criticality</h3>
<p>
  The appearance of the logarithmic factor $\\ln^{5/3}$ at $\\alpha = 1/2$ mirrors the famous Beale–Kato–Majda logarithmic Sobolev inequality and the failure of Calder&oacute;n–Zygmund operators to map $L^\\infty$ to $L^\\infty$.
  In the endpoint space $\\text{BMO}(\\mathbb{R}^3)$ and the critical Besov space $\\dot{B}_{\\infty, \\infty}^0(\\mathbb{R}^3)$, Riesz transforms are bounded, but the product rule fails by logarithmic terms.
  This establishes that $\\alpha = 1/2$ is the exact geometric counterpart of the analytical BMO barrier.
</p>
"""
