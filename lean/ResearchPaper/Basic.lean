/-
Copyright (c) 2026 Rohit Ramakant Prajapati. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Author: Rohit Ramakant Prajapati
-/
import Mathlib.Analysis.InnerProductSpace.PiL2

open Set

/-- 3D Euclidean space ℝ³ represented via Mathlib's canonical PiL2 finite vector space. -/
abbrev Point3 := EuclideanSpace ℝ (Fin 3)
abbrev Vector3 := EuclideanSpace ℝ (Fin 3)

/-- A spatial vector field u : ℝ³ → ℝ³. -/
def VectorField3 := Point3 → Vector3

/-- A time-dependent spatial vector field u : ℝ → ℝ³ → ℝ³. -/
def TimeDepVectorField3 := ℝ → Point3 → Vector3

/-- Standard basis vectors in ℝ³. -/
def e0 : Vector3 := (WithLp.equiv 2 (Fin 3 → ℝ)).symm (Pi.single 0 1)
def e1 : Vector3 := (WithLp.equiv 2 (Fin 3 → ℝ)).symm (Pi.single 1 1)
def e2 : Vector3 := (WithLp.equiv 2 (Fin 3 → ℝ)).symm (Pi.single 2 1)
