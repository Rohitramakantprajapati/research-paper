/-
Copyright (c) 2026 Rohit Ramakant Prajapati. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Author: Rohit Ramakant Prajapati
-/
import ResearchPaper.Basic
import Mathlib.Analysis.Calculus.FDeriv.Basic
import Mathlib.Analysis.InnerProductSpace.Dual

open Set ContinuousLinearMap

/-- Basis vector in ℝ³ at coordinate index i. -/
def basisVector (i : Fin 3) : Point3 :=
  (WithLp.equiv 2 (Fin 3 → ℝ)).symm (Pi.single i 1)

/-- Divergence of a 3D vector field: ∇ · u = ∑ ∂uᵢ / ∂xᵢ. -/
noncomputable def divergence (u : VectorField3) (x : Point3) : ℝ :=
  ∑ i : Fin 3, fderiv ℝ u x (basisVector i) i

/-- Incompressibility condition: ∇ · u = 0 everywhere on ℝ³. -/
def IsIncompressible (u : VectorField3) : Prop :=
  ∀ x : Point3, divergence u x = 0

/-- Vorticity vector field (Curl): ω = ∇ × u. -/
noncomputable def curl (u : VectorField3) (x : Point3) : Vector3 :=
  let D := fderiv ℝ u x
  let w0 := D (basisVector 1) 2 - D (basisVector 2) 1
  let w1 := D (basisVector 2) 0 - D (basisVector 0) 2
  let w2 := D (basisVector 0) 1 - D (basisVector 1) 0
  (WithLp.equiv 2 (Fin 3 → ℝ)).symm ![w0, w1, w2]

/-- Convective acceleration term: (u · ∇)u. -/
noncomputable def advection_term (u : VectorField3) (x : Point3) : Vector3 :=
  fderiv ℝ u x (u x)

/-- Componentwise 3D Laplacian: Δu = ∑ ∂²u / ∂xᵢ². -/
noncomputable def laplacian3 (u : VectorField3) (x : Point3) : Vector3 :=
  ∑ i : Fin 3, fderiv ℝ (fun y => fderiv ℝ u y (basisVector i)) x (basisVector i)

/-- Gradient of a scalar pressure field: ∇p. -/
noncomputable def grad_scalar (f : Point3 → ℝ) (x : Point3) : Vector3 :=
  (WithLp.equiv 2 (Fin 3 → ℝ)).symm (fun i => fderiv ℝ f x (basisVector i))

/-- 
Full 3D Incompressible Navier–Stokes System Predicate on ℝ³ × (0, T):
  ∂u/∂t + (u · ∇)u + ∇p - ν Δu = 0,   ∇ · u = 0
-/
def IsNavierStokesSolution
    (u : TimeDepVectorField3)
    (p : ℝ → Point3 → ℝ)
    (ν : ℝ)
    (T : ℝ) : Prop :=
  (∀ t ∈ Ioo 0 T, IsIncompressible (u t)) ∧
  (∀ t ∈ Ioo 0 T, ∀ x : Point3,
    fderiv ℝ (fun s => u s x) t 1
    + advection_term (u t) x
    + grad_scalar (p t) x
    - ν • laplacian3 (u t) x = 0)
