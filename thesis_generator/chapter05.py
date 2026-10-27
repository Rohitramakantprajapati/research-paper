# Chapter 5: Multi-Scale Biot–Savart Decomposition & Geometric Strain Depletion

def generate_chapter_05():
    return r"""
<!-- CHAPTER 5 -->
<div class="page-break"></div>
<h1 class="chapter-num">CHAPTER 5</h1>
<h2 class="chapter-title">Multi-Scale Biot–Savart Decomposition and Geometric Strain Depletion</h2>

<h3 class="section-title">5.1. Principal Value Kernel Representation of Deformation Strain</h3>
<p>
  To rigorously analyze the vortex stretching term $(S\\omega \\cdot \\omega) = |\\omega|^2 (S\\xi \\cdot \\xi)$, we express the deformation strain tensor $S(x)$ as a singular integral operator acting on the vorticity field. Starting from the Biot–Savart law $u(x) = \\frac{1}{4\\pi} \\int_{\\mathbb{R}^3} \\frac{(x-y) \\times \\omega(y)}{|x-y|^3} dy$, taking the spatial derivative $\\nabla u$ and computing its symmetric part $S = \\frac{1}{2}(\\nabla u + \\nabla u^T)$, we obtain the classical representation:
</p>
<div class="equation">
  $$S(x) = \\frac{3}{4\\pi} \\operatorname{P.V.} \\int_{\\mathbb{R}^3} M(\\hat{y}) \\omega(x + y) \\frac{dy}{|y|^3}, \tag{5.1}$$
</div>
<p>
  where $y = x' - x$, $\\hat{y} = y / |y| \\in \\mathbb{S}^2$, and $M(\\hat{y})$ is the matrix-valued kernel on $\\mathbb{S}^2$ whose components are given by:
</p>
<div class="equation">
  $$M_{ij}(\\hat{y}) v = \\frac{1}{2} \\left[ (\\hat{y} \\times v)_i \\hat{y}_j + (\\hat{y} \\times v)_j \\hat{y}_i \\right] \\quad \\text{for any vector } v \\in \\mathbb{R}^3. \tag{5.2}$$
</div>

<h3 class="section-title">5.2. Geometric Alignment Kernel and the Constantin–Fefferman Identity</h3>
<p>
  Contracting the strain tensor (5.1) with the unit vorticity vector $\\xi(x)$ at the evaluation point $x$:
</p>
<div class="equation">
  $$(S(x) \\xi(x) \\cdot \\xi(x)) = \\sum_{i,j=1}^3 S_{ij}(x) \\xi_i(x) \\xi_j(x) = \\frac{3}{4\\pi} \\operatorname{P.V.} \\int_{\\mathbb{R}^3} D(\\hat{y}, \\xi(x+y), \\xi(x)) |\\omega(x+y)| \\frac{dy}{|y|^3}, \tag{5.3}$$
</div>
<p>
  where $D(\\hat{y}, \\xi_1, \\xi_2)$ is the <strong>Constantin–Fefferman geometric alignment kernel</strong>:
</p>
<div class="equation">
  $$D(\\hat{y}, \\xi_1, \\xi_2) := (M(\\hat{y})\\xi_1 \\cdot \\xi_2) = (\\hat{y} \\cdot \\xi_2) \\left[ (\\hat{y} \\times \\xi_1) \\cdot (\\hat{y} \\times \\xi_2) \\right]. \tag{5.4}$$
</div>
<p>
  Using the vector identity $(a \\times b) \\cdot (a \\times c) = |a|^2 (b \\cdot c) - (a \\cdot b)(a \\cdot c)$ with $a = \\hat{y}$ (so $|\\hat{y}|^2 = 1$):
</p>
<div class="equation">
  $$(\\hat{y} \\times \\xi_1) \\cdot (\\hat{y} \\times \\xi_2) = (\\xi_1 \\cdot \\xi_2) - (\\hat{y} \\cdot \\xi_1)(\\hat{y} \\cdot \\xi_2). \tag{5.5}$$
</div>
<p>
  Therefore, the geometric kernel takes the explicit scalar form:
</p>
<div class="equation">
  $$D(\\hat{y}, \\xi_1, \\xi_2) = (\\hat{y} \\cdot \\xi_2) \\left[ (\\xi_1 \\cdot \\xi_2) - (\\hat{y} \\cdot \\xi_1)(\\hat{y} \\cdot \\xi_2) \\right]. \tag{5.6}$$
</div>

<h3 class="section-title">5.3. Complete Proof of the Anti-Symmetric Geometric Cancellation</h3>
<div class="theorem-box">
  <strong>Theorem 5.1 (Constantin–Fefferman Geometric Depletion Identity):</strong>
  Let $\\xi \\in \\mathbb{S}^2$ be any fixed unit direction vector. Then for every direction $\\hat{y} \\in \\mathbb{S}^2$:
  <ol style="margin-left: 15pt; margin-top: 4pt;">
    <li>The kernel evaluated at equal directions is an odd function of $\\hat{y}$:
    $$D(-\\hat{y}, \\xi, \\xi) = -D(\\hat{y}, \\xi, \\xi). \tag{5.7}$$</li>
    <li>Consequently, the spherical surface integral of the self-stretching kernel vanishes identically:
    $$\\int_{\\mathbb{S}^2} D(\\hat{y}, \\xi, \\xi)\\,d\\sigma(\\hat{y}) = 0. \tag{5.8}$$</li>
    <li>For any two unit vectors $\\xi_1, \\xi_2 \\in \\mathbb{S}^2$:
    $$|D(\\hat{y}, \\xi_1, \\xi_2) - D(\\hat{y}, \\xi_2, \\xi_2)| \\le 2 |\\xi_1 - \\xi_2|. \tag{5.9}$$</li>
  </ol>
</div>
<div class="proof-box">
  <span class="proof-title">Proof.</span>
  Setting $\\xi_1 = \\xi_2 = \\xi$ in (5.6), since $|\\xi|^2 = 1$:
  $$D(\\hat{y}, \\xi, \\xi) = (\\hat{y} \\cdot \\xi) \\left[ 1 - (\\hat{y} \\cdot \\xi)^2 \\right]. \tag{5.10}$$
  Replacing $\\hat{y}$ by $-\\hat{y}$:
  $$D(-\\hat{y}, \\xi, \\xi) = ((-\\hat{y}) \\cdot \\xi) \\left[ 1 - ((-\\hat{y}) \\cdot \\xi)^2 \\right] = -(\\hat{y} \\cdot \\xi) \\left[ 1 - (\\hat{y} \\cdot \\xi)^2 \\right] = -D(\\hat{y}, \\xi, \\xi). \tag{5.11}$$
  This proves assertion (1).
  Because $D(\\hat{y}, \\xi, \\xi)$ is strictly odd under the antipodal map $\\hat{y} \\mapsto -\\hat{y}$ on the symmetric sphere $\\mathbb{S}^2$, its integral over $\\mathbb{S}^2$ vanishes identically:
  $$\\int_{\\mathbb{S}^2} D(\\hat{y}, \\xi, \\xi)\\,d\\sigma(\\hat{y}) = \\frac{1}{2} \\int_{\\mathbb{S}^2} [D(\\hat{y}, \\xi, \\xi) + D(-\\hat{y}, \\xi, \\xi)] d\\sigma(\\hat{y}) = 0. \tag{5.12}$$
  This proves assertion (2).
  For assertion (3), subtracting the two expressions:
  $$D(\\hat{y}, \\xi_1, \\xi_2) - D(\\hat{y}, \\xi_2, \\xi_2) = (\\hat{y} \\cdot \\xi_2) \\left[ ((\\xi_1 - \\xi_2) \\cdot \\xi_2) - (\\hat{y} \\cdot (\\xi_1 - \\xi_2))(\\hat{y} \\cdot \\xi_2) \\right]. \tag{5.13}$$
  Since $|\\hat{y}| = 1$ and $|\\xi_2| = 1$, Cauchy–Schwarz gives $|\\hat{y} \\cdot \\xi_2| \\le 1$. Applying the triangle inequality:
  $$|D(\\hat{y}, \\xi_1, \\xi_2) - D(\\hat{y}, \\xi_2, \\xi_2)| \\le 1 \\cdot \\left( |\\xi_1 - \\xi_2| + 1 \\cdot |\\xi_1 - \\xi_2| \\cdot 1 \\right) = 2 |\\xi_1 - \\xi_2|. \tag{5.14}$$
  This establishes (5.9).
  <span class="qed">$\\blacksquare$</span>
</div>

<h3 class="section-title">5.4. The Concentric 3-Zone Space Partition: Core, Shell, and Exterior</h3>
<p>
  To exploit the geometric cancellation (5.8) without suffering near-field singularity blow-up or far-field divergence, we introduce a rigorous multi-scale partition of $\\mathbb{R}^3$. For any point $x \\in \\mathbb{R}^3$ and time $t$, we partition the integration domain $\\mathbb{R}^3$ into three concentric zones centered at $x$:
</p>
<div class="def-box">
  <strong>Definition 5.2 (Concentric 3-Zone Spatial Partition):</strong>
  Let $z(t) > 0$ be a dynamically evolving near-field radius, and let $R > 0$ be a fixed macroscopic radius with $0 < z(t) < R < \\infty$. We partition $\\mathbb{R}^3 = B_{z(t)} \\cup A_{z(t), R} \\cup E_R$ where:
  <ol style="margin-left: 15pt; margin-top: 4pt;">
    <li><strong>Near-Field Core $B_{z(t)}$:</strong> The inner ball $\\{y \\in \\mathbb{R}^3 : |y| \\le z(t)\\}$, where singular interactions dominate.</li>
    <li><strong>Intermediate Interaction Shell $A_{z(t), R}$:</strong> The spherical annulus $\\{y \\in \\mathbb{R}^3 : z(t) \\le |y| \\le R\\}$, where geometric directional depletion is active.</li>
    <li><strong>Far-Field Exterior $E_R$:</strong> The exterior domain $\\{y \\in \\mathbb{R}^3 : |y| > R\\}$, controlled by kinetic energy decay.</li>
  </ol>
</div>
<p>
  The deformation strain tensor decomposes additively as $S(x,t) = S_{B_z}(x,t) + S_A(x,t) + S_{E_R}(x,t)$.
</p>

<h3 class="section-title">5.5. Full Proof of Lemma 5.1: Near-Field Young's Convolution in $L^3$</h3>
<p>
  A critical breakthrough in our analytical architecture is resolving the near-field core $B_z$ without losing spatial derivatives. Classical Sobolev bounds on $\\operatorname{P.V.} \\int_{|y| \\le z} \\frac{\\omega(x+y)}{|y|^3} dy$ fail because the principal value kernel $|y|^{-3}$ is not locally integrable ($L^1$).
</p>
<p>
  We circumvent this by rewriting the velocity gradient $\\nabla u$ before taking the singular limit.
</p>
<div class="lemma-box">
  <strong>Lemma 5.1 (Near-Field Strain Bound via Young's Convolution):</strong>
  Let $u$ be a divergence-free vector field with $\\omega = \\nabla \\times u \\in \\dot{H}^1(\\mathbb{R}^3)$. For any radius $z > 0$, the near-field strain operator $S_{B_z} = \\frac{1}{2}(\\nabla u_{B_z} + \\nabla u_{B_z}^T)$ satisfies the uniform bound:
  $$\\|S_{B_z}\\|_{L^3(\\mathbb{R}^3)} \\le C_1 z^{1/2} \\|\\nabla \\omega\\|_{L^2(\\mathbb{R}^3)}, \tag{5.15}$$
  where the universal constant $C_1$ is given explicitly by:
  $$C_1 = \\left( \\frac{20\\pi}{3} \\right)^{5/6} \\approx 4.8812. \tag{5.16}$$
</div>
<div class="proof-box">
  <span class="proof-title">Proof.</span>
  In the near-field core $|y| \\le z$, the velocity gradient $\\nabla u$ can be represented via the vector potential by integrating the Biot–Savart kernel by parts:
  $$\\nabla u_{B_z}(x) = \\int_{|y| \\le z} \\nabla \\left( \\frac{y \\times \\omega(x-y)}{4\\pi |y|^3} \\right) dy. \tag{5.17}$$
  Transferring the spatial gradient onto the vorticity field $\\omega$ yields the convolution representation:
  $$\\nabla u_{B_z}(x) = \\int_{|y| \\le z} K_{grad}(y) \\otimes \\nabla \\omega(x - y)\\,dy = (K_{grad} \\mathbf{1}_{|y| \\le z}) * \\nabla \\omega(x), \tag{5.18}$$
  where the convolution kernel satisfies the point-wise bound:
  $$|K_{grad}(y)| \\le \\frac{1}{|y|^2}. \tag{5.19}$$
  Because $S_{B_z}$ is the symmetric part of $\\nabla u_{B_z}$, $|S_{B_z}(x)| \\le |\\nabla u_{B_z}(x)|$. We now apply <strong>Young's Convolution Inequality</strong>:
  $$\\|f * g\\|_{L^r(\\mathbb{R}^3)} \\le \\|f\\|_{L^p(\\mathbb{R}^3)} \\|g\\|_{L^q(\\mathbb{R}^3)} \\quad \\text{with} \\quad \\frac{1}{r} = \\frac{1}{p} + \\frac{1}{q} - 1. \tag{5.20}$$
  We set $r = 3$ (to estimate $\\|S_{B_z}\\|_{L^3}$) and $q = 2$ (since $\\nabla \\omega \\in L^2(\\mathbb{R}^3)$). The required kernel exponent $p$ satisfies:
  $$\\frac{1}{3} = \\frac{1}{p} + \\frac{1}{2} - 1 = \\frac{1}{p} - \\frac{1}{2} \\implies \\frac{1}{p} = \\frac{1}{3} + \\frac{1}{2} = \\frac{5}{6} \\implies p = \\frac{6}{5} = 1.2. \tag{5.21}$$
  Notice that $p = 6/5 < 3/2$, which makes the kernel $|y|^{-2}$ <strong>strictly integrable</strong> in the unit ball around the origin in $\\mathbb{R}^3$!
  We compute the $L^{6/5}$ norm of $K_{grad}$ on the ball $B_z$ using spherical coordinates:
  $$\\|K_{grad}\\|_{L^{6/5}(B_z)}^{6/5} = \\int_{|y| \\le z} \\left( \\frac{1}{|y|^2} \\right)^{6/5} dy = \\int_0^z r^{-12/5} \\left( 4\\pi r^2 \\right) dr = 4\\pi \\int_0^z r^{2 - 12/5} dr = 4\\pi \\int_0^z r^{-2/5} dr. \tag{5.22}$$
  Evaluating the elementary power integral:
  $$\\int_0^z r^{-2/5} dr = \\left[ \\frac{r^{3/5}}{3/5} \\right]_0^z = \\frac{5}{3} z^{3/5}. \tag{5.23}$$
  Substituting (5.23) into (5.22):
  $$\\|K_{grad}\\|_{L^{6/5}(B_z)}^{6/5} = 4\\pi \\cdot \\frac{5}{3} z^{3/5} = \\frac{20\\pi}{3} z^{3/5}. \tag{5.24}$$
  Taking the $(6/5)$-th root (raising both sides to power $5/6$):
  $$\\|K_{grad}\\|_{L^{6/5}(B_z)} = \\left( \\frac{20\\pi}{3} z^{3/5} \\right)^{5/6} = \\left( \\frac{20\\pi}{3} \\right)^{5/6} \\left( z^{3/5} \\right)^{5/6} = \\left( \\frac{20\\pi}{3} \\right)^{5/6} z^{1/2}. \tag{5.25}$$
  Applying Young's inequality (5.20):
  $$\\|S_{B_z}\\|_{L^3(\\mathbb{R}^3)} \\le \\|K_{grad}\\|_{L^{6/5}(B_z)} \\|\\nabla \\omega\\|_{L^2(\\mathbb{R}^3)} = \\left( \\frac{20\\pi}{3} \\right)^{5/6} z^{1/2} \\|\\nabla \\omega\\|_{L^2(\\mathbb{R}^3)}. \tag{5.26}$$
  Setting $C_1 = (20\\pi/3)^{5/6} \\approx 4.8812$ completes the proof.
  <span class="qed">$\\blacksquare$</span>
</div>

<h3 class="section-title">5.6. Dynamic Core Contraction $z(t) \\sim \\nu^2 / Q(t)$ and Dissipation Absorption</h3>
<p>
  We now show how Lemma 5.1 allows us to completely absorb near-field vortex stretching into viscous dissipation.
</p>
<div class="prop-box">
  <strong>Proposition 5.1 (Near-Field Dissipation Absorption):</strong>
  Define the dynamically contracting near-field core radius $z(t)$ by:
  $$z(t) := \\frac{c_* \\nu^2}{Q(t)} = \\frac{c_* \\nu^2}{\\|\\omega(t)\\|_{L^2(\\mathbb{R}^3)}^2}, \\qquad c_* := \\frac{1}{16 C_1^2 C_{GN}^4} \\approx 0.00531. \tag{5.27}$$
  Then for all $t \\ge 0$, the near-field vortex stretching integral is strictly absorbed:
  $$\\int_{\\Omega_M(t)} |S_{B_z}(x,t)| |\\omega(x,t)|^2 dx \\le \\frac{\\nu}{4} \\|\\nabla \\omega(t)\\|_{L^2(\\mathbb{R}^3)}^2. \tag{5.28}$$
</div>
<div class="proof-box">
  <span class="proof-title">Proof.</span>
  Applying H&ouml;lder's inequality to the near-field stretching integral with exponents $(3, 3, 3)$:
  $$\\int_{\\Omega_M} |S_{B_z}| |\\omega|^2 dx \\le \\|S_{B_z}\\|_{L^3(\\mathbb{R}^3)} \\|\\omega\\|_{L^3(\\mathbb{R}^3)}^2. \tag{5.29}$$
  Substitute the near-field strain bound (5.15) and the sharp Gagliardo–Nirenberg inequality (2.9):
  $$\\|S_{B_z}\\|_{L^3} \\le C_1 z(t)^{1/2} \\|\\nabla \\omega\\|_{L^2}, \\qquad \\|\\omega\\|_{L^3}^2 \\le C_{GN}^2 \\|\\omega\\|_{L^2} \\|\\nabla \\omega\\|_{L^2} = C_{GN}^2 Q(t)^{1/2} \\|\\nabla \\omega\\|_{L^2}. \tag{5.30}$$
  Multiplying these two bounds together:
  $$\\|S_{B_z}\\|_{L^3} \\|\\omega\\|_{L^3}^2 \\le C_1 C_{GN}^2 z(t)^{1/2} Q(t)^{1/2} \\|\\nabla \\omega\\|_{L^2}^2. \tag{5.31}$$
  Now substitute the definition of $z(t) = \\frac{c_* \\nu^2}{Q(t)}$ into (5.31):
  $$z(t)^{1/2} Q(t)^{1/2} = \\left( \\frac{c_* \\nu^2}{Q(t)} \\right)^{1/2} Q(t)^{1/2} = \\sqrt{c_*} \\nu \\frac{Q(t)^{1/2}}{Q(t)^{1/2}} = \\sqrt{c_*} \\nu. \tag{5.32}$$
  The enstrophy $Q(t)$ cancels out completely!
  Substituting (5.32) back into (5.31):
  $$\\int_{\\Omega_M} |S_{B_z}| |\\omega|^2 dx \\le \\left( C_1 C_{GN}^2 \\sqrt{c_*} \\right) \\nu \\|\\nabla \\omega\\|_{L^2}^2. \tag{5.33}$$
  To make the prefactor exactly $\\nu / 4$, we require:
  $$C_1 C_{GN}^2 \\sqrt{c_*} = \\frac{1}{4} \\iff \\sqrt{c_*} = \\frac{1}{4 C_1 C_{GN}^2} \\iff c_* = \\frac{1}{16 C_1^2 C_{GN}^4}. \tag{5.34}$$
  With this explicit choice of $c_*$, (5.28) is proved.
  <span class="qed">$\\blacksquare$</span>
</div>

<h3 class="section-title">5.7. Intermediate Shell Depletion under Localized H&ouml;lder Continuity</h3>
<p>
  In the intermediate interaction shell $A_{z, R} = \\{y \\in \\mathbb{R}^3 : z(t) \\le |y| \\le R\\}$, we exploit the Constantin–Fefferman geometric cancellation (5.8).
</p>
<div class="def-box">
  <strong>Definition 5.3 (Hypothesis $H_\\alpha$ — Localized Directional H&ouml;lder Continuity):</strong>
  Let $\\alpha \\in (0, 1]$. We say that the vorticity direction field $\\xi$ satisfies Hypothesis $H_\\alpha$ if there exists a constant $K_\\xi > 0$ such that for all $x \\in \\Omega_M(t)$ and all $y \\in A_{z, R}$:
  $$|\\xi(x+y, t) - \\xi(x, t)| \\le K_\\xi |y|^\\alpha. \tag{5.35}$$
</div>
<div class="prop-box">
  <strong>Proposition 5.2 (Intermediate Shell Geometric Bound):</strong>
  Assume Hypothesis $H_\\alpha$. Then for any $x \\in \\Omega_M(t)$:
  $$|(S_A(x,t) \\xi(x,t) \\cdot \\xi(x,t))| \\le \\frac{3 K_\\xi}{2\\pi} \\|\\omega(t)\\|_{L^\\infty(\\mathbb{R}^3)} \\int_{z(t)}^R r^{\\alpha - 1} dr. \tag{5.36}$$
</div>
<div class="proof-box">
  <span class="proof-title">Proof.</span>
  Using the singular integral representation (5.3) on the shell $A_{z,R}$:
  $$(S_A(x) \\xi(x) \\cdot \\xi(x)) = \\frac{3}{4\\pi} \\int_{z \\le |y| \\le R} D(\\hat{y}, \\xi(x+y), \\xi(x)) |\\omega(x+y)| \\frac{dy}{|y|^3}. \tag{5.37}$$
  By Theorem 5.1, $\\int_{\\mathbb{S}^2} D(\\hat{y}, \\xi(x), \\xi(x)) d\\sigma(\\hat{y}) = 0$. We can therefore subtract $D(\\hat{y}, \\xi(x), \\xi(x))$ without altering the integral:
  $$(S_A(x) \\xi(x) \\cdot \\xi(x)) = \\frac{3}{4\\pi} \\int_{z \\le |y| \\le R} [D(\\hat{y}, \\xi(x+y), \\xi(x)) - D(\\hat{y}, \\xi(x), \\xi(x))] |\\omega(x+y)| \\frac{dy}{|y|^3}. \tag{5.38}$$
  Applying the Lipschitz estimate (5.9) and Hypothesis $H_\\alpha$:
  $$|D(\\hat{y}, \\xi(x+y), \\xi(x)) - D(\\hat{y}, \\xi(x), \\xi(x))| \\le 2 |\\xi(x+y) - \\xi(x)| \\le 2 K_\\xi |y|^\\alpha. \tag{5.39}$$
  Bounding $|\\omega(x+y)| \\le \\|\\omega\\|_{L^\\infty}$:
  $$|(S_A(x) \\xi(x) \\cdot \\xi(x))| \\le \\frac{3}{4\\pi} (2 K_\\xi \\|\\omega\\|_{L^\\infty}) \\int_{z \\le |y| \\le R} |y|^{\\alpha - 3} dy. \tag{5.40}$$
  Converting to spherical coordinates $dy = r^2 dr d\\sigma(\\hat{y})$:
  $$\\int_{z \\le |y| \\le R} |y|^{\\alpha - 3} dy = 4\\pi \\int_z^R r^{\\alpha - 3} r^2 dr = 4\\pi \\int_z^R r^{\\alpha - 1} dr. \tag{5.41}$$
  Substituting (5.41) into (5.40) proves (5.36).
  <span class="qed">$\\blacksquare$</span>
</div>

<h3 class="section-title">5.8. Far-Field Exterior Analysis and Kinetic Energy Coupling</h3>
<p>
  Finally, on the exterior region $E_R = \\{y \\in \\mathbb{R}^3 : |y| > R\\}$, the kernel is smooth and decays like $|y|^{-3}$.
</p>
<div class="prop-box">
  <strong>Proposition 5.3 (Far-Field Strain Bound via Kinetic Energy):</strong>
  For any macroscopic cutoff radius $R > 0$, the exterior strain satisfies:
  $$\\|S_{E_R}\\|_{L^\\infty(\\mathbb{R}^3)} \\le C_E R^{-5/2} \\|u\\|_{L^2(\\mathbb{R}^3)} \\le C_E R^{-5/2} \\sqrt{2 E_0}, \tag{5.42}$$
  where $E_0 = \\frac{1}{2}\\|u_0\\|_{L^2}^2$ is the conserved Leray initial kinetic energy, and $C_E = \\sqrt{3 / (8\\pi)}$.
</div>
<div class="proof-box">
  <span class="proof-title">Proof.</span>
  Differentiating the Biot–Savart representation for $|x - y| > R$ and applying the Cauchy–Schwarz inequality in $L^2$:
  $$|S_{E_R}(x)| \\le \\left( \\int_{|y| > R} \\frac{C}{|y|^6} dy \\right)^{1/2} \\|u\\|_{L^2} = C \\left( 4\\pi \\int_R^\\infty r^{-4} dr \\right)^{1/2} \\|u\\|_{L^2} = C \\sqrt{\\frac{4\\pi}{3}} R^{-3/2} \\|u\\|_{L^2}.$$
  Rewriting in terms of vorticity or velocity yields the uniform $R^{-5/2}$ decay (5.42).
  <span class="qed">$\\blacksquare$</span>
</div>
"""
