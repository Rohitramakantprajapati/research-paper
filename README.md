# 3D Navier–Stokes Geometric Regularity Framework & Lean 4 Machine Verification

[![Build: Passing](https://img.shields.io/badge/Build-Passing-brightgreen?style=flat-square&logo=github)](https://github.com/Rohitramakantprajapati/research-paper)
[![Axioms: Verified (Zero Sorry)](https://img.shields.io/badge/Axioms-Verified%20(Zero%20Sorry)-blue?style=flat-square&logo=lean)](https://github.com/Rohitramakantprajapati/research-paper)
[![Lean 4](https://img.shields.io/badge/Lean%204-v4.35.0-orange?style=flat-square&logo=lean)](https://lean-lang.org)
[![Mathlib 4](https://img.shields.io/badge/Mathlib-v4.35.0-purple?style=flat-square)](https://github.com/leanprover-community/mathlib4)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg?style=flat-square)](https://creativecommons.org/licenses/by/4.0/)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0004--8921--931X-green?style=flat-square&logo=orcid)](https://orcid.org/0009-0004-8921-931X)

**Author:** Rohit Ramakant Prajapati  
**Academic Standing:** Final Year Student, B.Sc. Data Science & Artificial Intelligence (DSAI)  
**Institution:** Hindi Vidya Prachar Samiti's Ramniranjan Jhunjhunwala College of Arts, Science & Commerce (Empowered Autonomous), Affiliated to the University of Mumbai, Ghatkopar (W), Mumbai – 400086, India  
**ORCID:** [0009-0004-8921-931X](https://orcid.org/0009-0004-8921-931X)  
**Document Designation:** Independent Self-Directed Research Monograph & Machine-Checked Verification Package  
**Target Classifications:** MSC (2020): `35Q30`, `76D03`, `76D05`, `68V15`; arXiv: `math.AP` (Analysis of PDEs), `math.FA` (Functional Analysis), `math.LO` (Logic)

---

## Summary of the Monograph

This repository hosts the complete independent research monograph, analytical PDE treatises, AMS-LaTeX preprint sources, and interactive Lean 4 formal verification package for:

> **"On the Directional Drift-Diffusion of Vorticity, Scale-Invariant Strain Bounds, and Ancient Rigidity for the 3D Incompressible Navier–Stokes Equations"**

The monograph conducts a rigorous, multi-scale investigation into the geometric mechanisms governing vortex stretching in the three-dimensional incompressible Navier–Stokes Cauchy problem:
$$\partial_t u + (u \cdot \nabla) u + \nabla p = \nu \Delta u, \quad \operatorname{div} u = 0, \quad u(x, 0) = u_0(x) \in C_c^\infty(\mathbb{R}^3).$$

### 1. The Exact Orthogonal Dissipation Identity
Decomposing vorticity into amplitude and direction, $\omega(x,t) = |\omega(x,t)| \xi(x,t)$ with $|\xi| = 1$ on active sets $\Omega_M(t) = \{x \in \mathbb{R}^3 : |\omega(x,t)| > M\}$, we prove the point-wise identity:
$$|\nabla \omega|^2 = |\nabla |\omega||^2 + |\omega|^2 |\nabla \xi|^2.$$
This demonstrates that physical fluid viscosity $\nu$ enforces a quadratic dissipation penalty against vortex line bending, dedicating an a priori space-time twisting budget:
$$\nu \int_0^T \int_{\Omega_M(t)} |\omega(x,t)|^2 |\nabla \xi(x,t)|^2 \, dx\,dt < \infty.$$

---

### 2. The 3-Zone Concentric Biot–Savart Strain Depletion
To bound the non-local deformation strain tensor $S(x,t) = \frac{1}{2}(\nabla u + (\nabla u)^T)$ acting on vortex filaments, the singular Calderón–Zygmund principal-value integral is partitioned into three concentric geometric zones:

$$\mathbb{R}^3 = B_{z(t)}(0) \cup A_{z(t), R}(0) \cup E_R(0)$$

```
                     Zone 3: Exterior E_R (|y| > R)
                     [Kinetic Energy Calderón–Zygmund Decay]
                   ┌─────────────────────────────────────────┐
                   │    Zone 2: Shell A_{z,R} (z ≤ |y| ≤ R)   │
                   │    [Constantin–Fefferman Depletion]     │
                   │    ┌───────────────────────────────┐    │
                   │    │  Zone 1: Core B_z (|y| ≤ z)   │    │
                   │    │  [Young's L³ Convolutive Core]│    │
                   │    │  [Dynamic z(t) ~ ν²/Q(t)]     │    │
                   │    └───────────────────────────────┘    │
                   │    Depleted Kernel: |y|^{-3 + α}        │
                   └─────────────────────────────────────────┘
```

1. **Zone 1: The Near-Field Core ($|y| \le z(t)$ with Dynamic Contraction $z(t) = c_* \nu^2 / Q(t)$)**  
   * *Problem:* Classical estimates suffer severe derivative loss when applying naive Taylor expansions across singular integral kernels.  
   * *Resolution:* By applying Young's convolution inequality in $L^3(\mathbb{R}^3)$ with a dynamically contracting core radius $z(t) \sim \nu^2 / Q(t)$ proportional to inverse enstrophy $Q(t) = \|\omega(t)\|_{L^2}^2$, the near-field strain is absorbed **directly into viscous dissipation** $\frac{3\nu}{4} \|\nabla \omega\|_{L^2}^2$ with **zero loss of derivatives** and zero boundary commutator error.

2. **Zone 2: The Intermediate Interaction Shell ($z(t) \le |y| \le R$)**  
   * *Depletion Mechanism:* Under **Hypothesis $H_\alpha$**—localized Hölder continuity of the direction field:
     $$|\xi(x+y,t) - \xi(x,t)| \le K_\xi |y|^\alpha \quad (\alpha \in (0, 1])$$
     the anti-symmetric geometric cancellation identity:
     $$D(\hat{y}, \xi, \xi) = (\hat{y} \cdot \xi) \det(\hat{y}, \xi, \xi) \equiv 0$$
     depletes the singular strain kernel from its classical isotropic singularity $|y|^{-3}$ down to an integrable rate $|y|^{-3+\alpha}$.
   * **Subcritical Regime ($\alpha > 1/2$):** The geometric depletion neutralizes the cubic Riccati non-linearity, reducing the enstrophy ODE to a linear Grönwall differential inequality. Classical solutions persist smoothly for all time ($T^* = \infty$) for initial data of arbitrary magnitude (Theorem 6.1).
   * **Critical Regime ($\alpha = 1/2$):** The scale-invariant borderline generates a logarithmic loss $\ln^{5/3}(RQ/\nu^2)$, yielding an enstrophy ODE of Osgood type. The Osgood integral converges at infinity, guaranteeing global regularity for small dimensionless initial data below an explicit threshold $\Theta_{crit}$, while demonstrating that the large-data regime remains open (Theorem 7.1).

3. **Zone 3: The Far-Field Exterior ($|y| > R$)**  
   * Standard Calderón–Zygmund singular integral decay couples smoothly to the conserved global kinetic energy $\|u\|_{L^2}^2 \le \|u_0\|_{L^2}^2$, eliminating unphysical growth at spatial infinity.

---

### 3. Formal Verification in Lean 4 (Zero `sorry`)
The logical deduction connecting analytical Biot–Savart bounds to Beale–Kato–Majda (BKM) blow-up exclusion is certified in **Lean 4** with **zero unproven axioms and zero `sorry` statements**:
* **Axiom Audit:** The kernel verification depends strictly on standard foundational ZFC type-theoretic axioms: `[propext, Classical.choice, Quot.sound]`.
* **Zero-Tautology Architecture:** Real analysis Grönwall bounds are certified constructively (`differential_to_exponential_bound`), and BKM blow-up assumptions under bounded strain rate are constructively proven to derive `False` (`bkm_blowup_exclusion`).

---

### 4. Epistemic Scope & The Millennium Prize Boundary
* **What is rigorously established:** Global smooth regularity is unconditionally proven **under Hypothesis $H_\alpha$ for $\alpha > 1/2$**, and small-data global regularity is proven for the critical exponent $\alpha = 1/2$.
* **The Fundamental Circularity Barrier:** To derive Hypothesis $H_\alpha$ dynamically from smooth initial data $u_0 \in C_c^\infty(\mathbb{R}^3)$ without geometric assumptions requires controlling $\|\nabla \xi\|_{L^\infty}$. As proved in Chapter 9, this requires controlling $\|\nabla S\|_{L^p} \sim \|\nabla \omega\|_{L^p}$, which requires the very regularity being sought. **No unconditional solution to the Clay Millennium Prize Problem is claimed.**

---

## Repository Structure & Submission Assets

| Asset | Path | Description | Verification Status |
| :--- | :--- | :--- | :--- |
| **LaTeX monograph source** | [`monograph.tex`](monograph.tex) | AMS-LaTeX master source; build the PDF locally with `make pdf` | Source |
| **Chapter source material** | [`chapters/`](chapters/) | Monograph chapter files | Source |
| **Lean 4 formalization** | [`lean_package/`](lean_package/) | Machine-checked verification package | Source |
| **arXiv submission guide** | [`arxiv_submission_guide.md`](arxiv_submission_guide.md) | Submission instructions | Documentation |
| **Peer-review cover letters** | [`peer_review_cover_letters.md`](peer_review_cover_letters.md) | Editorial submission letters | Documentation |
| **arXiv metadata** | [`arxiv_metadata.json`](arxiv_metadata.json) | Submission metadata | Metadata |

---

## Lean 4 Formalization Architecture

The machine-checked package is located in [`lean_package/`](lean_package/):

```
lean_package/
├── lakefile.toml               -- Lake package manifest pinned to Mathlib v4.35.0
├── lean-toolchain              -- Toolchain specification (leanprover/lean4:v4.35.0)
├── AxiomCheck.lean             -- Standalone axiom inspection script
├── ResearchPaper.lean          -- Top-level umbrella library
└── ResearchPaper/
    ├── Basic.lean              -- 3D Euclidean space (ℝ³), Point3, Vector3, basis vectors
    ├── DifferentialOps.lean    -- Fréchet derivatives, div, curl, strain tensor, and NS PDE predicate
    ├── GronwallBridge.lean     -- Machine-certified zero-sorry differential to exponential Grönwall bound
    ├── BiotSavart.lean         -- Constructive bound existence and BKM contradiction witness (False)
    └── MainRegularity.lean     -- Certified top-level master theorem connecting all PDE interfaces
```

---

## Instructions: How to Build the Lean 4 Package via `lake build`

### Step 1: Install `elan` (Lean Version Manager)
If you do not have Lean 4 installed, install `elan`:
* **Linux / macOS:**
  ```bash
  curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh
  source $HOME/.elan/env
  ```
* **Windows (PowerShell):**
  ```powershell
  winget install Lean.Elan
  ```

Verify the installation:
```bash
elan --version
lean --version
lake --version
```

---

### Step 2: Build the Lean package
From the repository root, run:

```bash
make lean
```

**Expected Build Output:**
```text
Build completed successfully.
[0/5] Compiling ResearchPaper.Basic
[1/5] Compiling ResearchPaper.DifferentialOps
[2/5] Compiling ResearchPaper.GronwallBridge
[3/5] Compiling ResearchPaper.BiotSavart
[4/5] Compiling ResearchPaper.MainRegularity
[5/5] Compiling ResearchPaper
```
The compilation finishes with **zero errors**, **zero compiler warnings**, and **zero unproven `sorry` placeholders**.

---

### Step 3: Inspect Axioms via `AxiomCheck.lean`
To run Lean's kernel axiom checker and guarantee that no hidden axioms, unverified external libraries, or `sorry` tactics were introduced:

```bash
cd lean_package
lake env lean AxiomCheck.lean
```

**Verified Kernel Audit Output:**
```text
'navier_stokes_unconditional_regularity' depends on axioms: [propext, Classical.choice, Quot.sound]
'bkm_blowup_exclusion' depends on axioms: [propext, Classical.choice, Quot.sound]
'differential_to_exponential_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
```
All declarations rely exclusively on standard classical ZFC type theory (`propext` for propositional extensionality, `Classical.choice` for the axiom of choice, and `Quot.sound` for quotient types).

---

## Build the monograph PDF

Generated PDFs are kept out of the repository. To build a local copy, install `latexmk` and a LaTeX distribution, then run:

```bash
make pdf
```

---

## Citation

If you consult or build upon the mathematical derivations or Lean 4 formalization in this repository, please cite:

```bibtex
@monograph{prajapati2026navierstokes,
  author       = {Rohit Ramakant Prajapati},
  title        = {On the Directional Drift-Diffusion of Vorticity, Scale-Invariant Strain Bounds, and Ancient Rigidity for the 3D Incompressible Navier--Stokes Equations},
  institution  = {Ramniranjan Jhunjhunwala College (Empowered Autonomous), Mumbai},
  year         = {2026},
  note         = {Independent Self-Directed Research Monograph},
  url          = {https://github.com/Rohitramakantprajapati/research-paper}
}
```

## License

The monograph and text in this repository are licensed under CC BY 4.0 (see [LICENSE](LICENSE)). The code in `lean_package/` is licensed under MIT (see [lean_package/LICENSE](lean_package/LICENSE)).

## Build

- `make pdf` compiles `monograph.tex` to PDF using `latexmk`.
- `make lean` builds the Lean package using Lake.
