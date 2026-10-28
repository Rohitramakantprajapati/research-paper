# Chapter 1: Introduction, Historical Context, Physical Foundations, and Research Program

def generate_chapter_01():
    return r"""
<!-- CHAPTER 1 -->
<div class="page-break"></div>
<h1 class="chapter-num">CHAPTER 1</h1>
<h2 class="chapter-title">The 3D Navier–Stokes Millennium Problem: Physical Foundations and Historical Overview</h2>

<h3 class="section-title">1.1. Continuum Mechanics, Conservation Laws, and Incompressibility</h3>
<p>
  The mathematical description of macroscopic fluid motion rests on the continuum hypothesis, which posits that fluids can be modeled as continuous distributions of matter rather than discrete molecular ensembles. Consider an arbitrary bounded control volume $\\Omega \\subset \\mathbb{R}^3$ with smooth boundary $\\partial \\Omega$ immersed within a flowing fluid. Let $\\rho(x,t)$ denote the fluid density and $u(x,t) = (u_1(x,t), u_2(x,t), u_3(x,t))^T \\in \\mathbb{R}^3$ denote the Eulerian velocity vector field at spatial coordinate $x = (x_1, x_2, x_3) \\in \\mathbb{R}^3$ and time $t \\in [0, \\infty)$.
</p>
<p>
  The principle of mass conservation mandates that the rate of change of mass enclosed within $\\Omega$ must balance the net convective mass flux traversing the bounding surface $\\partial \\Omega$:
</p>
<div class="equation">
  $$\\frac{d}{dt} \\int_\\Omega \\rho(x,t)\\,dx = -\\int_{\\partial \\Omega} \\rho(x,t) (u(x,t) \\cdot n(x))\\,dS(x), \tag{1.1}$$
</div>
<p>
  where $n(x)$ represents the outward unit normal vector to $\\partial \\Omega$. Applying the Gauss divergence theorem converts the surface flux into a volume integral:
</p>
<div class="equation">
  $$\\int_\\Omega \\left[ \\partial_t \\rho + \\nabla \\cdot (\\rho u) \\right] dx = 0. \tag{1.2}$$
</div>
<p>
  Since the control volume $\\Omega$ is arbitrary, localized mass conservation yields the classical continuity equation $\\partial_t \\rho + \\nabla \\cdot (\\rho u) = 0$. For a homogeneous, incompressible fluid, the density field is strictly constant in space and time ($\rho \\equiv \\rho_0 > 0$). Consequently, the mass conservation law reduces to the foundational kinematic incompressibility constraint:
</p>
<div class="equation">
  $$\\operatorname{div} u = \\nabla \\cdot u = \\sum_{j=1}^3 \\partial_j u_j = 0. \tag{1.3}$$
</div>
<p>
  Newton's second law applied to the control volume dictates that the rate of change of linear momentum equals the sum of surface stresses and external body forces:
</p>
<div class="equation">
  $$\\frac{d}{dt} \\int_\\Omega \\rho_0 u_i\\,dx + \\int_{\\partial \\Omega} \\rho_0 u_i (u \\cdot n)\\,dS = \\int_{\\partial \\Omega} \\sigma_{ij} n_j\\,dS + \\int_\\Omega f_i\\,dx, \tag{1.4}$$
</div>
<p>
  where $\\sigma = (\\sigma_{ij})_{1 \\le i,j \\le 3}$ is the symmetric Cauchy stress tensor, and $f = (f_1, f_2, f_3)^T$ represents external volume forces. By the divergence theorem, the localized Cauchy momentum equation reads:
</p>
<div class="equation">
  $$\\rho_0 \\left( \\partial_t u_i + u_j \\partial_j u_i \\right) = \\partial_j \\sigma_{ij} + f_i. \tag{1.5}$$
</div>
<p>
  For a Newtonian fluid, the Cauchy stress tensor is assumed to depend linearly on the symmetric rate-of-strain tensor $S_{ij} = \\frac{1}{2}(\\partial_j u_i + \\partial_i u_j)$. Invoking Stokesian constitutive postulates (isotropy, frame indifference, and zero bulk viscosity under incompressibility), the stress tensor takes the form:
</p>
<div class="equation">
  $$\\sigma_{ij} = -P\\,\\delta_{ij} + 2\\mu S_{ij} = -P\\,\\delta_{ij} + \\mu (\\partial_j u_i + \\partial_i u_j), \tag{1.6}$$
</div>
<p>
  where $P(x,t)$ is thermodynamic pressure, $\\delta_{ij}$ is the Kronecker delta, and $\\mu > 0$ is dynamic viscosity. Substituting (1.6) into (1.5) and setting external body forces to zero ($f \\equiv 0$), we obtain:
</p>
<div class="equation">
  $$\\rho_0 \\left( \\partial_t u_i + u_j \\partial_j u_i \\right) = -\\partial_i P + \\mu \\partial_j (\\partial_j u_i + \\partial_i u_j) = -\\partial_i P + \\mu \\Delta u_i + \\mu \\partial_i (\\nabla \\cdot u). \tag{1.7}$$
</div>
<p>
  Invoking the incompressibility condition $\\nabla \\cdot u = 0$, dividing by $\\rho_0$, and introducing the kinematic viscosity $\\nu := \\mu / \\rho_0 > 0$ and the kinematic pressure $p := P / \\rho_0$, we arrive at the classical Navier–Stokes system:
</p>
<div class="equation">
  $$\\begin{cases}
  \\partial_t u + (u \\cdot \\nabla) u + \\nabla p = \\nu \\Delta u, & x \\in \\mathbb{R}^3, \\; t > 0, \\\
  \\nabla \\cdot u = 0, & x \\in \\mathbb{R}^3, \\; t > 0, \\\
  u(x, 0) = u_0(x), & x \\in \\mathbb{R}^3.
  \\end{cases} \tag{1.8}$$
</div>

<h3 class="section-title">1.2. The Clay Mathematics Institute Official Millennium Formulation</h3>
<p>
  In the year 2000, the Clay Mathematics Institute (CMI) designated the mathematical existence and smoothness of solutions to the 3D incompressible Navier–Stokes equations as one of the seven Millennium Prize Problems, accompanied by the definitive problem formulation authored by Charles L. Fefferman.
</p>
<div class="def-box">
  <strong>Definition 1.1 (Smooth Initial Data Class $\\mathcal{S}(\\mathbb{R}^3)$):</strong>
  A vector field $u_0 = (u_{0,1}, u_{0,2}, u_{0,3}) \\in C^\\infty(\\mathbb{R}^3)$ belongs to the admissible initial data class if it is divergence-free ($\nabla \\cdot u_0 = 0$) and satisfies rapid decay at spatial infinity in all derivatives:
  $$\\sup_{x \\in \\mathbb{R}^3} (1 + |x|)^K |\\partial^\\beta u_0(x)| < \\infty \\quad \\text{for all } K \\in \\mathbb{N} \\text{ and multi-indices } \\beta = (\\beta_1, \\beta_2, \\beta_3) \\in \\mathbb{N}_0^3. \tag{1.9}$$
</div>
<p>
  The official challenge comprises two complementary, mutually exclusive conjectures regarding the global behavior of the Cauchy problem (1.8):
</p>
<div class="theorem-box">
  <strong>Millennium Problem Statement (Fefferman, 2000):</strong>
  Prove or disprove one of the following two assertions:
  <ol style="margin-left: 15pt; margin-top: 6pt;">
    <li><strong>Assertion A (Global Regularity in $\\mathbb{R}^3$):</strong> For every initial datum $u_0 \\in \\mathcal{S}(\\mathbb{R}^3)$ with $\\nabla \\cdot u_0 = 0$, there exist smooth functions $u \\in C^\\infty(\\mathbb{R}^3 \\times [0, \\infty); \\mathbb{R}^3)$ and $p \\in C^\\infty(\\mathbb{R}^3 \\times [0, \\infty); \\mathbb{R})$ satisfying (1.8) on $\\mathbb{R}^3 \\times [0, \\infty)$ such that the total kinetic energy remains globally bounded:
    $$\\sup_{t \\ge 0} \\int_{\\mathbb{R}^3} |u(x,t)|^2 dx < \\infty. \tag{1.10}$$</li>
    <li><strong>Assertion B (Finite-Time Breakdown in $\\mathbb{R}^3$):</strong> There exists an initial datum $u_0 \\in \\mathcal{S}(\\mathbb{R}^3)$ with $\\nabla \\cdot u_0 = 0$ such that no smooth solution $(u, p) \\in C^\\infty(\\mathbb{R}^3 \\times [0, \\infty))$ exists satisfying (1.8). That is, there exists a finite blow-up time $T^* < \\infty$ such that:
    $$\\limsup_{t \\to T^{*-}} \\|u(\\cdot, t)\\|_{L^\\infty(\\mathbb{R}^3)} = \\infty \\quad \\text{or} \\quad \\limsup_{t \\to T^{*-}} \\|\\nabla u(\\cdot, t)\\|_{L^\\infty(\\mathbb{R}^3)} = \\infty. \tag{1.11}$$</li>
  </ol>
</div>

<h3 class="section-title">1.3. The Pioneering Foundation of Jean Leray (1934) and Weak Solutions</h3>
<p>
  The foundational mathematical theory for (1.8) was inaugurated in Jean Leray's seminal 1934 memoir <em>"Sur le mouvement d'un liquide visqueux emplissant l'espace"</em> published in <em>Acta Mathematica</em>. Prior to Leray, partial differential equations were studied almost exclusively via classical solutions, where all derivatives appearing in the differential operator must exist point-wise and remain continuous.
</p>
<p>
  Leray realized that physical fluid motion possesses a fundamental conservation law that remains valid even if point-wise derivatives fail: the <strong>energy inequality</strong>. Taking the $L^2(\\mathbb{R}^3)$ inner product of (1.8) with $u(x,t)$, integrating over $\\mathbb{R}^3$, and integrating by parts:
</p>
<div class="equation">
  $$\\int_{\\mathbb{R}^3} u \\cdot \\partial_t u\\,dx + \\int_{\\mathbb{R}^3} u \\cdot (u \\cdot \\nabla)u\\,dx + \\int_{\\mathbb{R}^3} u \\cdot \\nabla p\\,dx = \\nu \\int_{\\mathbb{R}^3} u \\cdot \\Delta u\\,dx. \tag{1.12}$$
</div>
<p>
  The nonlinear convective term vanishes identically due to the incompressibility condition:
</p>
<div class="equation">
  $$\\int_{\\mathbb{R}^3} u \\cdot (u \\cdot \\nabla) u\\,dx = \\sum_{i,j=1}^3 \\int_{\\mathbb{R}^3} u_i u_j \\partial_j u_i\\,dx = \\frac{1}{2} \\sum_{j=1}^3 \\int_{\\mathbb{R}^3} u_j \\partial_j (|u|^2)\\,dx = -\\frac{1}{2} \\int_{\\mathbb{R}^3} (\\nabla \\cdot u) |u|^2\\,dx = 0. \tag{1.13}$$
</div>
<p>
  Similarly, the pressure term decouples completely because $\\nabla \\cdot u = 0$:
</p>
<div class="equation">
  $$\\int_{\\mathbb{R}^3} u \\cdot \\nabla p\\,dx = -\\int_{\\mathbb{R}^3} (\\nabla \\cdot u) p\\,dx = 0. \tag{1.14}$$
</div>
<p>
  Integrating the viscous term by parts yields $\\int_{\\mathbb{R}^3} u \\cdot \\Delta u\\,dx = -\\int_{\\mathbb{R}^3} |\\nabla u|^2 dx$. We thus obtain the fundamental energy identity:
</p>
<div class="equation">
  $$\\frac{1}{2} \\frac{d}{dt} \\|u(t)\\|_{L^2(\\mathbb{R}^3)}^2 + \\nu \\|\\nabla u(t)\\|_{L^2(\\mathbb{R}^3)}^2 = 0. \tag{1.15}$$
</div>
<p>
  Integrating (1.15) over the time interval $[0, t]$ gives the classical Leray energy inequality:
</p>
<div class="equation">
  $$\\frac{1}{2} \\|u(t)\\|_{L^2(\\mathbb{R}^3)}^2 + \\nu \\int_0^t \\|\\nabla u(s)\\|_{L^2(\\mathbb{R}^3)}^2 ds \\le \\frac{1}{2} \\|u_0\\|_{L^2(\\mathbb{R}^3)}^2 =: E_0 \\quad \\text{for all } t \\ge 0. \tag{1.16}$$
</div>
<p>
  Leray introduced mollification techniques to construct global weak solutions $u \\in L^\\infty(0, \\infty; L^2(\\mathbb{R}^3)) \\cap L^2(0, \\infty; \\dot{H}^1(\\mathbb{R}^3))$ satisfying (1.8) in the sense of distributions and obeying (1.16). In 1951, Eberhard Hopf generalized Leray's construction to bounded domains $\\Omega \\subset \\mathbb{R}^d$, giving rise to the modern class of <strong>Leray–Hopf weak solutions</strong>.
</p>
<p>
  Crucially, Leray established that weak solutions are unique and smooth in two dimensions ($d=2$), but the uniqueness and smoothness of Leray–Hopf weak solutions in three dimensions ($d=3$) has remained unresolved for nearly a century.
</p>

<h3 class="section-title">1.4. The Classical Regularity Criteria: Serrin, Ladyzhenskaya, and Prodi</h3>
<p>
  Given the existence of global weak solutions, an intense line of research in the 1950s and 1960s sought criteria under which a Leray–Hopf weak solution is guaranteed to be smooth and unique. This culminated in the celebrated <strong>Ladyzhenskaya–Prodi–Serrin (LPS) condition</strong>:
</p>
<div class="theorem-box">
  <strong>Theorem 1.1 (Ladyzhenskaya–Prodi–Serrin Condition):</strong>
  Let $u$ be a Leray–Hopf weak solution to the 3D Navier–Stokes equations on $\\mathbb{R}^3 \\times [0, T)$. If $u$ satisfies the integrability condition:
  $$u \\in L^p(0, T; L^q(\\mathbb{R}^3)) \\quad \\text{with} \\quad \\frac{2}{p} + \\frac{3}{q} = 1, \\quad 3 < q \\le \\infty, \tag{1.17}$$
  then $u$ is smooth ($u \\in C^\\infty(\\mathbb{R}^3 \\times (0, T])$) and unique on $[0, T)$.
</div>
<p>
  The scaling relation $\\frac{2}{p} + \\frac{3}{q} = 1$ is scale-invariant under the natural parabolic dilation:
</p>
<div class="equation">
  $$u_\\lambda(x,t) = \\lambda u(\\lambda x, \\lambda^2 t), \quad \\|u_\\lambda\\|_{L^p(0, \\lambda^{-2} T; L^q(\\mathbb{R}^3))} = \\lambda^{1 - \\frac{2}{p} - \\frac{3}{q}} \\|u\\|_{L^p(0, T; L^q(\\mathbb{R}^3))}. \tag{1.18}$$
</div>
<p>
  When $\\frac{2}{p} + \\frac{3}{q} = 1$, the exponent of $\\lambda$ is exactly zero, meaning the norm $\\|u\\|_{L^p_t L^q_x}$ is dimensionless. The endpoint case $q = 3$ corresponds to $p = \\infty$, requiring $u \\in L^\\infty(0, T; L^3(\\mathbb{R}^3))$. This endpoint resisted resolution for four decades until the landmark 2003 paper by Luis Escauriaza, Gregory Seregin, and Vladim&iacute;r &Scaron;ver&aacute;k, who proved that if $\\sup_{t \\in [0, T)} \\|u(t)\\|_{L^3(\\mathbb{R}^3)} < \\infty$, then no singularity can develop at $T$.
</p>

<h3 class="section-title">1.5. The Beale–Kato–Majda Blow-Up Criterion (1984) and Vorticity Primacy</h3>
<p>
  While the LPS criteria formulate regularity in terms of velocity $u$, the fundamental physical mechanism driving potential singularity formation is the accumulation of rotation: <strong>vorticity</strong> $\\omega := \\operatorname{curl} u = \\nabla \\times u$. In 1984, J. Thomas Beale, Tosio Kato, and Andrew J. Majda proved a milestone theorem establishing that vorticity controls all higher Sobolev norms:
</p>
<div class="theorem-box">
  <strong>Theorem 1.2 (Beale–Kato–Majda (BKM) Criterion, 1984):</strong>
  Let $u_0 \\in H^s(\\mathbb{R}^3)$ for $s \\ge 3$ with $\\nabla \\cdot u_0 = 0$. Let $T^* > 0$ be a hypothetical maximal existence time of a classical solution $u \\in C([0, T^*); H^s(\\mathbb{R}^3))$. Then $T^* < \\infty$ if and only if:
  $$\\int_0^{T^*} \\|\\omega(\\cdot, t)\\|_{L^\\infty(\\mathbb{R}^3)}\\,dt = \\infty. \tag{1.19}$$
  Equivalently, if $\\int_0^{T^*} \\|\\omega(\\cdot, t)\\|_{L^\\infty} dt < \\infty$, then $u$ can be smoothly extended beyond $T^*$.
</div>
<p>
  The BKM criterion is remarkable because it requires control over only the $L^\\infty$ norm of vorticity, rather than the velocity gradient $\\nabla u$. This shifts the entire analytical focus to the dynamics of the vorticity equation:
</p>
<div class="equation">
  $$\\partial_t \\omega + (u \\cdot \\nabla) \\omega = (\\omega \\cdot \\nabla) u + \\nu \\Delta \\omega = S\\omega + \\nu \\Delta \\omega, \tag{1.20}$$
</div>
<p>
  where $S = \\frac{1}{2}(\\nabla u + \\nabla u^T)$ is the deformation strain tensor.
</p>

<h3 class="section-title">1.6. Critical Scaling, Energy Supercriticality, and the Dimensional Gap</h3>
<p>
  The principal obstacle preventing an unconditional resolution of the 3D Navier–Stokes existence problem is the <strong>energy-supercriticality</strong> of the equations. Under the scale transformation:
</p>
<div class="equation">
  $$u_\\lambda(x,t) := \\lambda u(\\lambda x, \\lambda^2 t), \\quad p_\\lambda(x,t) := \\lambda^2 p(\\lambda x, \\lambda^2 t), \tag{1.21}$$
</div>
<p>
  the system (1.8) is invariant: $(u_\\lambda, p_\\lambda)$ satisfies (1.8) on $\\mathbb{R}^3 \\times [0, \\lambda^{-2} T)$ if and only if $(u, p)$ does.
</p>
<p>
  Now consider the scaling behavior of the $L^2$ kinetic energy:
</p>
<div class="equation">
  $$\\|u_\\lambda(\\cdot, t)\\|_{L^2(\\mathbb{R}^3)}^2 = \\int_{\\mathbb{R}^3} |\\lambda u(\\lambda x, \\lambda^2 t)|^2 dx = \\lambda^2 \\int_{\\mathbb{R}^3} |u(y, \\lambda^2 t)|^2 \\lambda^{-3} dy = \\lambda^{-1} \\|u(\\cdot, \\lambda^2 t)\\|_{L^2(\\mathbb{R}^3)}^2. \tag{1.22}$$
</div>
<p>
  As $\\lambda \\to \\infty$ (focusing into smaller spatial scales where singularities might nucleate), $\\lambda^{-1} \\to 0$. The physical energy bound $\\|u_\\lambda\\|_{L^2} \\le \\lambda^{-1/2} E_0^{1/2}$ actually weakens to zero as scale shrinks, offering zero coercive control against localized concentration!
</p>
<p>
  In contrast, the scale-invariant Sobolev space for 3D Navier–Stokes is $\\dot{H}^{1/2}(\\mathbb{R}^3)$, since:
</p>
<div class="equation">
  $$\\|u_\\lambda\\|_{\\dot{H}^{1/2}(\\mathbb{R}^3)} = \\lambda^{1/2 + 1 - 3/2} \\|u\\|_{\\dot{H}^{1/2}} = \\|u\\|_{\\dot{H}^{1/2}}. \tag{1.23}$$
</div>
<p>
  There is a gap of one-half spatial derivative between the conserved physical energy ($L^2 = \\dot{H}^0$) and the critical regularity space ($\\dot{H}^{1/2}$). This half-derivative discrepancy is the mathematical manifestation of the energy cascade in 3D turbulence.
</p>

<table class="academic-table">
  <caption class="table-caption">Table 1.1: Historical Progression of Regularity Criteria for 3D Incompressible Navier–Stokes</caption>
  <thead>
    <tr>
      <th>Author(s) & Year</th>
      <th>Regularity Condition</th>
      <th>Scaling Nature</th>
      <th>Primary Mechanism</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Jean Leray (1934)</td>
      <td>$\\|u\\|_{L^\\infty_t L^2_x} + \\nu^{1/2} \\|\\nabla u\\|_{L^2_t L^2_x} \\le E_0^{1/2}$</td>
      <td>Supercritical ($L^2$)</td>
      <td>Kinetic energy dissipation</td>
    </tr>
    <tr>
      <td>Prodi (1959), Serrin (1962)</td>
      <td>$u \\in L^p_t L^q_x$ with $\\frac{2}{p} + \\frac{3}{q} = 1, \\; q > 3$</td>
      <td>Critical ($L^p_t L^q_x$)</td>
      <td>Convective absorption</td>
    </tr>
    <tr>
      <td>Ladyzhenskaya (1967)</td>
      <td>Uniqueness of LPS solutions</td>
      <td>Critical</td>
      <td>Energy method for difference</td>
    </tr>
    <tr>
      <td>Beale–Kato–Majda (1984)</td>
      <td>$\\int_0^T \\|\\omega(t)\\|_{L^\\infty} dt < \\infty$</td>
      <td>Critical ($L^1_t L^\\infty_x$)</td>
      <td>Vorticity-strain singular kernel</td>
    </tr>
    <tr>
      <td>Constantin–Fefferman (1993)</td>
      <td>$|\\xi(x+y) - \\xi(x)| \\le K |y|^\\alpha, \\; \\alpha \\ge 1/2$</td>
      <td>Geometric critical</td>
      <td>Anti-symmetric kernel depletion</td>
    </tr>
    <tr>
      <td>Escauriaza–Seregin–Šverák (2003)</td>
      <td>$u \\in L^\\infty(0, T; L^3(\\mathbb{R}^3))$</td>
      <td>Endpoint Critical ($L^3$)</td>
      <td>Backward Carleman inequalities</td>
    </tr>
  </tbody>
</table>

<h3 class="section-title">1.7. Coherent Vortex Structures and the Geometric Perspective</h3>
<p>
  Direct numerical simulations of fully developed 3D turbulent flows consistently reveal that intense vorticity does not concentrate in isotropic spherical droplets; rather, it organizes into highly anisotropic, quasi-one-dimensional <strong>vortex filaments</strong> ("worms") and quasi-two-dimensional <strong>vortex sheets</strong>.
</p>
<p>
  This geometric structure motivated Peter Constantin and Charles Fefferman in 1993 to introduce the directional decomposition of vorticity:
</p>
<div class="equation">
  $$\\xi(x,t) := \\frac{\\omega(x,t)}{|\\omega(x,t)|} \\in \\mathbb{S}^2 = \\{v \\in \\mathbb{R}^3 : |v| = 1\\}, \tag{1.24}$$
</div>
<p>
  defined wherever $|\\omega(x,t)| > 0$. They discovered that the nonlinear vortex stretching term $(S\\omega \\cdot \\omega) = |\\omega|^2 (S\\xi \\cdot \\xi)$ exhibits an exact geometric cancellation: if the direction field $\\xi$ is spatially uniform (i.e., parallel vortex lines), vortex stretching vanishes identically: $(S\\xi \\cdot \\xi) \\equiv 0$.
</p>
<p>
  Consequently, finite-time singularity formation requires not merely high vorticity amplitude, but rapid, violent <strong>directional twisting</strong> of the vortex lines.
</p>

<h3 class="section-title">1.8. Detailed Dissertation Layout, Scope, and Epistemic Commitments</h3>
<p>
  This doctoral dissertation presents a rigorous mathematical framework synthesizing geometric vorticity dynamics, Littlewood–Paley critical scaling, Osgood dynamical systems, and formal machine verification in Lean 4.
</p>
<div class="theorem-box alert-box">
  <strong>Strict Epistemic Commitments:</strong>
  In adherence to the highest standards of mathematical integrity:
  <ol style="margin-left: 15pt; margin-top: 6pt;">
    <li>All conditional hypotheses are explicitly demarcated as definitions and theorem assumptions.</li>
    <li>We distinguish sharply between subcritical regimes ($\\alpha > 1/2$), where global regularity holds unconditionally in data magnitude, and the critical regime ($\\alpha = 1/2$), where logarithmic losses leave large-data regularity strictly open.</li>
    <li>We provide a rigorous circularity analysis in Chapter 9 demonstrating why deriving Hypothesis $H_\\alpha$ dynamically from smooth initial data remains fundamentally open.</li>
    <li>We do not claim an unconditional resolution of the Clay Millennium Prize Problem.</li>
  </ol>
</div>
"""
