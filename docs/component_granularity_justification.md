# Component Granularity Justification

## Question

Why six Layer-0 roles rather than five, seven, or another number?

## Answer

The six roles are not claimed to be the only possible vocabulary. They are the chosen root granularity because each role protects a distinct responsibility boundary. A valid alternative vocabulary must preserve these boundaries or explain why one boundary is unnecessary for LLM status.

## Six boundaries

| Component | Boundary protected | Why it is not redundant |
|---|---|---|
| TOKEN_OR_SYMBOL_SPACE | representation | Without linguistic addressability, there is no language sequence domain. |
| CONTEXT_CONDITIONING_STATE | inference state | Without context conditioning, the system collapses toward context-free statistics. |
| LEARNED_PARAMETERIZED_TRANSFORM | learned model object | Without learned transformation, the system is a rule table, retriever, or non-generalizing text tool. |
| CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE | conditional alternatives | Without this surface, the system may encode text but cannot define continuation/completion/scoring alternatives. |
| SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION | training/fitting | Without a language-sequence fitting criterion, the system is a classifier, retriever, ranker, or embedding model rather than an LLM. |
| DECODING_OR_EMISSION_INTERFACE | operational emission | Without an emission/scoring path, the object is a latent core or checkpoint tensor, not an operational LLM system. |

## Five-component merge tests

| Proposed merge | Failure |
|---|---|
| merge output surface + emission interface | hides the difference between latent conditional alternatives and operational emission |
| merge learned transform + fitting criterion | hides the difference between model object and training/fitting source |
| merge token space + context state | hides the difference between representation and conditioning |
| merge context state + output surface | hides the difference between state maintenance and conditional alternative selection |

## Seven-plus split tests

Seven or more components are possible as implementation refinements. For example, Transformer systems may split the learned transform into attention, MLP, normalization, residual path, positional/order access, and LM head. Those are Layer-1 implementation details, not Layer-0 root roles.

## Rule

- If a split is implementation-specific, keep it below Layer 0.
- If a merge hides a responsibility boundary, reject it for Layer 0.
- If an alternative vocabulary preserves all six boundaries, it is compatible with this repository rather than a refutation.

