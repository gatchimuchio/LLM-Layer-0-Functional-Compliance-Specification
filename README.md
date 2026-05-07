# Layer-0 Mathematical Functional Necessity Theorem for Large Language Models

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE-MIT)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE-CC-BY-4.0)
[![make audit](https://img.shields.io/badge/make%20audit-PASS-brightgreen.svg)](#quickstart)
[![make verify](https://img.shields.io/badge/make%20verify-PASS-brightgreen.svg)](#quickstart)
[![Layer A](https://img.shields.io/badge/Layer%20A-PROVEN%20BY%20EXHAUSTIVE%20ENUMERATION-blue.svg)](appendices/layer_a_obligation_graph_enumeration_v0_5/layer_a_executable_certificate.json)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19826582.svg)](https://doi.org/10.5281/zenodo.19826582)

> **Version:** v3.0 / Layer A appendix v0.5
> **Formal status:** `FORMAL_MATHEMATICAL_FUNCTIONAL_NECESSITY_THEOREM`
> **Executable status:** `PROVEN_BY_EXHAUSTIVE_ENUMERATION_OF_DECLARED_OBLIGATION_GRAPH`
> **🇯🇵 Japanese version:** [README.ja.md](README.ja.md)

---

## 🚀 Layer-0 in 60 seconds

**Claim.** Every contemporary Large Language Model must instantiate **six** functional roles. Drop any one — and every functional equivalent — and the system stops being an LLM.

The six roles:

1. **TOKEN_OR_SYMBOL_SPACE** — what the model reads/writes
2. **CONTEXT_CONDITIONING_STATE** — what conditions the prediction
3. **LEARNED_PARAMETERIZED_TRANSFORM** — the trainable model object
4. **CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE** — the conditional output space
5. **SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION** — the training signal
6. **DECODING_OR_EMISSION_INTERFACE** — how the next token comes out

**Proof method.** Finite exhaustive enumeration of all 64 subsets of the six roles. The full set passes; every proper subset fails. Reproducible via `make audit` / `make verify`.

**Architecture-agnostic.** Transformer, Dense, MoE, SSM/Mamba, RWKV — all implementation branches *below* Layer-0. The six roles do not change.

---

## 🎯 What is this useful for?

| Use case | How Layer-0 helps |
| --- | --- |
| **Audit** | Six fixed responsibility boundaries — a reproducible compliance check, not vibes. `make audit` returns a deterministic PASS/FAIL with an executable certificate. |
| **Regulation & standards** | A formal, citation-anchored boundary for the question *"is this system an LLM?"* — survives architecture churn (Transformer → MoE → SSM → next thing). |
| **Architecture discussion** | A shared vocabulary that separates *what an LLM is* from *how it is implemented*. Attention, MoE, RoPE, RMSNorm, SwiGLU, MLA, GQA all sit **below** Layer-0. |
| **Counterexample protocol** | Clear refutation rules. A critic must produce either a stricter decomposition with better boundary preservation, or a valid LLM counterexample. "It's definition-dependent" is not a refutation. |

**One-line summary.** Layer-0 is a common language for auditing, regulating, and arguing about LLMs without sliding back into marketing terms.

---

## ⚡ Quickstart

```
make audit
make verify
make test-all
```

Expected status:

```
main audit: PASS
artifact manifest: ALL_OK
Layer A obligation graph: PROVEN_BY_EXHAUSTIVE_ENUMERATION_OF_DECLARED_OBLIGATION_GRAPH
proper_subset_pass_count: 0
repository manifest: ALL_OK
```

**Primary artifact:** `llm_minimal_architecture_groups_v3_0.py`
**Layer A certificate:** `appendices/layer_a_obligation_graph_enumeration_v0_5/layer_a_executable_certificate.json`

---

## Layer-0 theorem statement

This repository states and verifies a mathematical functional-necessity theorem for the Layer-0 minimum of **Large Language Models (LLMs)**.

The theorem is intentionally strong:

> Any system that qualifies as a contemporary Large Language Model must instantiate the six Layer-0 roles below, explicitly or through functional equivalents. A system that lacks one of these roles and every functional equivalent may still be an AI system, text tool, classifier, retriever, encoder, or historical language model, but it is not an LLM under the contemporary technical meaning of the term.

This is not a survey of every deployed model. It is a formal theorem over an explicitly fixed technical class. Mathematical proof is allowed to proceed from definitions, axioms, and finite enumeration; calling that "definition-dependent" is not a refutation unless the critic supplies a better formal boundary or a valid counterexample.

```
TOKEN_OR_SYMBOL_SPACE
+ CONTEXT_CONDITIONING_STATE
+ LEARNED_PARAMETERIZED_TRANSFORM
+ CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE
+ SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION
+ DECODING_OR_EMISSION_INTERFACE
```

## Why the LLM boundary is not private opinion

The theorem domain is anchored in convergent official usage by major LLM providers and maintainers:

* OpenAI describes LLMs as text-to-text systems that predict following text.
* Anthropic describes LLMs as high-parameter AI language models trained on vast text data and capable of generating human-like text.
* xAI officially classifies Grok as a family of Large Language Models.
* Meta's Llama 3.1 model card classifies Llama as an auto-regressive language model using an optimized transformer architecture.
* Mistral AI describes LLMs as AI systems trained to understand and generate human language.
* DeepSeek-AI, GLM/THUDM, and Qwen/Alibaba publish language-model / LLM-family systems with public model-family descriptions.

Provider language anchors the theorem domain. The six-role decomposition is not inferred from provider wording alone; it is justified by role separation, merge/split analysis, removal obligations, and finite exhaustive enumeration.

See:

* `docs/official_llm_reference_bundle.md`
* `docs/reference_strength_matrix.md`
* `docs/component_granularity_justification.md`

## Claim layers

| Layer | What it establishes | Verification / support | Boundary |
| --- | --- | --- | --- |
| Layer 0 | Mathematical functional necessity of the six LLM roles | term-boundary axioms + role-separation argument | formal theorem domain |
| Layer A | Finite obligation graph theorem | exhaustive enumeration of all 64 subsets | formal executable certificate |
| Layer B | Known public LLM families map to Layer 0 | official references and public model-family witnesses | public witness mapping |
| Layer 1+ | Transformer/Dense/MoE/SSM/RWKV branch placement | public architecture descriptions | implementation branches below Layer 0 |

## Layer A executable theorem certificate

The appendix enumerates all 64 subsets of the six Layer-0 roles and checks whether the declared obligations are satisfied.

Expected result:

```
layer_a_status = PROVEN_BY_EXHAUSTIVE_ENUMERATION_OF_DECLARED_OBLIGATION_GRAPH
full_set_pass = true
proper_subset_pass_count = 0
single_removal_fail_count = 6
```

This is a finite mathematical proof over the declared obligation graph. It is not an empirical inspection of all deployed models, because the claim is formal rather than survey-based.

## Why six components?

The six roles are not claimed to be the only possible English labels. They are the minimum responsibility boundaries required for an operational LLM system:

| Role | Boundary |
| --- | --- |
| TOKEN_OR_SYMBOL_SPACE | representation boundary |
| CONTEXT_CONDITIONING_STATE | inference-state boundary |
| LEARNED_PARAMETERIZED_TRANSFORM | learned model-object boundary |
| CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE | conditional output-alternative boundary |
| SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION | training/fitting boundary |
| DECODING_OR_EMISSION_INTERFACE | operational emission boundary |

A five-component merge hides a responsibility boundary. A seven-or-more split moves below the Layer-0 root into implementation refinements. A critic may propose a different decomposition, but to defeat this theorem they must show either a stricter minimal decomposition with better boundary preservation or a valid LLM counterexample.

## Counterexample protocol

A valid counterexample must satisfy both:

1. establish that the candidate is a contemporary Large Language Model in ordinary technical usage; and
2. establish that it lacks at least one Layer-0 role and every functional equivalent of that role.

If a system lacks large learned contextual language modeling, it is not an LLM counterexample. It is a different AI/text system.

## Objection policy

* "This is definition-dependent" is not a refutation. Mathematical theorems are definition- and axiom-dependent by construction.
* "This is not empirical inspection of every model" is not a refutation. The theorem is formal; empirical witness mapping is Layer B.
* "Future architecture may differ" is not a refutation. If it is an LLM, it must implement the six roles or equivalents. If it does not, it is a different AI class or it forces a terminology revision.
* "Large has no fixed parameter threshold" is not a refutation. `Large` is a contemporary technical scale condition, not the theorem's operative mechanism.

## What this claims

* LLM status mathematically requires the six Layer-0 roles or their functional equivalents.
* Transformer attention, MoE, RoPE, RMSNorm, SwiGLU, MLA, and GQA are implementation/performance branches, not the Layer-0 root.
* Mamba/SSM and RWKV/recurrent language models support architecture-agnostic Layer-0 framing.
* Public official references support the term boundary; public architecture witnesses support Layer B mapping.

## What this does not claim

* It does not claim consciousness, understanding, meaning, agency, or human-equivalent reasoning.
* It does not claim empirical inspection of closed-weight internals.
* It does not claim that the six English labels are the only possible vocabulary.
* It does not claim that Transformer, attention, MoE, RoPE, RMSNorm, SwiGLU, MLA, or GQA are universal LLM roots.

## Citation

If you use this repository, please cite via [CITATION.cff](CITATION.cff) or the Zenodo DOI badge above.

## License

Dual-licensed: [MIT](LICENSE-MIT) for code, [CC-BY-4.0](LICENSE-CC-BY-4.0) for documents and specifications.

## Final positioning

> A reproducible mathematical functional-necessity theorem and finite executable proof package for the Layer-0 operational core of contemporary Large Language Models.