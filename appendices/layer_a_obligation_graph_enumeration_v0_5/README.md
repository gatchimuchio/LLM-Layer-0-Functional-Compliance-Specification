# Layer A Obligation Graph Enumeration v0.5

## Status

`PROVEN_BY_EXHAUSTIVE_ENUMERATION_OF_DECLARED_OBLIGATION_GRAPH`

## Semantics

This appendix validates the declared finite obligation graph for the six Layer-0 roles.
It intentionally does not simulate natural-language answers and does not use hard-coded answer strings.
The pass/fail result is computed from declared obligations and required modules.

## What this proves

- The complete six-role set satisfies all declared obligations.
- Every singleton removal fails at least one declared obligation.
- No proper subset satisfies the full declared obligation graph.

## What this does not prove

- It does not empirically inspect all deployed or future LLMs.
- It does not prove that no alternative decomposition can ever be proposed.
- It does not assign calibrated calibrated probability estimate.

## Summary

```json
{
  "version": "v0.5",
  "certificate_type": "finite_obligation_graph_theorem_enumeration",
  "result_semantics": "finite theorem certificate over declared obligations; PASS/FAIL; not a calibrated probability",
  "layer_a_status": "PROVEN_BY_EXHAUSTIVE_ENUMERATION_OF_DECLARED_OBLIGATION_GRAPH",
  "module_count": 6,
  "subset_count": 64,
  "obligation_count": 6,
  "passing_subset_count": 1,
  "passing_subset_ids": [
    "M111111"
  ],
  "proper_subset_pass_count": 0,
  "single_removal_fail_count": 6,
  "full_set_pass": true,
  "explicit_limitation": "This certificate proves the declared finite role-obligation graph by exhaustive enumeration. It is formal proof, not empirical model inspection."
}
```
