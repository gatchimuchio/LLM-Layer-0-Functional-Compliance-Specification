# Layer-0 Mathematical Functional Necessity Theorem for Large Language Models v3.0

## Formal Functional Core, Implementation Branches, and Public Witness Audit

**Status:** PASS_FORMAL_MATHEMATICAL_THEOREM_WITH_OPEN_COUNTEREXAMPLE_PROTOCOL  
**Internal consistency status:** PASS  
**Claim mode:** Layer 0 is a formal mathematical functional-necessity theorem for Large Language Models; Layers 1-3 are implementation-branch and public-witness claims.  

## 0. Root thesis

```text
TOKEN_OR_SYMBOL_SPACE + CONTEXT_CONDITIONING_STATE + LEARNED_PARAMETERIZED_TRANSFORM + CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE + SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION + DECODING_OR_EMISSION_INTERFACE
```

## 0.5 Claim-layer separation

This repository separates two claim layers. This separation is a core part of the specification.

| Layer | Content | Verification method | Result semantics |
|---|---|---|---|
| Layer A: internal executable specification | the formalized Layer 0 module set and removal/restoration rules inside this repository | deterministic execution via `make test-all` | PASS/FAIL, not a calibrated probability |
| Layer B: external architecture-family generalization | the claim that known real-world LLM architecture families map into Layer 0 | public witnesses plus counterexample-testable boundary conditions | public witness mapping, counterexample-testable |

Layer A is not an empirical hypothesis. It is a deterministic property of a finite executable specification. Running `make test-all` verifies the stated PASS/FAIL result under the same code and execution procedure. Calling Layer A "not empirical" does not weaken it; it identifies the correct category.

However, Layer A does not prove that the specification design is the only possible design. A critic may challenge the design of the specification, but not the reproducibility of the stated execution result without showing an execution-level failure.

Layer B is the public witness mapping for real-world LLM families. A counterexample must be an LLM while lacking every Layer-0 functional equivalent.

This is a formal mathematical functional-necessity theorem for Large Language Models. It is not a Transformer-specific, MoE-specific, or consciousness/meaning claim. Classical unigram/n-gram systems may be historical statistical language models, but absent large learned contextual parametric transformation they are not LLMs in the contemporary technical sense.

## 1. Layer 0 removal tests with concrete counter-systems

| removed_component | abbrev | concrete_counter_system | remaining_system_description | observable_break | classification_after_removal | minimality_conclusion |
|---|---|---|---|---|---|---|
| TOKEN_OR_SYMBOL_SPACE | TOK | continuous image/audio regressor or non-linguistic vector function | A learned or fixed continuous function can transform inputs, but it lacks a linguistically addressable sequence space. | No stable linguistic units exist for context conditioning, sequence fitting, or token emission. | non-linguistic model or embedding/vector processor | Fails Large Language Model status. |
| CONTEXT_CONDITIONING_STATE | CTX | unigram language model | The system may emit tokens from a global distribution, but output is not conditioned on prior prompt or sequence state. | Prompt-specific relations and multi-token dependencies cannot be preserved. | context-free statistical language model | Valid historical LM class, but not a contemporary Large Language Model. |
| LEARNED_PARAMETERIZED_TRANSFORM | XFORM | KenLM-style n-gram table, hand-written grammar, or retrieval-only lookup system | The system may store or retrieve text statistics/rules, but lacks a high-capacity learned transform that generalizes through parameters. | Generalized context-to-distribution transformation is replaced by lookup, rules, or retrieval. | statistical LM, rule system, or retrieval tool | Useful text system, but not a Large Language Model in this parametric scope. |
| CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE | COND_SURF | encoder-only representation model or embedding-only model without a generative head | The system may encode text, but does not expose conditional linguistic output scores, selections, or emissions. | No conditional linguistic output surface exists to support continuation, completion, scoring, selection, or emission. | representation model or classifier backbone | Text-processing model, but not a Large Language Model interface. |
| SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION | SEQ_FIT | text classifier, retriever, ranker, or contrastive embedding model | The model may be trained on text, but its fitting target is labels, similarity, ranking, or retrieval utility rather than generative sequence modeling. | Parameters are not fitted to produce coherent language sequences or equivalent generative emissions. | text task model, not generative sequence model | Not a Large Language Model. |
| DECODING_OR_EMISSION_INTERFACE | EMIT | internal logits-only model object, offline perplexity scorer, or latent representation engine without emission path | The model core may compute scores or states, but no system boundary exposes observable language emission. | No operational text output can be emitted, even if internal scores exist. | latent scorer/model object rather than Large Language Model system | Fails the Large Language Model system boundary; applies to deployed system, not necessarily isolated weights alone. |


## 2. Layer 0 architecture-agnostic witnesses

| witness | architecture_family | purpose | token_or_symbol_space | context_conditioning_state | learned_parameterized_transform | conditional_linguistic_output_surface | sequence_modeling_objective_or_equivalent_fitting_criterion | decoding_or_emission_interface |
|---|---|---|---|---|---|---|---|---|
| Transformer causal LM family | Transformer | Layer 0 canonical modern implementation witness. | yes | yes; prompt prefix and attention/KV context | yes; transformer blocks | yes; LM head/logits | yes; autoregressive or generative fitting | yes; operational generation interface |
| Mamba language model family | Selective State Space Model | Non-Transformer Layer 0 witness; shows attention is not universal root requirement. | yes; language-model tokenization assumed by LM examples | yes; SSM state / sequence state | yes; selective SSM/Mamba blocks | yes; language model head in end-to-end LM example | yes; pretrained LM examples and generation/evaluation scripts | yes; generation scripts / LM interface |
| RWKV language model family | RNN / recurrent sequence model | Non-Transformer Layer 0 witness; shows recurrent state can instantiate context conditioning. | yes; LM token sequence | yes; recurrent state | yes; learned recurrent/RWKV mixing blocks | yes; LM logits/head | yes; language-model training objective | yes; generation interface |


## 3. Modern Transformer instantiation

| component_group | role |
|---|---|
| TOKENIZER_OR_TOKEN_SPACE | Empirical implementation of TOKEN_OR_SYMBOL_SPACE. |
| TOKEN_EMBEDDING | Maps token ids to internal vectors. |
| ORDER_BASIS_OR_ORDER_ACCESS | Encodes or preserves sequence order; includes explicit positional encodings such as RoPE/absolute/ALiBi, implicit causal order access, recurrent state order, or equivalent. |
| SEQUENCE_MIXER | Attention, SSM, recurrence, convolutional mixing, or equivalent context interaction mechanism. |
| NONLINEAR_TRANSFORM | MLP/FFN/SwiGLU/GeLU-class transform or equivalent nonlinear feature transform. |
| RESIDUAL_STABILITY | Residual stream plus normalization/stability mechanism where applicable. |
| OUTPUT_PROJECTION_OR_LM_HEAD | Projects hidden state to token logits or equivalent emission scores. |
| AUTOREGRESSIVE_OR_GENERATIVE_SEQUENCE_FITTING | Training/fitting criterion for sequence continuation, denoising, infilling, or equivalent text generation. |


## 4. Frontier definition and rules

| criterion | description | use |
|---|---|---|
| F1_flagship_release | Maintainer presents the model as a current flagship, most capable, or frontier-class open/open-weight release. | Primary witness signal; not a calibrated global ranking. |
| F2_scale_threshold | Dense model with roughly >=70B parameters, or MoE model with >=200B total and >=20B activated parameters. | Operational capacity threshold for this audit; not a universal law. |
| F3_reference_status | Appears as a direct comparator, baseline, or current-generation row in official technical reports/model cards. | Frontier-near or control role depending on capacity and release context. |


| role | rule | interpretation |
|---|---|---|
| frontier_witness | F1 AND F2 | Primary branch witness within this audit. F3 may strengthen the role but is not required if F1 and F2 are both satisfied. |
| frontier_near_witness | F2 AND F3 AND NOT F1 | Capacity-qualified and officially referenced, but not treated as the main current flagship/frontier witness. |
| current_generation_dense_control | F3 AND NOT F2 | Useful same-generation or architectural control, not a frontier witness under this operational threshold. |
| non_frontier_architecture_agnostic_witness | Layer0_support AND non_transformer AND not evaluated under frontier criteria | Used only to test Layer 0 architecture-agnostic coverage, not frontier status. |


## 5. Frontier / near-frontier branch witnesses

| model | branch | architecture_family | capacity_branch | frontier_role | frontier_criteria | parameter_note | source |
|---|---|---|---|---|---|---|---|
| Llama 3.1 405B | DENSE_FRONTIER_WITNESS | Transformer | Dense | frontier_witness | F1,F2 | 405B parameters; official card describes an auto-regressive language model using an optimized transformer architecture. | Meta/Hugging Face model card and Meta release blog |
| Llama 3.3 70B Instruct | DENSE_FRONTIER_NEAR_WITNESS | Transformer | Dense | frontier_near_witness | F2,F3 | 70B text-only model used as dense near-frontier witness rather than primary frontier witness. | Meta Llama 3.3 docs |
| Qwen2.5-72B | DENSE_FRONTIER_NEAR_WITNESS | Transformer | Dense | frontier_near_witness | F2,F3 | 72B-class causal LM; used as dense near-frontier/reference witness. | Qwen2.5-72B Hugging Face model card |
| Qwen3-32B | DENSE_CURRENT_GEN_CONTROL | Transformer | Dense | current_generation_dense_control | F3 | Largest dense Qwen3 model; used as current-generation dense control rather than frontier witness under F2 threshold. | Qwen3 model card / Qwen docs |
| DeepSeek-V3 | MOE_FRONTIER_WITNESS | Transformer-MoE | MoE | frontier_witness | F1,F2,F3 | 671B total / 37B activated; DeepSeekMoE and MLA are documented by maintainer. | DeepSeek-V3 README / technical report |
| Kimi K2 Base | MOE_FRONTIER_WITNESS | Transformer-MoE | MoE | frontier_witness | F1,F2,F3 | 1T total / 32B activated; official README states MoE, MLA, SwiGLU. | Kimi-K2 README |
| Qwen3-235B-A22B | MOE_FRONTIER_WITNESS | Transformer-MoE | MoE | frontier_witness | F1,F2,F3 | 235B total / 22B activated; model card lists MoE, GQA, experts, and causal LM type. | Qwen3-235B-A22B Hugging Face model card / Qwen3 technical report |


## 6. Closed-weight scope

The Layer 2/3 public witness set is necessarily open/open-weight oriented because public architecture evidence is auditable. Layer 0 itself is a formal mathematical functional-necessity theorem over Large Language Models and is not restricted by open/closed weight status.

## 6.5 Official usage anchor

The Layer-0 definition is not a private taxonomy. It is anchored in official public usage by OpenAI, Anthropic, xAI, Google DeepMind, Meta, Mistral AI, DeepSeek-AI, GLM/THUDM, and Qwen/Alibaba. See `docs/official_llm_reference_bundle.md` and the generated CSV `artifacts/llm_minimal_architecture_groups_v3_0_official_llm_usage_references.csv`.

| provider | source | short_official_excerpt | layer0_implication |
|---|---|---|---|
| OpenAI | How to work with large language models | Large language models are functions that map text to text. | text input/output, context-conditioned continuation, learned sequence modeling |
| Anthropic | Tracing the thoughts of a large language model | Language models like Claude ... trained on large amounts of data. | learned parameterized transform and linguistic output under context |
| xAI | xAI developer documentation / Grok introduction | Grok is a family of Large Language Models (LLMs). | xAI classifies Grok as an LLM; Grok-1 separately documents large MoE parameters |
| Google DeepMind | Gemini Diffusion model page | Large-language models are the foundation of generative AI today. | language generation remains the functional target even with non-standard generation mechanisms |
| Meta | Llama 3.1 405B Instruct model card | auto-regressive language model using an optimized transformer architecture | token/word sequence, context conditioning, conditional output surface, recursive text generation |
| Mistral AI | What's a Large Language Model (LLM)? | trained to understand and generate human language | learned language modeling, generation, and conditional linguistic output |
| DeepSeek-AI | DeepSeek-LLM README | an advanced language model comprising 67 billion parameters | large learned parameterized model trained over token-scale language data |
| GLM / THUDM | THUDM/GLM README | pretrained with an autoregressive blank-filling objective | language sequence fitting criterion can be autoregressive, blank-filling, or equivalent |
| Qwen / Alibaba Cloud | Qwen3 GitHub / Alibaba Cloud Qwen page | Qwen3 is the large language model series developed by Qwen team | officially positioned as an LLM family; architecture details are implementation branch, not root definition |


## 6.6 Objection-handling matrix

| objection | answer | boundary |
|---|---|---|
| Your definition of LLM is just your opinion. | False. The theorem domain is fixed by convergent official usage across OpenAI, Anthropic, xAI, DeepMind, Meta, Mistral, DeepSeek, GLM, and Qwen sources. Calling this an opinion is not a mathematical objection. | A critic may propose a different taxonomy, but must then show that the candidate is still called an LLM by contemporary technical usage while lacking a Layer-0 equivalent. |
| This is true only because you defined it that way. | No. The six elements decompose the ordinary content of Large + Language + Model: scale, learned modeling, linguistic sequences, contextual conditioning, fitted output behavior, and observable emission/scoring. | Mathematical proof routinely proceeds from definitions and axioms. To refute this theorem, a critic must reject the stated LLM boundary or provide a valid LLM counterexample lacking every Layer-0 equivalent. |
| A large n-gram system is a language model, so it refutes the learned-transform requirement. | It may be a historical statistical language model, but it is not a contemporary Large Language Model unless it has a large learned contextual model core or functional equivalent. | The repository explicitly separates historical LM from contemporary LLM. |
| Masked or infilling models are not next-token predictors. | The specification no longer uses next-token distribution as the root. It uses CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE, covering scoring, selection, infilling, denoising, and emission surfaces. | The implementation objective may vary; the Layer-0 role must remain. |
| A diffusion language model breaks autoregressive assumptions. | No. Diffusion changes the generation mechanism, not the need for linguistic representation, context conditioning, learned transform, conditional output surface, fitting criterion, and emission interface. | Non-autoregressive implementation is an implementation branch, not a Layer-0 escape hatch. |
| RAG or retrieval systems can answer text without being LLMs. | Correct, and therefore they are not counterexamples unless the generative LLM component itself lacks a Layer-0 equivalent while still qualifying as an LLM. | Composite systems must be decomposed into retriever/tool layers and LLM layers. |
| Encoder-only or embedding models process language. | They are language-related models, but not Large Language Models as operational generative/scoring systems unless they expose the conditional linguistic output role or equivalent. | Language processing is broader than LLM status. |
| Closed-weight GPT/Claude/Gemini internals are not inspectable. | Closed weights limit public architecture witness inspection, not the Layer-0 specification. If they function as LLMs, they must instantiate the functional roles or equivalents. | Layer 0 is functional; Layer B public witness coverage is evidence-limited. |
| Future architectures may lack one of these elements. | If they lack all functional equivalents of a Layer-0 role, they are a different AI class. If they are still LLMs, the role reappears under another implementation name. | Renaming an implementation does not remove the functional requirement. |
| Large has no fixed parameter threshold. | The specification does not require a universal parameter threshold. Large is used as a class boundary excluding hand-written, lookup, and small historical statistical systems. | Frontier thresholds are branch-witness audit thresholds, not the Layer-0 definition. |
| The decoding/emission interface is a system property, not a model-object property. | Correct boundary distinction; not a refutation. The theorem targets operational LLM systems. Isolated latent tensors are model objects, not the full LLM system boundary. | Model-core and system-interface boundaries must not be conflated. |
| Multimodal LLMs break the language-only definition. | No. MLLMs add modalities, but the LLM component still needs the language Layer-0 functions for linguistic output, scoring, or completion. | Additional modalities extend the system; they do not erase the language-model core. |


## 6.7 Relation to prior definitional discussions

Bender and Koller (2020) discuss meaning, form, and understanding; this report does not claim meaning, understanding, consciousness, or human-equivalent reasoning. Its scope is lower-level: the formal functional core of Large Language Models. Bommasani et al. (2021) frame foundation models broadly across capabilities, risks, systems, applications, and social impact; this report is narrower and focuses only on a formal mathematical functional-necessity theorem for Large Language Models.

Accordingly, this work is not a replacement for capability, meaning, or sociotechnical analyses. It is a lower-level audit scaffold for specifying what object those analyses are referring to when they discuss Large Language Models.

## 7. Conclusion

Layer 0 proves the formal mathematical functional minimum for any Large Language Model under the stated theorem domain. Transformer, Dense, MoE, MLA/GQA, RoPE, RMSNorm, and SwiGLU are implementation-level or frontier-level branches, not the universal root definition.
