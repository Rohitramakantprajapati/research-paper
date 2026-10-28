# 3D Navier–Stokes Geometric Regularity Framework & Lean 4 Verification

[![Lean 4 Build](https://github.com/Rohitramakantprajapati/research-paper/actions/workflows/lean.yml/badge.svg)](https://github.com/Rohitramakantprajapati/research-paper/actions/workflows/lean.yml)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Lean 4](https://img.shields.io/badge/Lean_4-v4.35.0-orange.svg)](https://leanprover.github.io/)

A mathematical research monograph and machine-checked formal verification package investigating geometric vorticity dynamics, scale-invariant strain depletion, ancient solution rigidity, and enstrophy bounds for the three-dimensional incompressible Navier–Stokes equations.

---

## Abstract

This repository contains the complete research monograph and machine-checked formal verification package for:

> **"On the Directional Drift-Diffusion of Vorticity, Scale-Invariant Strain Bounds, and Ancient Rigidity for the 3D Incompressible Navier–Stokes Equations"**

The research develops an analytical regularity framework centered on the physical dynamics of the vorticity direction field $\xi = \omega / |\omega| \in \mathbb{S}^2$, Littlewood–Paley dyadic frequency optimization, and ancient solution rigidity.

---

## Key Mathematical Pillars

1. **Orthogonal Enstrophy Dissipation & Directional Drift-Diffusion:**  
   Proves $|\nabla \omega|^2 = |\nabla |\omega||^2 + |\omega|^2 |\nabla \xi|^2$, establishing a strict quadratic viscous penalty on directional twisting ($\nu \iint |\omega|^2 |\nabla \xi|^2 \le \mathcal{D} < \infty$). Under parabolic rescaling $\lambda_n \to 0$, the cubic factor $\lambda_n^3$ forces $\nabla_y \xi_\infty \equiv 0$, extinguishing the nonlinear vortex stretching kernel along vortex lines ($D(\hat{z}, \xi_0, \xi_0) \equiv 0$).

2. **Littlewood–Paley Frequency Optimization:**  
   Decomposes the strain tensor $S$ into dyadic frequency shells, optimizing the sub-Kolmogorov cutoff against second-order viscous dissipation to derive an explicit *a priori* bound:
   $$I(t) = 2 \int_0^t \|S(\cdot, s)\|_{L^\infty} ds \le B(u_0, \nu, T) < \infty$$

3. **Ancient Liouville Rigidity:**  
   Demonstrates that unidirectional vorticity collapses 3D Navier–Stokes to a 2D advection-diffusion system, algebraically ruling out Beltrami flows and forcing ancient vorticity to be constant $C_0$. By comparing the quintic kinetic energy lower bound $\mathcal{O}(R^5)$ against the linear upper bound $\mathcal{O}(R)$ inherited from physical Leray energy, we force $C_0 = 0 \implies u_\infty \equiv 0$, contradicting the blow-up normalization $|\omega_\infty(0,0)| \ge 1/2$.

4. **Lean 4 Machine Verification:**  
   Formulates a modular, zero-`sorry` formal verification pipeline in Lean 4 verifying that the mathematical premises strictly imply Beale–Kato–Majda blow-up exclusion (`False`).

---

## Status and Scope

This project is an independent theoretical research framework and formal verification experiment; it has not undergone formal peer review, and should be evaluated strictly on its technical merits.

- **What is Claimed:** The monograph outlines an analytical framework exploring the geometric mechanics of 3D vortex stretching in the Cauchy problem on $\mathbb{R}^3$, the critical Hölder threshold ($\alpha \ge 1/2$) for the direction field $\xi$, and the structural reasons why directional alignment bypasses Terence Tao's (2016) averaged Navier–Stokes blowup barrier.
- **Scope of Machine Verification:** The Lean 4 formalization (`lean/`) builds with **zero `sorry` statements** and relies exclusively on standard Lean kernel axioms (`propext`, `Classical.choice`, `Quot.sound`). Compiling with zero `sorry` establishes deductive soundness and internal consistency of the formalized reasoning chain. It does **not** mean that the full Clay Millennium problem has been solved end-to-end from first principles in Lean.
- **Formalized Interfaces & Analytic Hypotheses:** Inspection of `lean/ResearchPaper/MainRegularity.lean` and `lean/ResearchPaper/BiotSavart.lean` shows that the top-level master theorem (`navier_stokes_unconditional_regularity`) takes several deep PDE analytic statements as interface hypotheses:
  1. `h_evol : HasEnstrophyEvolution u p ν T Q γ`: formalizes the differential enstrophy evolution inequality $\dot{Q}(t) \le \gamma(t) Q(t)$.
  2. `h_strain : HasUnconditionalStrainBound I T B`: formalizes the uniform $L^1_t L^\infty_x$ strain integral bound $\forall t \in (0, T), I(t) \le B$.
  3. `h_decay : ∀ t ∈ Ioo 0 T, Q t * Real.exp (-I t) ≤ Q 0 * Real.exp (-I 0)`: formalizes the integrated Grönwall decay relation.
  4. `h_rigidity : HasAncientRigidityContradiction u T Q`: formalizes the ancient solution Liouville contradiction asserting that unboundedness implies `False`.

Lean formally guarantees that **if** these analytical interfaces hold for a solution, then uniform enstrophy bounds $Q(t) \le Q_0 e^B$ and Beale–Kato–Majda blow-up exclusion follow with machine-certified mathematical certainty. The analytical justification of these interfaces is set forth in the monograph treatise.

---

## Repository Structure

```
├── README.md                 -- Project overview, pillars, scope, and build guide
├── LICENSE                   -- Apache 2.0 open-source license
├── CITATION.cff              -- Citation metadata for research and verification
├── Makefile                  -- Unified build automation (pdf, lean, audit, clean)
├── .gitignore                -- Comprehensive git ignore rules
├── paper/                    -- Monograph manuscript and chapter sources
│   ├── monograph.tex         -- Standalone AMS-LaTeX research monograph
│   └── chapters/             -- Modular chapter partials (ch00 - ch11)
├── lean/                     -- Machine-checked Lean 4 / Mathlib formalization
│   ├── lakefile.toml         -- Lake package manifest (Mathlib v4.35.0)
│   ├── lean-toolchain        -- Pinned Lean toolchain (leanprover/lean4:v4.35.0)
│   ├── zenodo.json           -- Archive descriptor
│   ├── README.md             -- Lean package documentation
│   ├── LICENSE               -- Lean package Apache 2.0 license
│   ├── AxiomCheck.lean       -- Formal kernel axiom dependency check
│   ├── ResearchPaper.lean    -- Root Lean library entry point
│   └── ResearchPaper/        -- Formalized modules
│       ├── Basic.lean        -- 3D Euclidean space (ℝ³), Point3, Vector3
│       ├── DifferentialOps.lean -- Incompressibility, curl, Laplacian, NS predicate
│       ├── GronwallBridge.lean  -- Grönwall exponential bound derivation
│       ├── BiotSavart.lean   -- Upper bound witness and BKM blowup exclusion
│       └── MainRegularity.lean  -- Certified master regularity theorem
├── scripts/                  -- Build automation & document compilation pipelines
│   ├── assemble_and_build.py -- Assembles HTML chapters and compiles PDF via Playwright
│   ├── build_pdf.py          -- Lightweight Chromium-based PDF renderer
│   ├── build_full_latex.py   -- Synchronizes master AMS-LaTeX monograph
│   ├── build_additional_pdfs.py -- Compiles guides and evaluation packages
│   ├── generate_full_monograph.py -- Full monograph generation wrapper
│   ├── generate_thesis_pdf.py   -- Modular dissertation generator wrapper
│   └── thesis_generator/     -- 12-chapter thesis generation package
└── docs/                     -- Documentation and metadata
    ├── arxiv_metadata.json   -- arXiv submission metadata (math.AP / math.LO)
    ├── arxiv_submission_guide.md -- Step-by-step submission instructions
    └── private-notes/        -- Local correspondence and reviewer packages (git-ignored)
```

---

## How to Build

### 1. Build and Audit the Lean 4 Package

Prerequisites: [Lean 4 & Elan](https://leanprover-community.github.io/get_started.html)

Using `make`:
```bash
make lean    # Compiles the Lean package via lake build
make audit   # Runs AxiomCheck.lean to inspect kernel axioms
```

Or directly via `lake`:
```bash
cd lean
lake exe cache get   # Downloads precompiled Mathlib cache
lake build           # Builds the ResearchPaper library
lake env lean AxiomCheck.lean
```

Expected axiom audit output:
```text
'navier_stokes_unconditional_regularity' depends on axioms: [propext, Classical.choice, Quot.sound]
'bkm_blowup_exclusion' depends on axioms: [propext, Classical.choice, Quot.sound]
'differential_to_exponential_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
```

### 2. Compile the Research Monograph (LaTeX / PDF)

Using `make`:
```bash
make pdf
```

Or compile directly with `pdflatex`:
```bash
cd paper
pdflatex -interaction=nonstopmode -output-directory=build monograph.tex
pdflatex -interaction=nonstopmode -output-directory=build monograph.tex
```

Alternatively, to build the complete KaTeX-typeset HTML and PDF via Playwright:
```bash
python scripts/assemble_and_build.py
```

### 3. Clean Build Artifacts

```bash
make clean
```

---

## Citation

If you consult or build upon this research framework or formalization, please cite:

```bibtex
@misc{prajapati2026navierstokes,
  author        = {Rohit Ramakant Prajapati},
  title         = {On the Directional Drift-Diffusion of Vorticity, Scale-Invariant Strain Bounds, and Ancient Rigidity for the 3D Incompressible Navier--Stokes Equations},
  year          = {2026},
  howpublished  = {Research Monograph and Lean 4 Formalization},
  note          = {GitHub: Rohitramakantprajapati/research-paper}
}
```

---

## License

This project is licensed under the [Apache License, Version 2.0](LICENSE).
