# 3D Navier–Stokes Geometric Regularity Framework & Lean 4 Formalization

**Author:** Rohit Ramakant Prajapati  
**Affiliation:** Independent Researcher  
**License:** CC BY 4.0 for the monograph; MIT for `lean_package/`  
**DOI:** [10.5281/zenodo.XXXXXXX](https://zenodo.org)  

---

## Abstract

This repository contains the complete research monograph and machine-checked formal verification package for:

> **"On the Directional Drift-Diffusion of Vorticity, Scale-Invariant Strain Bounds, and Ancient Rigidity for the 3D Incompressible Navier–Stokes Equations"**

The research develops an analytical regularity framework centered on the physical dynamics of the vorticity direction field $\xi = \omega / |\omega| \in \mathbb{S}^2$, Littlewood–Paley dyadic frequency optimization, and ancient solution rigidity.

---

## Repository Structure

```
├── monograph.tex                   -- Complete AMS-LaTeX research monograph
├── arxiv_metadata.json             -- Full arXiv submission metadata (math.AP / math.LO)
├── arxiv_submission_guide.md       -- Field-by-field upload guide for arXiv.org
├── peer_review_cover_letters.md    -- Pre-submission evaluation letters for leading PDE analysts
├── .gitignore                      -- Git configuration ignoring build artifacts
└── lean_package/                   -- Verified Lean 4 / Mathlib 4 formalization package
    ├── lakefile.toml               -- Lake package configuration (Mathlib v4.35.0)
    ├── lean-toolchain              -- Pinned toolchain (leanprover/lean4:v4.35.0)
    ├── zenodo.json                 -- Immutable DOI archiving descriptor
    ├── README.md                   -- Lean package documentation
    ├── LICENSE                     -- Apache 2.0 license
    ├── AxiomCheck.lean             -- Machine audit script verifying zero 'sorry'
    ├── ResearchPaper.lean          -- Library entry point
    └── ResearchPaper/
        ├── Basic.lean              -- 3D Euclidean space (ℝ³), Point3, Vector3
        ├── DifferentialOps.lean    -- Fréchet derivatives, div, curl, strain, and NS predicate
        ├── GronwallBridge.lean     -- Zero-sorry certified real analysis
        ├── BiotSavart.lean         -- Constructive bound existence & BKM contradiction
        └── MainRegularity.lean     -- Top-level certified master theorem
```

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

## Building the Lean 4 Formalization

To compile and verify the formalization locally:

```bash
cd lean_package
lake update
lake build
```

To run the axiom audit verifying zero `sorry` and reliance strictly on canonical Lean 4 axioms (`propext`, `Classical.choice`, `Quot.sound`):
```bash
lake env lean AxiomCheck.lean
```

---

## Citation

```bibtex
@article{prajapati2026navierstokes,
  author    = {Rohit Ramakant Prajapati},
  title     = {On the Directional Drift-Diffusion of Vorticity, Scale-Invariant Strain Bounds, and Ancient Rigidity for the 3D Incompressible Navier--Stokes Equations},
  year      = {2026},
  eprint    = {arXiv:XXXX.XXXXX},
  archivePrefix = {arXiv},
  primaryClass  = {math.AP}
}
```

## License

The monograph and text in this repository are licensed under CC BY 4.0 (see [LICENSE](LICENSE)). The code in `lean_package/` is licensed under MIT (see [lean_package/LICENSE](lean_package/LICENSE)).

## Build

- `make pdf` compiles `monograph.tex` to PDF using `latexmk`.
- `make lean` builds the Lean package using Lake.
