# Chapter 3: Vorticity Formulation, Boundary Behavior, and Enstrophy Dynamics

def generate_chapter_03():
    return r"""
<!-- CHAPTER 3 -->
<div class="page-break"></div>
<h1 class="chapter-num">CHAPTER 3</h1>
<h2 class="chapter-title">Vorticity Formulation, Boundary Vanishing, and Enstrophy Dynamics</h2>

<h3 class="section-title">3.1. Complete Vector Calculus Derivation of the Vorticity Equation</h3>
<p>
  To isolate the physical rotation of fluid elements from the pressure field, we apply the curl operator $\\nabla \\times$ to the momentum equation of the 3D Navier–Stokes system:
</p>
<div class="equation">
  $$\\nabla \\times \\left( \\partial_t u + (u \\cdot \\nabla) u + \\nabla p - \\nu \\Delta u \\right) = 0. \tag{3.1}$$
</div>
<p>
  We evaluate each term individually using classical vector identities:
</p>
<ol style="margin-left: 15pt; line-height: 1.7;">
  <li><strong>Time derivative:</strong> Because spatial and temporal derivatives commute on $C^2$ fields:
  $$\\nabla \\times (\\partial_t u) = \\partial_t (\\nabla \\times u) = \\partial_t \\omega. \tag{3.2}$$</li>
  <li><strong>Pressure gradient:</strong> The curl of any conservative gradient field vanishes identically:
  $$\\nabla \\times (\\nabla p) = 0. \tag{3.3}$$</li>
  <li><strong>Viscous Laplacian:</strong> Since $\\Delta = \\nabla \\cdot \\nabla$ commutes with the curl:
  $$\\nabla \\times (\\nu \\Delta u) = \\nu \\Delta (\\nabla \\times u) = \\nu \\Delta \\omega. \tag{3.4}$$</li>
  <li><strong>Nonlinear convective term:</strong> We invoke the standard vector calculus identity for the curl of a convective product:
  $$\\nabla \\times ((u \\cdot \\nabla) u) = (u \\cdot \\nabla)(\\nabla \\times u) - ((\\nabla \\times u) \\cdot \\nabla) u + (\\nabla \\cdot u)(\\nabla \\times u) - (\\nabla \\cdot (\\nabla \\times u)) u. \tag{3.5}$$
  Substituting $\\omega = \\nabla \\times u$, and applying the incompressibility condition $\\nabla \\cdot u = 0$ along with the vector identity $\\nabla \\cdot (\\nabla \\times u) \\equiv 0$:
  $$\\nabla \\times ((u \\cdot \\nabla) u) = (u \\cdot \\nabla)\\omega - (\\omega \\cdot \\nabla) u. \tag{3.6}$$</li>
</ol>
<p>
  Assembling these four results into (3.1) yields the classical 3D vorticity equation:
</p>
<div class="equation">
  $$\\partial_t \\omega + (u \\cdot \\nabla) \\omega = (\\omega \\cdot \\nabla) u + \\nu \\Delta \\omega. \tag{3.7}$$
</div>

<h3 class="section-title">3.2. The Deformation Strain Tensor $S$ and Vortex Stretching Mechanics</h3>
<p>
  The velocity gradient tensor $\\nabla u = (\\partial_j u_i)_{1 \\le i,j \\le 3}$ can be uniquely decomposed into its symmetric and anti-symmetric parts:
</p>
<div class="equation">
  $$\\nabla u = S + \\Omega_{anti}, \tag{3.8}$$
</div>
<p>
  where $S$ is the symmetric rate-of-strain tensor and $\\Omega_{anti}$ is the skew-symmetric rotation tensor:
</p>
<div class="equation">
  $$S_{ij} := \\frac{1}{2}(\\partial_j u_i + \\partial_i u_j), \\qquad (\\Omega_{anti})_{ij} := \\frac{1}{2}(\\partial_j u_i - \\partial_i u_j) = -\\frac{1}{2} \\sum_{k=1}^3 \\epsilon_{ijk} \\omega_k. \tag{3.9}$$
</div>
<p>
  When acting on the vorticity vector $\\omega$, the anti-symmetric tensor satisfies:
</p>
<div class="equation">
  $$(\\Omega_{anti} \\omega)_i = \\sum_{j=1}^3 (\\Omega_{anti})_{ij} \\omega_j = -\\frac{1}{2} \\sum_{j,k=1}^3 \\epsilon_{ijk} \\omega_k \\omega_j = \\frac{1}{2} (\\omega \\times \\omega)_i = 0. \tag{3.10}$$
</div>
<p>
  Consequently, the term $(\\omega \\cdot \\nabla) u = (\\nabla u) \\omega$ reduces purely to the action of the symmetric deformation strain tensor $S$:
</p>
<div class="equation">
  $$(\\omega \\cdot \\nabla) u = S \\omega. \tag{3.11}$$
</div>
<p>
  The vorticity equation (3.7) can thus be rewritten in its canonical form:
</p>
<div class="equation">
  $$\\partial_t \\omega + (u \\cdot \\nabla) \\omega = S \\omega + \\nu \\Delta \\omega. \tag{3.12}$$
</div>
<p>
  The term $S\\omega$ is called the <strong>vortex stretching term</strong>. If an eigenvalue of $S$ aligned with $\\omega$ is positive (tensile strain), the vortex line is stretched, its cross-sectional area shrinks to conserve angular momentum, and the vorticity magnitude $|\omega|$ amplifies dramatically. In two dimensions ($d=2$), $\\omega = (0, 0, \\omega_3)$ is perpendicular to the plane of motion, forcing $(\\omega \\cdot \\nabla) u = \\omega_3 \\partial_3 u = 0$. Hence, vortex stretching is an exclusively three-dimensional phenomenon.
</p>

<h3 class="section-title">3.3. Full Mathematical Proof of the Beale–Kato–Majda Theorem</h3>
<p>
  We present the complete, self-contained proof of the Beale–Kato–Majda blow-up criterion (Theorem 1.2), which forms the bedrock of modern blow-up analysis.
</p>
<div class="lemma-box">
  <strong>Lemma 3.1 (Logarithmic Sobolev Inequality):</strong>
  Let $s > 5/2$. There exists a universal constant $C_{BKM} > 0$ depending only on $s$ such that for any divergence-free field $u \\in H^s(\\mathbb{R}^3)$ with $\\omega = \\nabla \\times u$:
  $$\\|\\nabla u\\|_{L^\\infty(\\mathbb{R}^3)} \\le C_{BKM} \\left( 1 + \\|\\omega\\|_{L^2(\\mathbb{R}^3)} + \\|\\omega\\|_{L^\\infty(\\mathbb{R}^3)} \\ln\\left( e + \\|\\omega\\|_{H^{s-1}(\\mathbb{R}^3)} \\right) \\right). \tag{3.13}$$
</div>
<div class="proof-box">
  <span class="proof-title">Proof of Lemma 3.1.</span>
  By the Littlewood–Paley dyadic decomposition, we partition $\\nabla u$ into three frequency regimes relative to a dyadic cutoff $N \\in \\mathbb{N}$:
  $$\\nabla u = \\dot{S}_0(\\nabla u) + \\sum_{j=0}^{N-1} \\dot{\\Delta}_j(\\nabla u) + \\sum_{j=N}^\\infty \\dot{\\Delta}_j(\\nabla u). \tag{3.14}$$
  <ol style="margin-left: 15pt;">
    <li><strong>Low frequencies ($j < 0$):</strong> By Bernstein's inequality and $L^2$ embedding:
    $$\\|\\dot{S}_0(\\nabla u)\\|_{L^\\infty} \\le C \\|\\dot{S}_0(\\nabla u)\\|_{L^2} \\le C \\|\\omega\\|_{L^2}. \tag{3.15}$$</li>
    <li><strong>Intermediate frequencies ($0 \\le j < N$):</strong> The operator relating $\\nabla u$ to $\\omega$ is a combination of Calder&oacute;n–Zygmund Riesz transforms $\\mathcal{R}_k \\mathcal{R}_l$. On localized dyadic shells, the Riesz transforms are bounded on $L^\\infty$:
    $$\\|\\dot{\\Delta}_j(\\nabla u)\\|_{L^\\infty} \\le C \\|\\dot{\\Delta}_j \\omega\\|_{L^\\infty} \\le C \\|\\omega\\|_{L^\\infty}. \tag{3.16}$$
    Summing over $j = 0, \\dots, N-1$:
    $$\\sum_{j=0}^{N-1} \\|\\dot{\\Delta}_j(\\nabla u)\\|_{L^\\infty} \\le C N \\|\\omega\\|_{L^\\infty}. \tag{3.17}$$</li>
    <li><strong>High frequencies ($j \\ge N$):</strong> By Bernstein's inequality with $s > 5/2$ (letting $\\delta = s - 5/2 > 0$):
    $$\\|\\dot{\\Delta}_j(\\nabla u)\\|_{L^\\infty} \\le C 2^{j \\cdot 3/2} \\|\\dot{\\Delta}_j(\\nabla u)\\|_{L^2} \\le C 2^{-j \\delta} \\left( 2^{j(s-1)} \\|\\dot{\\Delta}_j \\omega\\|_{L^2} \\right) \\le C 2^{-j \\delta} \\|\\omega\\|_{H^{s-1}}. \tag{3.18}$$
    Summing the geometric series for $j \\ge N$:
    $$\\sum_{j=N}^\\infty \\|\\dot{\\Delta}_j(\\nabla u)\\|_{L^\\infty} \\le C 2^{-N \\delta} \\|\\omega\\|_{H^{s-1}}. \tag{3.19}$$</li>
  </ol>
  Combining (3.15), (3.17), and (3.19):
  $$\\|\\nabla u\\|_{L^\\infty} \\le C \\left( \\|\\omega\\|_{L^2} + N \\|\\omega\\|_{L^\\infty} + 2^{-N \\delta} \\|\\omega\\|_{H^{s-1}} \\right). \tag{3.20}$$
  Choosing $N = \\lceil \\delta^{-1} \\log_2(e + \\|\\omega\\|_{H^{s-1}}) \\rceil$ balances the intermediate and high-frequency terms, yielding (3.13).
  <span class="qed">$\\blacksquare$</span>
</div>
<div class="proof-box">
  <span class="proof-title">Proof of Theorem 1.2 (BKM Continuation).</span>
  Applying $D^s$ to (3.7), taking the $L^2$ inner product with $D^s \\omega$, and applying the Kato–Ponce commutator estimate:
  $$\\frac{1}{2} \\frac{d}{dt} \\|\\omega\\|_{H^s}^2 + \\nu \\|\\nabla \\omega\\|_{H^s}^2 \\le C \\|\\nabla u\\|_{L^\\infty} \\|\\omega\\|_{H^s}^2. \tag{3.21}$$
  Substituting the logarithmic bound (3.13) into (3.21) yields:
  $$\\frac{d}{dt} \\ln(e + \\|\\omega(t)\\|_{H^s}) \\le C \\|\\omega(t)\\|_{L^\\infty} \\ln(e + \\|\\omega(t)\\|_{H^s}). \tag{3.22}$$
  By Gr&ouml;nwall's inequality:
  $$\\ln(e + \\|\\omega(t)\\|_{H^s}) \\le \\ln(e + \\|\\omega(0)\\|_{H^s}) \\exp\\left( C \\int_0^t \\|\\omega(\\tau)\\|_{L^\\infty} d\\tau \\right). \tag{3.23}$$
  If $\\int_0^{T^*} \\|\\omega(t)\\|_{L^\\infty} dt < \\infty$, then $\\sup_{t \\in [0, T^*)} \\|\\omega(t)\\|_{H^s} < \\infty$, preventing blow-up at $T^*$.
  <span class="qed">$\\blacksquare$</span>
</div>

<h3 class="section-title">3.4. Rigorous Derivation of the Fundamental Enstrophy Identity</h3>
<div class="prop-box">
  <strong>Proposition 3.1 (Fundamental Enstrophy Identity):</strong>
  Let $u \\in C([0, T^*); H^3(\\mathbb{R}^3))$ be a classical solution to (1.8). Define the total fluid enstrophy by:
  $$Q(t) := \\|\\omega(\\cdot, t)\\|_{L^2(\\mathbb{R}^3)}^2 = \\int_{\\mathbb{R}^3} |\\omega(x,t)|^2 dx. \tag{3.24}$$
  Then on $[0, T^*)$, $Q(t)$ satisfies the exact differential identity:
  $$\\frac{1}{2} \\frac{d}{dt} Q(t) + \\nu \\|\\nabla \\omega(t)\\|_{L^2(\\mathbb{R}^3)}^2 = \\int_{\\mathbb{R}^3} (S(x,t)\\omega(x,t) \\cdot \\omega(x,t))\\,dx. \tag{3.25}$$
</div>
<div class="proof-box">
  <span class="proof-title">Proof.</span>
  Take the $L^2(\\mathbb{R}^3)$ inner product of (3.12) with $\\omega(x,t)$:
  $$\\int_{\\mathbb{R}^3} \\partial_t \\omega \\cdot \\omega\\,dx + \\int_{\\mathbb{R}^3} ((u \\cdot \\nabla) \\omega) \\cdot \\omega\\,dx = \\int_{\\mathbb{R}^3} (S\\omega) \\cdot \\omega\\,dx + \\nu \\int_{\\mathbb{R}^3} (\\Delta \\omega) \\cdot \\omega\\,dx. \tag{3.26}$$
  <ol style="margin-left: 15pt;">
    <li>The temporal derivative gives $\\int_{\\mathbb{R}^3} \\partial_t \\omega \\cdot \\omega\\,dx = \\frac{1}{2} \\frac{d}{dt} \\int_{\\mathbb{R}^3} |\\omega|^2 dx = \\frac{1}{2} \\frac{d}{dt} Q(t)$.</li>
    <li>For the convective term, using summation convention:
    $$\\int_{\\mathbb{R}^3} u_j (\\partial_j \\omega_i) \\omega_i\\,dx = \\frac{1}{2} \\int_{\\mathbb{R}^3} u_j \\partial_j (|\\omega|^2)\\,dx = -\\frac{1}{2} \\int_{\\mathbb{R}^3} (\\partial_j u_j) |\\omega|^2\\,dx = 0,$$
    since $\\nabla \\cdot u = 0$.</li>
    <li>For the viscous term, integrating by parts:
    $$\\nu \\int_{\\mathbb{R}^3} (\\Delta \\omega) \\cdot \\omega\\,dx = -\\nu \\sum_{i,j=1}^3 \\int_{\\mathbb{R}^3} (\\partial_j \\omega_i)^2 dx = -\\nu \\|\\nabla \\omega\\|_{L^2(\\mathbb{R}^3)}^2.$$
    </li>
  </ol>
  Substituting these evaluations back into (3.26) yields (3.25).
  <span class="qed">$\\blacksquare$</span>
</div>

<h3 class="section-title">3.5. Boundary Vanishing at Spatial Infinity and Integration by Parts</h3>
<p>
  Because $\\mathbb{R}^3$ is unbounded, the integration by parts in Proposition 3.1 requires justification. Let $\\psi \\in C_c^\\infty(\\mathbb{R}^3)$ be a standard smooth cut-off function such that $\\psi(x) = 1$ for $|x| \\le 1$, $\\psi(x) = 0$ for $|x| \\ge 2$, and $|\\nabla \\psi(x)| \\le 2$. For each $R > 0$, define $\\psi_R(x) := \\psi(x/R)$.
</p>
<p>
  Integrating against the localized weight $\\psi_R$:
</p>
<div class="equation">
  $$\\int_{\\mathbb{R}^3} (\\Delta \\omega \\cdot \\omega) \\psi_R\\,dx = -\\int_{\\mathbb{R}^3} |\\nabla \\omega|^2 \\psi_R\\,dx - \\int_{\\mathbb{R}^3} (\\nabla \\omega : (\\omega \\otimes \\nabla \\psi_R))\\,dx. \tag{3.27}$$
</div>
<p>
  The boundary commutator term is estimated using the Cauchy–Schwarz inequality:
</p>
<div class="equation">
  $$\\left| \\int_{\\mathbb{R}^3} (\\nabla \\omega : (\\omega \\otimes \\nabla \\psi_R))\\,dx \\right| \\le \\|\\nabla \\omega\\|_{L^2(R \\le |x| \\le 2R)} \\|\\omega\\|_{L^2(R \\le |x| \\le 2R)} \\frac{2}{R}. \tag{3.28}$$
</div>
<p>
  Since $\\omega \\in L^2(\\mathbb{R}^3)$ and $\\nabla \\omega \\in L^2(\\mathbb{R}^3)$, the $L^2$ norms on the annulus $[R, 2R]$ tend to zero as $R \\to \\infty$, while $R^{-1} \\to 0$. By Lebesgue's Dominated Convergence Theorem, taking $R \\to \\infty$ eliminates the boundary term identically, justifying (3.25) unconditionally.
</p>

<h3 class="section-title">3.6. The Supercritical Enstrophy Barrier: Classical Riccati Blow-Up</h3>
<p>
  We now expose why standard functional analytic methods fail to establish global regularity for 3D Navier–Stokes. Consider estimating the vortex stretching integral $\\int_{\\mathbb{R}^3} (S\\omega \\cdot \\omega) dx$ using H&ouml;lder's inequality:
</p>
<div class="equation">
  $$\\left| \\int_{\\mathbb{R}^3} (S\\omega \\cdot \\omega) dx \\right| \\le \\|S\\|_{L^3(\\mathbb{R}^3)} \\|\\omega\\|_{L^3(\\mathbb{R}^3)}^2. \tag{3.29}$$
</div>
<p>
  By the Calder&oacute;n–Zygmund theorem (Theorem 2.1), the deformation strain tensor $S$ is bounded in $L^3$: $\\|S\\|_{L^3} \\le C_{CZ} \\|\\omega\\|_{L^3}$. Substituting this into (3.29):
</p>
<div class="equation">
  $$\\left| \\int_{\\mathbb{R}^3} (S\\omega \\cdot \\omega) dx \\right| \\le C_{CZ} \\|\\omega\\|_{L^3(\\mathbb{R}^3)}^3. \tag{3.30}$$
</div>
<p>
  Now apply the sharp Gagliardo–Nirenberg inequality (Proposition 2.1):
</p>
<div class="equation">
  $$\\|\\omega\\|_{L^3}^3 \\le C_{GN}^3 \\|\\omega\\|_{L^2}^{3/2} \\|\\nabla \\omega\\|_{L^2}^{3/2} = C_{GN}^3 Q(t)^{3/4} \\|\\nabla \\omega\\|_{L^2}^{3/2}. \tag{3.31}$$
</div>
<p>
  Substitute (3.31) into the enstrophy identity (3.25):
</p>
<div class="equation">
  $$\\frac{1}{2} \\frac{d}{dt} Q(t) + \\nu \\|\\nabla \\omega\\|_{L^2}^2 \\le C_0 Q(t)^{3/4} \\|\\nabla \\omega\\|_{L^2}^{3/2}, \\qquad C_0 = C_{CZ} C_{GN}^3. \tag{3.32}$$
</div>
<p>
  To absorb $\\|\\nabla \\omega\\|_{L^2}^{3/2}$ into the viscous dissipation $\\nu \\|\\nabla \\omega\\|_{L^2}^2$, we apply Young's inequality with conjugate exponents $p = 4/3$ and $q = 4$:
</p>
<div class="equation">
  $$a b \\le \\frac{3}{4} a^{4/3} + \\frac{1}{4} b^4, \\qquad a = (\\nu)^{3/4} \\|\\nabla \\omega\\|_{L^2}^{3/2}, \\quad b = \\frac{C_0}{\\nu^{3/4}} Q(t)^{3/4}. \tag{3.33}$$
</div>
<p>
  This yields:
</p>
<div class="equation">
  $$C_0 Q(t)^{3/4} \\|\\nabla \\omega\\|_{L^2}^{3/2} \\le \\frac{3}{4} \\nu \\|\\nabla \\omega\\|_{L^2}^2 + \\frac{C_0^4}{4 \\nu^3} Q(t)^3. \tag{3.34}$$
</div>
<p>
  Inserting (3.34) into (3.32) and subtracting $\\frac{3}{4}\\nu \\|\\nabla \\omega\\|_{L^2}^2$ from both sides:
</p>
<div class="equation">
  $$\\frac{1}{2} \\frac{d}{dt} Q(t) + \\frac{\\nu}{4} \\|\\nabla \\omega\\|_{L^2}^2 \\le \\frac{C_0^4}{4 \\nu^3} Q(t)^3. \tag{3.35}$$
</div>
<p>
  Dropping the positive dissipation term $\\frac{\\nu}{4} \\|\\nabla \\omega\\|_{L^2}^2 \\ge 0$, we arrive at the fatal <strong>cubic Riccati differential inequality</strong>:
</p>
<div class="equation">
  $$\\frac{d}{dt} Q(t) \\le \\frac{C_0^4}{2 \\nu^3} Q(t)^3. \tag{3.36}$$
</div>
<p>
  Separating variables and integrating (3.36):
</p>
<div class="equation">
  $$\\int_{Q_0}^{Q(t)} \\frac{dQ}{Q^3} \\le \\frac{C_0^4}{2 \\nu^3} t \\implies -\\frac{1}{2}\\left( \\frac{1}{Q(t)^2} - \\frac{1}{Q_0^2} \\right) \\le \\frac{C_0^4}{2 \\nu^3} t, \tag{3.37}$$
</div>
<p>
  which yields the explicit upper bound:
</p>
<div class="equation">
  $$Q(t) \\le \\frac{Q_0}{\\sqrt{1 - \\frac{C_0^4 Q_0^2}{\\nu^3} t}}. \tag{3.38}$$
</div>
<p>
  As $t \\to T_{blow} := \\frac{\\nu^3}{C_0^4 Q_0^2}$, the denominator vanishes and $Q(t) \\to +\\infty$.
</p>
<p>
  <strong>The Supercritical Barrier:</strong> Because the power of enstrophy is cubic ($Q^3$), classical energy methods are fundamentally incapable of ruling out finite-time blow-up. To break through this cubic barrier, one must uncover deeper geometric mechanisms that suppress vortex stretching.
</p>
"""
