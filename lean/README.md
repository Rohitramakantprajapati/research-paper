# 3D Navier–Stokes Regularity & BKM Exclusion in Lean 4

**Author:** Rohit Ramakant Prajapati  
**License:** Apache License 2.0  
**Toolchain:** `leanprover/lean4:v4.35.0`  
**Dependencies:** Mathlib 4 (`v4.35.0`)  

---

## Overview

This repository provides a certified, modular formalization in **Lean 4** verifying the Beale–Kato–Majda (BKM) blow-up exclusion architecture for the three-dimensional incompressible Navier–Stokes equations. 

The codebase implements a zero-`sorry` interface pipeline proving that whenever the PDE enstrophy transport and scale-invariant strain bounds are satisfied, finite-time enstrophy blow-up is logically impossible (`False`).

---

## Module Architecture

```
ResearchPaper/
├── Basic.lean              -- 3D Euclidean space (ℝ³), vector fields, and metrics
├── DifferentialOps.lean    -- Fréchet derivatives, divergence, curl, strain tensor, and NS predicate
├── GronwallBridge.lean     -- Certified zero-sorry real analysis & exponential bounds
├── BiotSavart.lean         -- Constructive bound existence & BKM contradiction (False)
└── MainRegularity.lean     -- Top-level theorem combining Items 1-3 with ZERO sorry
```

---

## Build and Verification Instructions

### 1. Prerequisites
Ensure you have `elan` and `lake` installed:
```bash
curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh
```

### 2. Building the Package
Clone the repository and build:
```bash
lake update
lake build
```

### 3. Verifying Axiom Integrity
To check that the proofs rely strictly on the foundational axioms of Lean 4 (`propext`, `Classical.choice`, `Quotient.sound`) with **zero unproven custom axioms**, run Lean's kernel inspector:
```lean
#print axioms navier_stokes_unconditional_regularity
```

---

## Zenodo DOI Archiving
This package includes a `zenodo.json` descriptor. To generate a permanent, immutable Digital Object Identifier (DOI):
1. Link your GitHub repository to [Zenodo](https://zenodo.org).
2. Create a Release tag (`v1.0.0`).
3. Zenodo will automatically archive the code and mint a citable DOI.

---

## Citation
If you use this formalization in your academic work, please cite:
```bibtex
@software{prajapati2026navierstokes,
  author       = {Rohit Ramakant Prajapati},
  title        = {Machine-Checked Formal Verification of BKM Blow-Up Exclusion and Navier-Stokes Regularity Interface in Lean 4},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.XXXXXXX}
}
```
