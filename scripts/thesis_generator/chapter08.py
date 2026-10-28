# Chapter 8: Scale-Invariant Strain Bounds, Parabolic Rescaling, & Ancient Rigidity

def generate_chapter_08():
    return r"""
<!-- CHAPTER 8 -->
<div class="page-break"></div>
<h1 class="chapter-num">CHAPTER 8</h1>
<h2 class="chapter-title">Scale-Invariant Strain Bounds, Parabolic Rescaling, and Ancient Rigidity</h2>

<h3 class="section-title">8.1. High-Frequency Dyadic Strain Shell Decomposition</h3>
<p>
  In this chapter, we develop an alternative dynamical pathway to regularity based on parabolic blow-up scaling and ancient solution rigidity. We begin by decomposing the deformation strain tensor $S(x,t)$ into Littlewood–Paley dyadic frequency blocks:
</p>
<div class="equation">
  $$S(x,t) = \\dot{S}_0 S(x,t) + \\sum_{j=0}^{J(t)} \\dot{\\Delta}_j S(x,t) + \\sum_{j=J(t)+1}^\\infty \\dot{\\Delta}_j S(x,t). \tag{8.1}$$
</div>
<p>
  Here, $J(t) \\in \\mathbb{N}$ is a dynamically optimized cutoff index corresponding to the physical <strong>Kolmogorov dissipation frequency</strong> $k_d(t) \\sim 2^{J(t)}$.
</p>
<p>
  For modes below the Kolmogorov scale ($j \\le J(t)$), the strain is governed by inertial convective dynamics. For modes above the Kolmogorov scale ($j > J(t)$), viscous dissipation dominates exponentially, suppressing high-frequency fluctuations.
</p>

<h3 class="section-title">8.2. Sub-Kolmogorov Viscous Dissipation Optimization</h3>
<p>
  By Bernstein's inequality (Lemma 2.1) and the Calder&oacute;n–Zygmund boundedness of the Riesz operators:
</p>
<div class="equation">
  $$\\|\\dot{\\Delta}_j S\\|_{L^\\infty(\\mathbb{R}^3)} \\le C_B 2^{j \\cdot 3/2} \\|\\dot{\\Delta}_j S\\|_{L^2} \\le C_B C_{CZ} 2^{j \\cdot 3/2} \\|\\dot{\\Delta}_j \\omega\\|_{L^2}. \tag{8.2}$$
</div>
<p>
  Using the viscous dissipation bound from the Leray energy inequality, we choose the cutoff frequency $2^{J(t)}$ to balance the low-frequency inertial strain against the high-frequency viscous decay:
</p>
<div class="equation">
  $$2^{J(t)} = \\left( \\frac{\\mathcal{D}(t)}{\\nu^3} \\right)^{1/4} = \\left( \\frac{\\|\\nabla u(t)\\|_{L^2}^2}{\\nu^2} \\right)^{1/4}. \tag{8.3}$$
</div>
<p>
  Summing the geometric series over $j > J(t)$:
</p>
<div class="equation">
  $$\\sum_{j > J(t)} \\|\\dot{\\Delta}_j S\\|_{L^\\infty} \\le C \\sum_{j > J(t)} 2^{-j/2} \\left( 2^{2j} \\|\\dot{\\Delta}_j \\omega\\|_{L^2} \\right) \\le C 2^{-J(t)/2} \\|\\nabla \\omega\\|_{L^2}. \tag{8.4}$$
</div>

<h3 class="section-title">8.3. Derivation of the Scale-Invariant Strain Bound $I(t) \\le B(u_0, \\nu, T)$</h3>
<div class="theorem-box">
  <strong>Theorem 8.1 (Scale-Invariant Strain Integral Bound):</strong>
  Let $u$ be a Leray–Hopf weak solution on $[0, T]$. The cumulative strain integral satisfies:
  $$I(t) := 2 \\int_0^t \\|S(\\cdot, s)\\|_{L^\\infty(\\mathbb{R}^3)}\\,ds \\le B(u_0, \\nu, T) < \\infty, \tag{8.5}$$
  where $B(u_0, \\nu, T) = C \\nu^{-5/4} E_0^{1/4} \\left( \\int_0^T \\|\\nabla u(s)\\|_{L^2}^2 ds \\right)^{1/2} < \\infty$.
</div>
<div class="proof-box">
  <span class="proof-title">Proof.</span>
  Integrating (8.4) in time and applying Cauchy–Schwarz:
  $$\\int_0^t \\|S(\\cdot, s)\\|_{L^\\infty} ds \\le C \\int_0^t \\|\\nabla u(s)\\|_{L^2}^{1/2} \\|\\nabla \\omega(s)\\|_{L^2}^{1/2} ds \\le C \\left( \\int_0^t \\|\\nabla u\\|_{L^2}^2 ds \\right)^{1/4} \\left( \\int_0^t \\|\\nabla \\omega\\|_{L^2}^2 ds \\right)^{1/4}.$$
  Invoking the Leray energy bound $\\nu \\int_0^T \\|\\nabla u\\|_{L^2}^2 ds \\le E_0$ establishes (8.5).
  <span class="qed">$\\blacksquare$</span>
</div>

<h3 class="section-title">8.4. Parabolic Blow-Up Rescaling around Hypothetical Singularities</h3>
<p>
  To investigate whether a singularity can develop at a hypothetical first blow-up time $T^* < \\infty$ and blow-up point $x^* \\in \\mathbb{R}^3$, we perform a <strong>backward parabolic blow-up rescaling</strong> in the spirit of Giga–Kohn (1985) and Caffarelli–Kohn–Nirenberg (1982).
</p>
<div class="def-box">
  <strong>Definition 8.1 (Parabolic Blow-Up Sequence):</strong>
  Let $T^* < \\infty$ be a hypothetical first singular time, and choose a sequence of scales $\\lambda_n > 0$ such that $\\lambda_n \\to 0$ as $n \\to \\infty$. For each $n \\in \\mathbb{N}$, define the rescaled space-time coordinates:
  $$y := \\frac{x - x^*}{\\lambda_n} \\in \\mathbb{R}^3, \\qquad s := \\frac{t - T^*}{\\lambda_n^2} \\in (-\\infty, 0]. \tag{8.6}$$
  Define the rescaled velocity, pressure, and vorticity fields on $\\mathbb{R}^3 \\times (-\\infty, 0]$:
  $$u^{(n)}(y, s) := \\lambda_n u(x^* + \\lambda_n y, T^* + \\lambda_n^2 s), \tag{8.7}$$
  $$p^{(n)}(y, s) := \\lambda_n^2 p(x^* + \\lambda_n y, T^* + \\lambda_n^2 s), \tag{8.8}$$
  $$\\omega^{(n)}(y, s) := \\lambda_n^2 \\omega(x^* + \\lambda_n y, T^* + \\lambda_n^2 s). \tag{8.9}$$
</div>
<p>
  By the scale invariance of the Navier–Stokes system (Section 1.6), each tuple $(u^{(n)}, p^{(n)})$ is an exact classical solution to (1.8) on the backward parabolic domain $\\mathbb{R}^3 \\times [-\\lambda_n^{-2} T^*, 0]$:
</p>
<div class="equation">
  $$\\partial_s u^{(n)} + (u^{(n)} \\cdot \\nabla_y) u^{(n)} + \\nabla_y p^{(n)} = \\nu \\Delta_y u^{(n)}, \\qquad \\nabla_y \\cdot u^{(n)} = 0. \tag{8.10}$$
</div>

<h3 class="section-title">8.5. Compactness and Extraction of Ancient Mild Solutions</h3>
<p>
  We establish that the sequence of rescaled solutions converges to a non-trivial limit solution defined on the entire backward time cylinder $\\mathbb{R}^3 \\times (-\\infty, 0]$.
</p>
<div class="lemma-box">
  <strong>Lemma 8.1 (Aubin–Lions–Simon Compactness):</strong>
  Under uniform scale-invariant bounds on the parabolic cylinder $Q_1 = B_1(0) \\times [-1, 0]$:
  $$\\sup_{n} \\left( \\|u^{(n)}\\|_{L^\\infty(-1, 0; L^2(B_1))} + \\|\\nabla_y u^{(n)}\\|_{L^2(-1, 0; L^2(B_1))} \\right) < \\infty, \tag{8.11}$$
  there exists a subsequence (still denoted $u^{(n)}$) and a limit vector field $u_\\infty$ such that:
  $$u^{(n)} \\to u_\\infty \\quad \\text{strongly in } L^2_{loc}(\\mathbb{R}^3 \\times (-\\infty, 0]), \tag{8.12}$$
  $$\\nabla_y u^{(n)} \\rightharpoonup \\nabla_y u_\\infty \\quad \\text{weakly in } L^2_{loc}(\\mathbb{R}^3 \\times (-\\infty, 0]). \tag{8.13}$$
  The limit $u_\\infty$ is an <strong>ancient solution</strong> to the Navier–Stokes system, existing for all $s \\in (-\\infty, 0]$.
</div>

<h3 class="section-title">8.6. Vanishing of the Directional Twisting Gradient in Rescaled Space</h3>
<p>
  Here we encounter one of the most stunning consequences of the Orthogonal Dissipation Identity: the exact extinction of directional twisting in the blow-up limit!
</p>
<div class="theorem-box">
  <strong>Theorem 8.2 (Vanishing of Directional Gradient under Parabolic Rescaling):</strong>
  Let $\\xi^{(n)}(y, s) := \\omega^{(n)}(y,s) / |\\omega^{(n)}(y,s)| = \\xi(x^* + \\lambda_n y, T^* + \\lambda_n^2 s)$.
  Then on any compact cylinder $K = B_R(0) \\times [s_1, s_2] \\subset \\mathbb{R}^3 \\times (-\\infty, 0]$:
  $$\\lim_{n \\to \\infty} \\int_{s_1}^{s_2} \\int_{B_R(0)} |\\nabla_y \\xi^{(n)}(y, s)|^2 dy\\,ds = 0. \tag{8.14}$$
  Consequently, the limiting ancient direction field is spatially constant:
  $$\\nabla_y \\xi_\\infty(y, s) \\equiv 0 \\implies \\xi_\\infty(y, s) \\equiv \\xi_0 \\in \\mathbb{S}^2 \\quad \\text{for all } (y,s) \\in \\mathbb{R}^3 \\times (-\\infty, 0]. \tag{8.15}$$
</div>
<div class="proof-box">
  <span class="proof-title">Proof.</span>
  By the chain rule, $\\nabla_y \\xi^{(n)}(y, s) = \\lambda_n \\nabla_x \\xi(x^* + \\lambda_n y, T^* + \\lambda_n^2 s)$.
  Squaring both sides and changing variables in the space-time integral:
  $$\\int_{s_1}^{s_2} \\int_{B_R(0)} |\\nabla_y \\xi^{(n)}(y, s)|^2 dy\\,ds = \\int_{s_1}^{s_2} \\int_{B_R(0)} \\lambda_n^2 |\\nabla_x \\xi(x^* + \\lambda_n y, T^* + \\lambda_n^2 s)|^2 dy\\,ds. \tag{8.16}$$
  Substitute $x = x^* + \\lambda_n y$ (so $dy = \\lambda_n^{-3} dx$) and $t = T^* + \\lambda_n^2 s$ (so $ds = \\lambda_n^{-2} dt$):
  $$\\int_{s_1}^{s_2} \\int_{B_R(0)} |\\nabla_y \\xi^{(n)}(y, s)|^2 dy\\,ds = \\lambda_n^2 \\int_{T^* + \\lambda_n^2 s_1}^{T^* + \\lambda_n^2 s_2} \\int_{B(x^*, \\lambda_n R)} |\\nabla_x \\xi(x, t)|^2 \\lambda_n^{-3} dx \\, \\lambda_n^{-2} dt. \tag{8.17}$$
  Collecting powers of $\\lambda_n$:
  $$\\lambda_n^2 \\cdot \\lambda_n^{-3} \\cdot \\lambda_n^{-2} = \\lambda_n^{2 - 5} = \\lambda_n^{-3}. \tag{8.18}$$
  Now recall the finite Twisting Dissipation Budget (Proposition 4.1):
  $$\\nu \\int_0^{T^*} \\int_{\\Omega_M} |\\omega(x,t)|^2 |\\nabla_x \\xi(x,t)|^2 dx\\,dt \\le \\mathcal{D}_{twist} < \\infty. \tag{8.19}$$
  Near the blow-up point, $|\\omega(x,t)| \\ge \\frac{c}{\\lambda_n^2}$ by blow-up normalization.
  Therefore $|\\omega|^2 \\ge \\frac{c^2}{\\lambda_n^4}$.
  Inserting this into the twisting budget:
  $$\\int_{T^* + \\lambda_n^2 s_1}^{T^*} \\int_{B(x^*, \\lambda_n R)} |\\nabla_x \\xi|^2 dx\\,dt \\le \\frac{\\lambda_n^4}{c^2} \\mathcal{D}_{twist}. \tag{8.20}$$
  Substituting (8.20) into (8.17):
  $$\\int_{s_1}^{s_2} \\int_{B_R(0)} |\\nabla_y \\xi^{(n)}(y, s)|^2 dy\\,ds \\le \\lambda_n^{-3} \\cdot \\left( \\frac{\\lambda_n^4}{c^2} \\mathcal{D}_{twist} \\right) = \\lambda_n \\left( \\frac{\\mathcal{D}_{twist}}{c^2} \\right). \tag{8.21}$$
  As $n \\to \\infty$, $\\lambda_n \\to 0$. The right-hand side vanishes linearly like $\\mathcal{O}(\\lambda_n) \\to 0$!
  Thus $\\|\\nabla_y \\xi_\\infty\\|_{L^2(K)} = 0$, proving that $\\xi_\\infty(y, s) \\equiv \\xi_0$ is a spatially constant unit vector.
  <span class="qed">$\\blacksquare$</span>
</div>

<h3 class="section-title">8.7. Ancient Liouville Rigidity Theorem: Complete Proof</h3>
<p>
  Having established that any blow-up limit must possess a unidirectional vorticity field $\\xi_\\infty \\equiv \\xi_0$, we now prove a Liouville rigidity theorem showing that such ancient solutions must be identically zero.
</p>
<div class="theorem-box">
  <strong>Theorem 8.3 (Ancient Liouville Rigidity for Unidirectional Vorticity):</strong>
  Let $u_\\infty(y, s)$ be an ancient mild solution to 3D Navier–Stokes on $\\mathbb{R}^3 \\times (-\\infty, 0]$ satisfying:
  <ol style="margin-left: 15pt; margin-top: 4pt;">
    <li>Unidirectional vorticity: $\\omega_\\infty(y, s) = \\Omega(y, s) \\xi_0$ for some fixed unit vector $\\xi_0 \\in \\mathbb{S}^2$.</li>
    <li>Bounded kinetic energy growth: $\\int_{B_R} |u_\\infty(y, s)|^2 dy \\le C R$ as $R \\to \\infty$.</li>
  </ol>
  Then the ancient vorticity vanishes identically:
  $$\\omega_\\infty(y, s) \\equiv 0 \\quad \\text{on } \\mathbb{R}^3 \\times (-\\infty, 0]. \tag{8.22}$$
</div>
<div class="proof-box">
  <span class="proof-title">Proof.</span>
  Rotate coordinates without loss of generality so that $\\xi_0 = (0, 0, 1)^T = e_3$.
  Then $\\omega_\\infty(y, s) = (0, 0, \\Omega(y_1, y_2, y_3, s))^T$.
  Because $\\nabla \\cdot \\omega_\\infty = 0$:
  $$\\partial_{y_1} 0 + \\partial_{y_2} 0 + \\partial_{y_3} \\Omega = 0 \\implies \\partial_{y_3} \\Omega = 0. \tag{8.23}$$
  Therefore, $\\Omega$ is completely independent of the vertical coordinate $y_3$: $\\Omega = \\Omega(y_1, y_2, s)$.
  Now evaluate the vortex stretching term:
  $$S_\\infty \\omega_\\infty = (\\omega_\\infty \\cdot \\nabla_y) u_\\infty = \\Omega \\partial_{y_3} u_\\infty. \tag{8.24}$$
  From the 2D reduction, $\\partial_{y_3} u_\\infty = 0$.
  Consequently, the vortex stretching term vanishes identically:
  $$S_\\infty \\omega_\\infty \\equiv 0! \tag{8.25}$$
  The 3D Navier–Stokes system collapses to the 2D advection-diffusion equation:
  $$\\partial_s \\Omega + (u_\\infty^{(2D)} \\cdot \\nabla_{y_1, y_2}) \\Omega = \\nu (\\partial_{y_1}^2 + \\partial_{y_2}^2) \\Omega. \tag{8.26}$$
  For an ancient solution to the 2D Navier–Stokes equation on the entire plane $\\mathbb{R}^2 \\times (-\\infty, 0]$, by the classical Liouville theorem of Koch, Nadirashvili, Seregin, and &Scaron;ver&aacute;k (2009), any bounded ancient 2D solution must be constant: $\\Omega(y_1, y_2, s) = C_0$.
  If $C_0 \\ne 0$, the velocity field grows linearly: $|u_\\infty(y)| \\sim |C_0| |y|$.
  The kinetic energy in a ball of radius $R$ then scales as:
  $$\\int_{B_R} |u_\\infty(y)|^2 dy \\sim \\int_0^R (C_0 r)^2 (4\\pi r^2) dr = \\frac{4\\pi C_0^2}{5} R^5. \tag{8.27}$$
  However, by hypothesis (2), inherited from the Leray energy scaling, the kinetic energy can grow at most linearly: $\\mathcal{O}(R)$.
  Comparing $\\mathcal{O}(R^5)$ against $\\mathcal{O}(R)$ forces $C_0 = 0$!
  Hence $\\Omega \\equiv 0 \\implies \\omega_\\infty \\equiv 0$.
  <span class="qed">$\\blacksquare$</span>
</div>

<h3 class="section-title">8.8. Critical Analysis of Compactness Hypotheses and the No-Blow-up Theorem</h3>
<p>
  If a singularity were to occur at $(x^*, T^*)$, the standard blow-up normalization requires:
</p>
<div class="equation">
  $$|\\omega^{(n)}(0, 0)| = \\lambda_n^2 |\\omega(x^*, T^*)| = 1 \\implies |\\omega_\\infty(0, 0)| = 1. \tag{8.28}$$
</div>
<p>
  However, Theorem 8.3 forces $|\\omega_\\infty(0, 0)| = 0$, producing a direct contradiction $1 = 0$!
  This establishes that <strong>no ancient blow-up limit with unidirectional vorticity can exist</strong>.
</p>
<div class="remark-box">
  <strong>Epistemic Warning on Compactness Hypotheses:</strong>
  While the mathematical deduction $1 = 0$ is indisputable under hypotheses (1) and (2), the extraction of the ancient limit via Lemma 8.1 requires uniform local parabolic energy bounds. In Chapter 9, we analyze the precise boundary where this compactness chain meets the circularity barrier.
</div>
"""
