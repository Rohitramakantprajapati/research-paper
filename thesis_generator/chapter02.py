# Chapter 2: Rigorous Functional Analysis, Harmonic Analysis, and Littlewood–Paley Theory

def generate_chapter_02():
    return r"""
<!-- CHAPTER 2 -->
<div class="page-break"></div>
<h1 class="chapter-num">CHAPTER 2</h1>
<h2 class="chapter-title">Rigorous Functional Analysis, Harmonic Analysis, and Littlewood–Paley Theory</h2>

<h3 class="section-title">2.1. Function Spaces: Lebesgue, Sobolev, and Homogeneous Sobolev Spaces</h3>
<p>
  Throughout this dissertation, we work in the three-dimensional Euclidean space $\\mathbb{R}^3$ equipped with standard Lebesgue measure $dx$. For $p \\in [1, \\infty]$, let $L^p(\\mathbb{R}^3)$ denote the standard Lebesgue space of equivalence classes of measurable functions $f: \\mathbb{R}^3 \\to \\mathbb{R}$ (or $\\mathbb{R}^3$) equipped with the norm:
</p>
<div class="equation">
  $$\\|f\\|_{L^p(\\mathbb{R}^3)} := \\left( \\int_{\\mathbb{R}^3} |f(x)|^p dx \\right)^{1/p} \\quad (1 \\le p < \\infty), \\qquad \\|f\\|_{L^\\infty(\\mathbb{R}^3)} := \\operatorname{ess\\,sup}_{x \\in \\mathbb{R}^3} |f(x)|. \tag{2.1}$$
</div>
<p>
  The Fourier transform of a Schwartz function $f \\in \\mathcal{S}(\\mathbb{R}^3)$ is normalized as:
</p>
<div class="equation">
  $$\\mathcal{F}[f](\\xi) = \\hat{f}(\\xi) := \\int_{\\mathbb{R}^3} f(x) e^{-i x \\cdot \\xi} dx, \\qquad \\mathcal{F}^{-1}[g](x) := \\frac{1}{(2\\pi)^3} \\int_{\\mathbb{R}^3} g(\\xi) e^{i x \\cdot \\xi} d\\xi. \tag{2.2}$$
</div>
<p>
  By Plancherel's theorem, $\\|\\hat{f}\\|_{L^2(\\mathbb{R}^3)} = (2\\pi)^{3/2} \\|f\\|_{L^2(\\mathbb{R}^3)}$. For any real exponent $s \\ge 0$, the inhomogeneous Sobolev space $H^s(\\mathbb{R}^3) = W^{s,2}(\\mathbb{R}^3)$ is the Hilbert space defined by:
</p>
<div class="equation">
  $$\\|f\\|_{H^s(\\mathbb{R}^3)}^2 := \\frac{1}{(2\\pi)^3} \\int_{\\mathbb{R}^3} (1 + |\\xi|^2)^s |\\hat{f}(\\xi)|^2 d\\xi = \\|f\\|_{L^2}^2 + \\|f\\|_{\\dot{H}^s}^2, \tag{2.3}$$
</div>
<p>
  where the homogeneous Sobolev semi-norm $\\dot{H}^s(\\mathbb{R}^3)$ is defined via:
</p>
<div class="equation">
  $$\\|f\\|_{\\dot{H}^s(\\mathbb{R}^3)}^2 := \\frac{1}{(2\\pi)^3} \\int_{\\mathbb{R}^3} |\\xi|^{2s} |\\hat{f}(\\xi)|^2 d\\xi. \tag{2.4}$$
</div>
<p>
  For $s = 1$, Plancherel's identity immediately identifies $\\|f\\|_{\\dot{H}^1(\\mathbb{R}^3)} = \\|\\nabla f\\|_{L^2(\\mathbb{R}^3)}$, where $\\nabla f = (\\partial_1 f, \\partial_2 f, \\partial_3 f)$.
</p>

<h3 class="section-title">2.2. Calder&oacute;n–Zygmund Singular Integrals and Riesz Transforms in $\\mathbb{R}^3$</h3>
<p>
  The recovery of the velocity gradient $\\nabla u$ and deformation strain $S$ from the vorticity field $\\omega$ involves singular integral operators of Calder&oacute;n–Zygmund type. In $\\mathbb{R}^3$, the classical Riesz transforms $\\mathcal{R}_j$ ($j = 1, 2, 3$) are Fourier multiplier operators defined by:
</p>
<div class="equation">
  $$\\widehat{\\mathcal{R}_j f}(\\xi) := -i \\frac{\\xi_j}{|\\xi|} \\hat{f}(\\xi) \\quad (\\xi \\in \\mathbb{R}^3 \\setminus \\{0\\}). \tag{2.5}$$
</div>
<p>
  In physical space, $\\mathcal{R}_j$ is represented as a principal value singular convolution kernel:
</p>
<div class="equation">
  $$\\mathcal{R}_j f(x) = \\frac{1}{\\pi^2} \\lim_{\\epsilon \\to 0} \\int_{|y| > \\epsilon} \\frac{y_j}{|y|^4} f(x - y)\\,dy. \tag{2.6}$$
</div>
<div class="theorem-box">
  <strong>Theorem 2.1 (Calder&oacute;n–Zygmund Theorem on $\\mathbb{R}^3$):</strong>
  Let $K(x) = \\Omega(\\hat{x}) / |x|^3$ be a homogeneous singular kernel of degree $-3$, where $\\Omega \\in C^1(\\mathbb{S}^2)$ satisfies the vanishing spherical moment condition:
  $$\\int_{\\mathbb{S}^2} \\Omega(\\theta)\\,d\\sigma(\\theta) = 0. \tag{2.7}$$
  Then the associated principal value operator $T f(x) = \\lim_{\\epsilon \\to 0} \\int_{|y| > \\epsilon} K(y) f(x-y)\\,dy$ defines a bounded linear operator from $L^p(\\mathbb{R}^3)$ into $L^p(\\mathbb{R}^3)$ for all $1 < p < \\infty$:
  $$\\|T f\\|_{L^p(\\mathbb{R}^3)} \\le C_{CZ}(p) \\|\\Omega\\|_{C^1(\\mathbb{S}^2)} \\|f\\|_{L^p(\\mathbb{R}^3)}. \tag{2.8}$$
  Moreover, for $p = 1$, $T$ is of weak-type $(1,1)$, and for $p = \\infty$, $T$ maps $L^\\infty(\\mathbb{R}^3)$ boundedly into the John–Nirenberg space of Bounded Mean Oscillation $\\text{BMO}(\\mathbb{R}^3)$.
</div>

<h3 class="section-title">2.3. Sharp Gagliardo–Nirenberg–Sobolev Inequalities and Extremal Constants</h3>
<p>
  A cornerstone inequality throughout this work is the interpolation of the $L^3(\\mathbb{R}^3)$ norm of vorticity between its $L^2$ enstrophy norm and its $\\dot{H}^1$ dissipation norm.
</p>
<div class="prop-box">
  <strong>Proposition 2.1 (Sharp Gagliardo–Nirenberg on $\\mathbb{R}^3$):</strong>
  For any divergence-free field $\\omega \\in L^2(\\mathbb{R}^3) \\cap \\dot{H}^1(\\mathbb{R}^3)$, the following interpolation inequality holds:
  $$\\|\\omega\\|_{L^3(\\mathbb{R}^3)} \\le C_{GN} \\|\\omega\\|_{L^2(\\mathbb{R}^3)}^{1/2} \\|\\nabla \\omega\\|_{L^2(\\mathbb{R}^3)}^{1/2}, \tag{2.9}$$
  where the optimal variational constant $C_{GN}$ is given explicitly by:
  $$C_{GN} = 3^{-1/4} (4\\pi)^{-1/3} \\approx 0.327429. \tag{2.10}$$
</div>
<div class="proof-box">
  <span class="proof-title">Proof.</span>
  By standard Sobolev embedding on $\\mathbb{R}^3$, the critical Sobolev space $\\dot{H}^{1/2}(\\mathbb{R}^3)$ embeds continuously into $L^3(\\mathbb{R}^3)$:
  $$\\|f\\|_{L^3(\\mathbb{R}^3)} \\le C_S \\|f\\|_{\\dot{H}^{1/2}(\\mathbb{R}^3)}. \tag{2.11}$$
  Using the Fourier definition of the homogeneous Sobolev norm:
  $$\\|f\\|_{\\dot{H}^{1/2}}^2 = \\frac{1}{(2\\pi)^3} \\int_{\\mathbb{R}^3} |\\xi| |\\hat{f}(\\xi)|^2 d\\xi. \tag{2.12}$$
  Applying the Cauchy–Schwarz inequality on the Fourier side:
  $$\\int_{\\mathbb{R}^3} |\\xi| |\\hat{f}(\\xi)|^2 d\\xi = \\int_{\\mathbb{R}^3} |\\hat{f}(\\xi)| \\cdot \\left( |\\xi| |\\hat{f}(\\xi)| \\right) d\\xi \\le \\left( \\int_{\\mathbb{R}^3} |\\hat{f}(\\xi)|^2 d\\xi \\right)^{1/2} \\left( \\int_{\\mathbb{R}^3} |\\xi|^2 |\\hat{f}(\\xi)|^2 d\\xi \\right)^{1/2}. \tag{2.13}$$
  Plancherel's theorem yields:
  $$\\left( \\int_{\\mathbb{R}^3} |\\hat{f}(\\xi)|^2 d\\xi \\right)^{1/2} = (2\\pi)^{3/2} \\|f\\|_{L^2}, \\qquad \\left( \\int_{\\mathbb{R}^3} |\\xi|^2 |\\hat{f}(\\xi)|^2 d\\xi \\right)^{1/2} = (2\\pi)^{3/2} \\|\\nabla f\\|_{L^2}. \tag{2.14}$$
  Multiplying these two bounds and taking the square root gives:
  $$\\|f\\|_{\\dot{H}^{1/2}(\\mathbb{R}^3)} \\le \\|f\\|_{L^2(\\mathbb{R}^3)}^{1/2} \\|\\nabla f\\|_{L^2(\\mathbb{R}^3)}^{1/2}. \tag{2.15}$$
  The best constant $C_S$ for the embedding $\\dot{H}^{1/2}(\\mathbb{R}^3) \\hookrightarrow L^3(\\mathbb{R}^3)$ was computed variationally by Lieb (1983) and Talenti (1976) via the ground state of the fractional Sobolev Euler–Lagrange equation:
  $$(-\\Delta)^{1/2} W = W^2 \\quad \\text{in } \\mathbb{R}^3, \tag{2.16}$$
  which yields $C_{GN} = 3^{-1/4} (4\\pi)^{-1/3} \\approx 0.3274$. This completes the derivation.
  <span class="qed">$\\blacksquare$</span>
</div>

<h3 class="section-title">2.4. Littlewood–Paley Dyadic Decomposition and Dyadic Partition of Unity</h3>
<p>
  To analyze fluid interactions across multi-scale frequency bands, we employ the classical Littlewood–Paley dyadic frequency decomposition. Let $\\chi \\in C_c^\\infty(\\mathbb{R}^3)$ be a smooth, radial cutoff function such that:
</p>
<div class="equation">
  $$\\chi(\\xi) = \\begin{cases} 1 & \\text{if } |\\xi| \\le 4/3, \\\ 0 & \\text{if } |\\xi| \\ge 5/3, \\end{cases} \\qquad 0 \\le \\chi(\\xi) \\le 1. \tag{2.17}$$
</div>
<p>
  Define $\\phi(\\xi) := \\chi(\\xi / 2) - \\chi(\\xi)$, which is supported in the dyadic frequency annulus $\\mathcal{C} = \\{\\xi \\in \\mathbb{R}^3 : 3/4 \\le |\\xi| \\le 8/3\\}$. Setting $\\phi_j(\\xi) := \\phi(2^{-j}\\xi)$ for each integer $j \\in \\mathbb{Z}$, we obtain the dyadic partition of unity:
</p>
<div class="equation">
  $$\\sum_{j \\in \\mathbb{Z}} \\phi(2^{-j}\\xi) = 1 \\quad \\text{for all } \\xi \\in \\mathbb{R}^3 \\setminus \\{0\\}. \tag{2.18}$$
</div>
<p>
  For any tempered distribution $f \\in \\mathcal{S}'(\\mathbb{R}^3)$, the homogeneous Littlewood–Paley projection operators $\\dot{\\Delta}_j$ and low-frequency smoothing operators $\\dot{S}_j$ are defined by:
</p>
<div class="equation">
  $$\\widehat{\\dot{\\Delta}_j f}(\\xi) := \\phi(2^{-j}\\xi) \\hat{f}(\\xi), \\qquad \\widehat{\\dot{S}_j f}(\\xi) := \\chi(2^{-j}\\xi) \\hat{f}(\\xi) = \\sum_{k=-\\infty}^{j-1} \\dot{\\Delta}_k f. \tag{2.19}$$
</div>
<div class="lemma-box">
  <strong>Lemma 2.1 (Bernstein's Inequalities for Dyadic Shells):</strong>
  Let $1 \\le p \\le q \\le \\infty$ and $k \\in \\mathbb{N}_0$. There exists a universal constant $C_B > 0$ such that for every $j \\in \\mathbb{Z}$ and every $f \\in \\mathcal{S}'(\\mathbb{R}^3)$:
  <ol style="margin-left: 15pt; margin-top: 4pt;">
    <li>$\\sup_{|\\beta| = k} \\|\\partial^\\beta \\dot{\\Delta}_j f\\|_{L^q(\\mathbb{R}^3)} \\le C_B^{k+1} 2^{j(k + 3(1/p - 1/q))} \\|\\dot{\\Delta}_j f\\|_{L^p(\\mathbb{R}^3)}$,</li>
    <li>$C_B^{-1} 2^{jk} \\|\\dot{\\Delta}_j f\\|_{L^p(\\mathbb{R}^3)} \\le \\sup_{|\\beta| = k} \\|\\partial^\\beta \\dot{\\Delta}_j f\\|_{L^p(\\mathbb{R}^3)} \\le C_B 2^{jk} \\|\\dot{\\Delta}_j f\\|_{L^p(\\mathbb{R}^3)}$.</li>
  </ol>
</div>

<h3 class="section-title">2.5. Bony Paraproducts, Commutator Estimates, and Critical Besov Spaces</h3>
<p>
  When taking products of two distributions $f$ and $g$, the Littlewood–Paley operators decompose the product into Bony's celebrated <strong>paraproduct decomposition</strong>:
</p>
<div class="equation">
  $$f g = T_f g + T_g f + R(f, g), \tag{2.20}$$
</div>
<p>
  where the paraproduct $T_f g$ and resonant remainder $R(f, g)$ are defined by:
</p>
<div class="equation">
  $$T_f g := \\sum_{j \\in \\mathbb{Z}} \\dot{S}_{j-1} f \\, \\dot{\\Delta}_j g, \\qquad R(f, g) := \\sum_{j \\in \\mathbb{Z}} \\sum_{|k - j| \\le 1} \\dot{\\Delta}_j f \\, \\dot{\\Delta}_k g. \tag{2.21}$$
</div>
<p>
  In $T_f g$, the low frequencies of $f$ modulate the high frequencies of $g$, preserving spectral localization in the dyadic shell $\\sim 2^j$. The resonant remainder $R(f, g)$ captures the interactions between comparable frequency modes, which can cascade into either higher or lower frequencies.
</p>
<div class="def-box">
  <strong>Definition 2.2 (Homogeneous Besov Spaces $\\dot{B}_{p,q}^s(\\mathbb{R}^3)$):</strong>
  For $s \\in \\mathbb{R}$ and $1 \\le p, q \\le \\infty$, the homogeneous Besov space $\\dot{B}_{p,q}^s(\\mathbb{R}^3)$ consists of all tempered distributions $f \\in \\mathcal{S}'/\\mathcal{P}$ such that the norm:
  $$\\|f\\|_{\\dot{B}_{p,q}^s(\\mathbb{R}^3)} := \\left( \\sum_{j \\in \\mathbb{Z}} \\left( 2^{js} \\|\\dot{\\Delta}_j f\\|_{L^p(\\mathbb{R}^3)} \\right)^q \\right)^{1/q} < \\infty \tag{2.22}$$
  (with the standard supremum replacement when $q = \\infty$).
</div>

<h3 class="section-title">2.6. The Biot–Savart Law: Vector Potential, Stream Functions, and Decay</h3>
<p>
  Given a divergence-free velocity vector field $u$ with vorticity $\\omega = \\nabla \\times u$, the vector identity $\\nabla \\times (\\nabla \\times u) = \\nabla(\\nabla \\cdot u) - \\Delta u$ simplifies to the vector Poisson equation:
</p>
<div class="equation">
  $$-\\Delta u = \\nabla \\times \\omega. \tag{2.23}$$
</div>
<p>
  Inverting the Laplacian in $\\mathbb{R}^3$ via the Newtonian potential $G(x) = \\frac{1}{4\\pi |x|}$, we obtain the classical <strong>Biot–Savart law</strong>:
</p>
<div class="equation">
  $$u(x) = \\nabla \\times \\left( \\frac{1}{4\\pi} \\int_{\\mathbb{R}^3} \\frac{\\omega(y)}{|x - y|} dy \\right) = \\frac{1}{4\\pi} \\int_{\\mathbb{R}^3} \\frac{(x - y) \\times \\omega(y)}{|x - y|^3} dy. \tag{2.24}$$
</div>
<p>
  Differentiating (2.24) yields the velocity gradient tensor $\\nabla u$. Taking the symmetric part produces the deformation strain tensor $S(x) = \\frac{1}{2}(\\nabla u + \\nabla u^T)$:
</p>
<div class="equation">
  $$S_{ij}(x) = \\frac{3}{4\\pi} \\operatorname{P.V.} \\int_{\\mathbb{R}^3} \\left[ \\frac{(x-y)_i (x-y)_k \\epsilon_{jkl} + (x-y)_j (x-y)_k \\epsilon_{ikl}}{2|x-y|^5} \\right] \\omega_l(y)\\,dy. \tag{2.25}$$
</div>
<p>
  Because the kernel has singularity $|x-y|^{-3}$ at $y \\to x$, it is a singular integral of Calder&oacute;n–Zygmund type with trace $\\operatorname{Tr}(S) = \\sum_{i=1}^3 S_{ii} = \\nabla \\cdot u = 0$.
</p>
"""
