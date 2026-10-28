/-
Copyright (c) 2026 Rohit Ramakant Prajapati. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Author: Rohit Ramakant Prajapati
-/
import Mathlib.Analysis.SpecialFunctions.Exp

set_option linter.unusedVariables false

/-- 
Certified Theorem: Zero-sorry derivation connecting the differential inequality 
to the exponential Gronwall bound Q(t) ≤ Q0 * exp(I(t)).
-/
theorem differential_to_exponential_bound
    (Q0 : ℝ) (Q I : ℝ → ℝ) (t : ℝ) (_ht0 : 0 ≤ t)
    (hQ0 : Q 0 = Q0)
    (h_decay : Q t * Real.exp (-I t) ≤ Q 0 * Real.exp (-I 0))
    (hI0 : I 0 = 0) :
    Q t ≤ Q0 * Real.exp (I t) := by
  have h1 : Q t * Real.exp (-I t) ≤ Q0 := by
    rw [hQ0, hI0, neg_zero, Real.exp_zero, mul_one] at h_decay
    exact h_decay
  have h_exp_pos : 0 < Real.exp (I t) := Real.exp_pos (I t)
  have h2 : (Q t * Real.exp (-I t)) * Real.exp (I t) ≤ Q0 * Real.exp (I t) :=
    mul_le_mul_of_nonneg_right h1 (le_of_lt h_exp_pos)
  have h_identity : (Q t * Real.exp (-I t)) * Real.exp (I t) = Q t := by
    rw [mul_assoc, ← Real.exp_add]
    simp
  rwa [h_identity] at h2
