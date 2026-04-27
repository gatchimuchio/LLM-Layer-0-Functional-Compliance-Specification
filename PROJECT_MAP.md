# Project Map

## Repository purpose

Reproducible term-explication and finite-specification audit package for the Layer-0 functional minimum of contemporary Large Language Models.

## Core files

| Path | Purpose |
|---|---|
| `README.md` / `README.ja.md` | Main English/Japanese entry points |
| `llm_minimal_architecture_groups_v3_0.py` | Deterministic generator for artifacts |
| `appendices/layer_a_obligation_graph_enumeration_v0_5/` | Layer A declared obligation-graph enumeration |
| `docs/claim_boundary_and_semantics.md` | Claim boundary and non-overclaim rules |
| `docs/component_granularity_justification.md` | Why the root decomposition uses six roles |
| `docs/objection_routing_protocol.md` | Valid/invalid objection routing |
| `docs/official_llm_reference_bundle.md` | Official usage anchors |
| `docs/reference_strength_matrix.md` | Reference strength classification |
| `scripts/verify_manifest.py` | SHA256 manifest verifier |
| `scripts/generate_repository_manifest.py` | Repository manifest generator |

## v3.0 changes

- Replaced overclaim-forward wording with specification-forward wording.
- Removed self-assigned numeric calibrated probability estimate scores.
- Replaced the v0.5 natural-language output harness with v0.5 declared obligation-graph enumeration.
- Added claim-boundary, component-granularity, and objection-routing documents.
- Preserved the counterexample protocol: a valid counterexample must be an LLM and must lack a Layer-0 role plus every functional equivalent.

