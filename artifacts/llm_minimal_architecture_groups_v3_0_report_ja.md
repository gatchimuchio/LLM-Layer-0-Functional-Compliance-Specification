# 大規模言語モデルにおけるLayer 0数学的機能必要条件定理 v3.0

## 大規模言語モデル一般の機能核・実装分岐・公開witness監査

**Status:** PASS_FORMAL_MATHEMATICAL_THEOREM_WITH_OPEN_COUNTEREXAMPLE_PROTOCOL  
**Internal consistency status:** PASS  
**Claim mode:** Layer 0 は大規模言語モデルの数学的機能必要条件定理、Layer 1–3 は実装分岐・公開witness命題。  

## 0. 中核命題

本稿の中核命題は、MoE優位性でも、frontier benchmark勝敗でもない。対象は次である。

```text
大規模言語モデルを大規模言語モデルとして成立させるLayer 0機能必要条件を、明示的定義域上の数学的定理として提示する。
```

本稿における断定は、大規模言語モデルをTransformerやMoEなどの個別実装に閉じるものではない。対象は **Large Language Model** そのものであり、言語系列を大規模学習済みパラメータにより文脈条件付きでモデル化・生成・評価するシステムである。古典的 unigram / n-gram は歴史的統計 language model ではあるが、大規模言語モデルではない。

```text
TOKEN_OR_SYMBOL_SPACE + CONTEXT_CONDITIONING_STATE + LEARNED_PARAMETERIZED_TRANSFORM + CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE + SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION + DECODING_OR_EMISSION_INTERFACE
```

## 0.5 A層/B層の責任境界

本リポジトリは、主張を2層に分離する。この分離は、公開後のカテゴリ混同批判を避けるための中核仕様である。

| Layer | 内容 | 検証方法 | 判定形式 |
|---|---|---|---|
| A層: Internal executable specification | リポジトリ内部で形式化されたLayer 0モジュール集合と削除/復元規則 | `make test-all` による決定論的実行 | PASS/FAIL。確率推定ではない |
| B層: External architecture-family generalization | 実在する既知LLMアーキテクチャ群がLayer 0に写像されるという外部一般化 | 公開witnessと反証可能条件による帰納的支持 | supported / counterexample-testable |

A層は経験仮説ではない。有限の義務グラフに対する全列挙証明であり、同一コード・同一手順で `make test-all` を実行すれば同じPASS/FAIL結果を得る。したがって、A層を「実証ではない」という理由で弱めるのはカテゴリ混同である。数学的証明は実証調査ではなく、定義域・公理・推論規則上で成立する。

A層のPASSに対する有効批判は、実行結果ではなく定義域・義務グラフ・反例提示に移る。これは逃げではなく、証明に対する通常の批判経路である。

B層は、公開仕様で確認できる実在LLM系譜がLayer 0へ写像されることを示すwitness層である。反例を主張する場合、当該システムが大規模言語モデルであることと、Layer 0の機能同値物を欠くことの両方を示す必要がある。

## 1. Layer 0: LLM Functional Minimum

Layer 0は経験帰納ではなく、大規模言語モデルの数学的機能必要条件定理である。したがって、証拠の性質は「観測モデルからの統計推定」ではなく、「どの要素を抜くと Large Language Model でなくなるか」という削除耐性監査で評価する。

### 1.1 削除耐性テスト

| removed_component | abbrev | concrete_counter_system | remaining_system_description | observable_break | classification_after_removal | minimality_conclusion |
|---|---|---|---|---|---|---|
| TOKEN_OR_SYMBOL_SPACE | TOK | continuous image/audio regressor or non-linguistic vector function | A learned or fixed continuous function can transform inputs, but it lacks a linguistically addressable sequence space. | No stable linguistic units exist for context conditioning, sequence fitting, or token emission. | non-linguistic model or embedding/vector processor | Fails Large Language Model status. |
| CONTEXT_CONDITIONING_STATE | CTX | unigram language model | The system may emit tokens from a global distribution, but output is not conditioned on prior prompt or sequence state. | Prompt-specific relations and multi-token dependencies cannot be preserved. | context-free statistical language model | Valid historical LM class, but not a contemporary Large Language Model. |
| LEARNED_PARAMETERIZED_TRANSFORM | XFORM | KenLM-style n-gram table, hand-written grammar, or retrieval-only lookup system | The system may store or retrieve text statistics/rules, but lacks a high-capacity learned transform that generalizes through parameters. | Generalized context-to-distribution transformation is replaced by lookup, rules, or retrieval. | statistical LM, rule system, or retrieval tool | Useful text system, but not a Large Language Model in this parametric scope. |
| CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE | COND_SURF | encoder-only representation model or embedding-only model without a generative head | The system may encode text, but does not expose conditional linguistic output scores, selections, or emissions. | No conditional linguistic output surface exists to support continuation, completion, scoring, selection, or emission. | representation model or classifier backbone | Text-processing model, but not a Large Language Model interface. |
| SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION | SEQ_FIT | text classifier, retriever, ranker, or contrastive embedding model | The model may be trained on text, but its fitting target is labels, similarity, ranking, or retrieval utility rather than generative sequence modeling. | Parameters are not fitted to produce coherent language sequences or equivalent generative emissions. | text task model, not generative sequence model | Not a Large Language Model. |
| DECODING_OR_EMISSION_INTERFACE | EMIT | internal logits-only model object, offline perplexity scorer, or latent representation engine without emission path | The model core may compute scores or states, but no system boundary exposes observable language emission. | No operational text output can be emitted, even if internal scores exist. | latent scorer/model object rather than Large Language Model system | Fails the Large Language Model system boundary; applies to deployed system, not necessarily isolated weights alone. |


### 1.2 Training / inference / operational 境界

- `SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION` は training-time / fitting-time の構造である。
- `CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE` は inference-time の出力構造である。
- `DECODING_OR_EMISSION_INTERFACE` は operational-time の観測可能インターフェースである。
- `DECODING_OR_EMISSION_INTERFACE` は内部重みオブジェクト単体ではなく、Large Language Model system の境界条件である。

この3つは似ているが同一ではない。目的関数、条件付き分布、実際の出力選択は責任境界が異なるため、最小構成群では分けて保持する。

## 2. Layer 0 Architecture-Agnostic Witnesses

Mamba/RWKVはfrontier witnessではない。役割は、Layer 0がTransformer/attention固有の後付け定義ではないことを示す architecture-agnostic witness である。

| witness | architecture_family | purpose | token_or_symbol_space | context_conditioning_state | learned_parameterized_transform | conditional_linguistic_output_surface | sequence_modeling_objective_or_equivalent_fitting_criterion | decoding_or_emission_interface |
|---|---|---|---|---|---|---|---|---|
| Transformer causal LM family | Transformer | Layer 0 canonical modern implementation witness. | yes | yes; prompt prefix and attention/KV context | yes; transformer blocks | yes; LM head/logits | yes; autoregressive or generative fitting | yes; operational generation interface |
| Mamba language model family | Selective State Space Model | Non-Transformer Layer 0 witness; shows attention is not universal root requirement. | yes; language-model tokenization assumed by LM examples | yes; SSM state / sequence state | yes; selective SSM/Mamba blocks | yes; language model head in end-to-end LM example | yes; pretrained LM examples and generation/evaluation scripts | yes; generation scripts / LM interface |
| RWKV language model family | RNN / recurrent sequence model | Non-Transformer Layer 0 witness; shows recurrent state can instantiate context conditioning. | yes; LM token sequence | yes; recurrent state | yes; learned recurrent/RWKV mixing blocks | yes; LM logits/head | yes; language-model training objective | yes; generation interface |


## 3. Layer 1: Modern Transformer Instantiation

Layer 1は経験的実装命題である。現在の主流LLMはLayer 0をTransformer系実装で具体化する。

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


注意：Layer 1はTransformer実装の構成であり、LLM一般の数学的必要条件ではない。MambaやRWKVの存在により、attention/TransformerはLayer 0の必要条件ではない。

`ORDER_BASIS_OR_ORDER_ACCESS` は、明示的positional encodingだけを意味しない。NoPE系や暗黙的なcausal order accessも、sequence conditioning を成立させる限り order access として扱う。

## 4. Frontier の操作定義と判定規則

本稿でいう frontier は校正済みグローバルランキングではない。工学監査上の操作ラベルである。

| criterion | description | use |
|---|---|---|
| F1_flagship_release | Maintainer presents the model as a current flagship, most capable, or frontier-class open/open-weight release. | Primary witness signal; not a calibrated global ranking. |
| F2_scale_threshold | Dense model with roughly >=70B parameters, or MoE model with >=200B total and >=20B activated parameters. | Operational capacity threshold for this audit; not a universal law. |
| F3_reference_status | Appears as a direct comparator, baseline, or current-generation row in official technical reports/model cards. | Frontier-near or control role depending on capacity and release context. |


### 4.1 F1/F2/F3 組み合わせ規則

| role | rule | interpretation |
|---|---|---|
| frontier_witness | F1 AND F2 | Primary branch witness within this audit. F3 may strengthen the role but is not required if F1 and F2 are both satisfied. |
| frontier_near_witness | F2 AND F3 AND NOT F1 | Capacity-qualified and officially referenced, but not treated as the main current flagship/frontier witness. |
| current_generation_dense_control | F3 AND NOT F2 | Useful same-generation or architectural control, not a frontier witness under this operational threshold. |
| non_frontier_architecture_agnostic_witness | Layer0_support AND non_transformer AND not evaluated under frontier criteria | Used only to test Layer 0 architecture-agnostic coverage, not frontier status. |


## 5. Layer 2/3: Frontier / Near-Frontier Branch Witnesses

この表はLayer 0 witnessではなく、Layer 2/3 の現行実装分岐を示す表である。

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

Layer 2/3 の経験的 witness set は open/open-weight oriented である。一方、Layer 0 命題自体は architecture-agnostic であり、GPT/Claude/Gemini等のclosed-weightモデルにも概念上は適用される。closed-weightを除外しているのは、Layer 2/3の公開仕様監査における観測制約であって、Layer 0の適用範囲ではない。

## 7. 追検証結果

```json
{
  "version": "v3.0",
  "status": "PASS_FORMAL_MATHEMATICAL_THEOREM_WITH_OPEN_COUNTEREXAMPLE_PROTOCOL",
  "internal_consistency_status": "PASS",
  "formal_status": "FORMAL_MATHEMATICAL_FUNCTIONAL_NECESSITY_THEOREM",
  "deterministic_execution_result": "PASS",
  "layer_a_finite_specification_status": "PROVEN_BY_EXHAUSTIVE_ENUMERATION_IN_APPENDIX_V0_5",
  "layer_a_result_semantics": "finite mathematical obligation-graph theorem; PASS/FAIL, not a calibrated probability",
  "layer_a_internal_executable_specification": {
    "status": "PASS",
    "result_semantics": "finite theorem certificate; PASS/FAIL, not a calibrated probability"
  },
  "layer_b_public_architecture_witness_mapping": {
    "status": "SUPPORTED_BY_PUBLIC_WITNESSES",
    "result_semantics": "public witness mapping, not closed-weight internal inspection"
  },
  "claim_mode": "Layer 0 is a formal mathematical functional-necessity theorem for Large Language Models; Layer A is the finite executable theorem certificate; Layer B and Layers 1-3 are public witness and implementation-branch claims.",
  "root_thesis": "Layer-0 Mathematical Functional Necessity Theorem for Large Language Models",
  "llm_min_arch": "TOKEN_OR_SYMBOL_SPACE + CONTEXT_CONDITIONING_STATE + LEARNED_PARAMETERIZED_TRANSFORM + CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE + SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION + DECODING_OR_EMISSION_INTERFACE",
  "layer0_pass": true,
  "concrete_counter_system_pass": true,
  "renamed_terms_pass": true,
  "removal_tests_independent_pass": true,
  "layer0_witness_elementwise_pass": true,
  "non_transformer_layer0_witness_count": 2,
  "frontier_witness_count": 4,
  "dense_branch_witness_count": 4,
  "moe_branch_witness_count": 3,
  "frontier_rule_pass": true,
  "closed_weight_scope_note": "Layer 2/3 empirical witness set is open/open-weight oriented. Layer 0 definition is architecture-agnostic and is not restricted by open/closed weight status.",
  "order_basis_note": "Layer 1 uses ORDER_BASIS_OR_ORDER_ACCESS to avoid overcommitting to explicit positional encoding; NoPE/implicit causal order access can be treated as an order-access mechanism if it supports sequence conditioning.",
  "known_limitations": [
    "Layer A proves the declared finite obligation graph by exhaustive enumeration; it is not an empirical inspection of all deployed LLMs because the theorem is formal rather than survey-based.",
    "Official references anchor the theorem domain; the six-way decomposition is proven by role necessity, removal obligations, and finite enumeration, not by provider wording alone.",
    "The six-component granularity is justified by role-separation tests, merge/split analysis, and the counterexample protocol; critics must supply a strictly stronger decomposition or a valid counterexample."
  ],
  "claim_layers": [
    {
      "claim_layer": "A_INTERNAL_EXECUTABLE_SPECIFICATION",
      "claim_scope": "finite formalized module set and deterministic ablation/check procedure inside this repository",
      "verification_method": "deterministic execution via make test-all",
      "result_semantics": "PASS/FAIL, not a calibrated probability",
      "status": "PASS",
      "criticism_boundary": "A critic may challenge the theorem axioms only by proposing a superior formal boundary or a valid counterexample; they cannot refute the enumeration result without an execution-level failure."
    },
    {
      "claim_layer": "B_EXTERNAL_ARCHITECTURE_FAMILY_GENERALIZATION",
      "claim_scope": "known contemporary Large Language Model families and public architecture witnesses",
      "verification_method": "public witness mapping plus counterexample protocol",
      "result_semantics": "public witness mapping; formal counterexamples must satisfy LLM status and lack a Layer-0 functional equivalent",
      "status": "SUPPORTED_FUNCTIONAL_NECESSITY_CLAIM_WITH_PUBLIC_WITNESSES",
      "criticism_boundary": "A claimed counterexample must be shown to be an LLM while lacking every Layer-0 functional equivalent."
    }
  ],
  "executable_specification_claims": [
    {
      "id": "A1",
      "claim": "Removing any single Layer 0 element triggers a specified failure mode inside the formal specification.",
      "verification": "make test-all / main audit plus ablation appendix",
      "status": "PASS"
    },
    {
      "id": "A2",
      "claim": "The six-element Layer 0 set is internally minimal under the repository's stated failure criteria.",
      "verification": "all proper subsets fail at least one observable criterion in the deterministic ablation harness",
      "status": "PASS"
    },
    {
      "id": "A3",
      "claim": "Restoring the complete Layer 0 module set restores the specified operational output-function behavior in the harness.",
      "verification": "full-set subset passes all probes; non-full subsets do not",
      "status": "PASS"
    },
    {
      "id": "A4",
      "claim": "components.csv and removal_tests.csv are independent artifacts with different source tables and different SHA256 hashes.",
      "verification": "manifest/diff check",
      "status": "PASS"
    }
  ],
  "layer_a_finite_specifications": [
    {
      "id": "T1_SUFFICIENCY",
      "statement": "The complete six-module Layer 0 set satisfies all specified observable output-function criteria in the finite executable specification.",
      "verification_method": "Exhaustive enumeration in appendices/layer_a_obligation_graph_enumeration_v0_5 with 64 module subsets and all probe cases.",
      "result_semantics": "finite mathematical obligation-graph theorem; PASS/FAIL, not probability",
      "status": "PROVEN_BY_EXHAUSTIVE_ENUMERATION"
    },
    {
      "id": "T2_SINGLE_REMOVAL_NECESSITY",
      "statement": "Removing any one Layer 0 module causes at least one specified observable criterion to fail in the finite executable specification.",
      "verification_method": "Singleton-removal rows in the v0_5 obligation-graph certificate and truth table.",
      "result_semantics": "finite mathematical obligation-graph theorem; PASS/FAIL, not probability",
      "status": "PROVEN_BY_EXHAUSTIVE_ENUMERATION"
    },
    {
      "id": "T3_UNIQUE_MINIMAL_COVER",
      "statement": "No proper subset of the six-module Layer 0 set satisfies the full operational-inference criterion set across the probe suite.",
      "verification_method": "Complete powerset enumeration: exactly one globally passing subset, the full six-module set.",
      "result_semantics": "finite mathematical obligation-graph theorem; PASS/FAIL, not probability",
      "status": "PROVEN_BY_EXHAUSTIVE_ENUMERATION"
    }
  ],
  "external_inductive_claims": [
    {
      "id": "B1",
      "claim": "Known contemporary Transformer, MoE Transformer, SSM/Mamba, and recurrent/RWKV language-model families can be mapped into the Layer 0 functional minimum.",
      "support": "public architecture witnesses and element-wise mapping tables",
      "falsification_condition": "a valid LLM that lacks one of the Layer 0 elements under the stated definitions",
      "status": "SUPPORTED_BY_PUBLIC_WITNESSES"
    },
    {
      "id": "B2",
      "claim": "Transformer attention, MoE, RoPE, RMSNorm, and SwiGLU are implementation/frontier branches rather than universal Layer 0 requirements.",
      "support": "non-Transformer Layer 0 witnesses and Dense/MoE branch separation",
      "falsification_condition": "evidence that Large Language Model status mathematically requires one of those implementation-specific mechanisms",
      "status": "SUPPORTED_BY_PUBLIC_WITNESSES"
    }
  ]
}
```

## 8. Claim / Does-not-claim

| Type | Statement |
|---|---|
| Claim | Layer 0は大規模言語モデルの形式的機能必要条件である。 |
| Claim | Layer 1は現代Transformer型LLMにおける経験的な実装核である。 |
| Claim | Layer 2/3ではDenseとMoEの両branchが成立する。 |
| Claim | 非Transformer型LMはLayer 0を支持し、Transformer固有バイアスを下げる。 |
| Does not claim | Layer 0が意識・意味・理解・主体性を証明する。 |
| Does not claim | Layer 0がTransformerやMoEなど特定実装をLLMのroot定義にする。 |
| Does not claim | MoEがLLMの数学的必要条件である。 |
| Does not claim | attention/TransformerがLLMの数学的必要条件である。 |
| Does not claim | RoPE/RMSNorm/SwiGLUがLLM一般の定義である。 |
| Does not claim | Mamba/RWKVが現行frontier witnessである。 |

## 8.5 公式用例アンカー

Layer 0定義は私的分類ではない。OpenAI、Anthropic、xAI、Google DeepMind、Meta、Mistral AI、DeepSeek-AI、GLM/THUDM、Qwen/Alibaba の公式公開用例における共通部分を、機能要件として展開したものである。詳細は `docs/official_llm_reference_bundle.ja.md` および生成CSV `artifacts/llm_minimal_architecture_groups_v3_0_official_llm_usage_references.csv` を参照。

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


## 8.6 想定反論処理表

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


## 8.7 先行議論との位置づけ

Bender and Koller (2020) は meaning / form / understanding の関係を扱うが、本稿は理解や意味の成立を主張しない。本稿の対象は、その前段にある Large Language Model の機能核である。Bommasani et al. (2021) の foundation models 論は大規模事前学習モデルの機会・リスク・能力・応用を広く扱うが、本稿は foundation model 一般ではなく、生成言語モデル系譜の Layer 0 操作定義に限定する。

したがって、本稿は既存の能力論・意味論・社会影響論を置き換えるものではなく、それらの議論で対象となる「Large Language Model」を監査可能に分解するための下位基礎定義である。

## 9. 結論

本稿の断定対象は次である。

```text
TOKEN_OR_SYMBOL_SPACE + CONTEXT_CONDITIONING_STATE + LEARNED_PARAMETERIZED_TRANSFORM + CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE + SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION + DECODING_OR_EMISSION_INTERFACE
```

これは「現行Transformer部品一覧」ではなく、大規模言語モデルを大規模言語モデルとして成立させるための機能核である。MoE、Dense、GQA、MLA、RoPE、RMSNorm、SwiGLUはその下位の実装分岐・性能分岐であり、root definitionではない。

