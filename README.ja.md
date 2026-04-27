# 大規模言語モデルにおける Layer 0 数学的機能必要条件定理

**Version:** v3.0 / Layer A appendix v0.5  
**Formal status:** `FORMAL_MATHEMATICAL_FUNCTIONAL_NECESSITY_THEOREM`  
**Executable status:** `PROVEN_BY_EXHAUSTIVE_ENUMERATION_OF_DECLARED_OBLIGATION_GRAPH`  
**Primary artifact:** `llm_minimal_architecture_groups_v3_0.py`  
**A層 certificate:** `appendices/layer_a_obligation_graph_enumeration_v0_5/layer_a_executable_certificate.json`

本リポジトリは、**大規模言語モデル（LLM）** の Layer 0 最小構成について、数学的な機能必要条件定理を提示・検証する。

中核定理は次である。

> 現代的な大規模言語モデルとして成立する任意のシステムは、以下6つの Layer 0 役割を、明示的または機能同値的に必ず持つ。これらのいずれか一つと、その全機能同値物を欠くシステムは、AIシステム、テキスト処理器、分類器、検索器、エンコーダ、歴史的言語モデルではあり得ても、現代技術用語としてのLLMではない。

これは全デプロイ済みモデルの経験調査ではない。明示的に固定した技術的定義域上の形式定理である。数学的証明は定義・公理・有限列挙から成立してよい。「定義依存だ」というだけでは反論にならない。有効な反論には、より良い形式境界、または有効な反例が必要である。

## Layer 0 定理文

```text
TOKEN_OR_SYMBOL_SPACE
+ CONTEXT_CONDITIONING_STATE
+ LEARNED_PARAMETERIZED_TRANSFORM
+ CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE
+ SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION
+ DECODING_OR_EMISSION_INTERFACE
```

## LLM境界が私的感想ではない理由

定理の定義域は、主要LLM提供者・保守者の公式用例によりアンカーされる。

- OpenAI：LLMを text-to-text / 後続text予測として説明。
- Anthropic：LLMを、多数パラメータを持ち、大量text dataで訓練され、人間らしいtext生成等が可能なAI language modelとして説明。
- xAI：Grokを Large Language Models の family と公式分類。
- Meta：Llama 3.1 model cardで、Llamaを optimized transformer architecture を用いる auto-regressive language model と説明。
- Mistral AI：LLMを human language を理解・生成するよう訓練されたAIとして説明。
- DeepSeek-AI、GLM/THUDM、Qwen/Alibaba：language model / LLM family としての公式用例・model-family witnessを公開。

公式文言は定理の定義域を支える。6役割分解そのものは、公式文言だけではなく、役割分離、merge/split分析、削除義務、有限全列挙によって正当化する。

参照：

- `docs/official_llm_reference_bundle.ja.md`
- `docs/reference_strength_matrix.ja.md`
- `docs/component_granularity_justification.ja.md`

## Claim layers

| Layer | 何を示すか | 検証・支持 | 境界 |
|---|---|---|---|
| Layer 0 | LLM 6役割の数学的機能必要性 | 用語境界公理 + 役割分離論証 | 形式定理領域 |
| Layer A | 有限義務グラフ定理 | 64部分集合の全列挙 | 実行可能な形式証明 certificate |
| Layer B | 公開LLM系譜が Layer 0 に写像されること | 公式参照 + 公開witness | 公開witness mapping |
| Layer 1+ | Transformer/Dense/MoE/SSM/RWKVの分岐配置 | 公開アーキテクチャ記述 | Layer 0 配下の実装分岐 |

## A層 executable theorem certificate

appendix は、6つの Layer 0 役割の全64部分集合を列挙し、宣言済み義務が満たされるかを検証する。

期待結果：

```text
layer_a_status = PROVEN_BY_EXHAUSTIVE_ENUMERATION_OF_DECLARED_OBLIGATION_GRAPH
full_set_pass = true
proper_subset_pass_count = 0
single_removal_fail_count = 6
```

これは宣言済み有限義務グラフ上の数学的証明である。経験調査ではない。経験調査でないことは弱点ではなく、形式証明としてのカテゴリである。

## なぜ6要素か

6つの役割は、唯一可能な英語ラベルだとは主張しない。ただし、運用可能なLLMシステムの最小責任境界として必要である。

| Role | Boundary |
|---|---|
| TOKEN_OR_SYMBOL_SPACE | 表現境界 |
| CONTEXT_CONDITIONING_STATE | 推論状態境界 |
| LEARNED_PARAMETERIZED_TRANSFORM | 学習済みモデルオブジェクト境界 |
| CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE | 条件付き出力候補境界 |
| SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION | 訓練・適合境界 |
| DECODING_OR_EMISSION_INTERFACE | 運用出力境界 |

5要素への統合は責任境界を隠す。7要素以上への分割は Layer 0 のrootを越えて実装詳細へ落ちる。批判者は別分解を提案してもよいが、この定理を倒すには、より境界保存性の高い最小分解、または有効なLLM反例を提示する必要がある。

## 反例プロトコル

有効な反例は、次の2条件を同時に満たす必要がある。

1. 当該候補が、現代技術用語としての大規模言語モデルであること。
2. 当該候補が、Layer 0 役割の少なくとも一つと、その全機能同値物を欠くこと。

大規模・学習済み・文脈条件付き・言語系列モデリングを欠くシステムは、LLMの反例ではない。別種のAI/テキストシステムである。

## 反論ポリシー

- 「定義依存だ」は反論ではない。数学的定理は定義・公理に依存して成立する。
- 「全モデルの経験検査ではない」は反論ではない。本定理は形式定理であり、経験的witness mappingはB層で扱う。
- 「未来アーキテクチャが違う」は反論ではない。LLMなら6役割または同値物を持つ。持たないなら別AI、または用語改定問題である。
- 「Largeに固定閾値がない」は反論ではない。`Large` は現代的技術用語上のscale conditionであり、定理の駆動機構ではない。

## 主張すること

- LLM状態は、6つの Layer 0 役割またはその機能同値物を数学的に必要とする。
- Transformer attention、MoE、RoPE、RMSNorm、SwiGLU、MLA、GQAは実装・性能分岐であり、Layer 0 rootではない。
- Mamba/SSM、RWKV/recurrent language model は architecture-agnostic な Layer 0 構成を支持する。
- 公式参照は用語境界を支え、公開アーキテクチャwitnessは Layer B mapping を支える。

## 主張しないこと

- 意識、理解、意味、主体性、人間同等推論。
- closed-weight 内部の経験的検査。
- 6つの英語ラベル以外の語彙が不可能であること。
- Transformer、attention、MoE、RoPE、RMSNorm、SwiGLU、MLA、GQAがLLM普遍rootであること。

## Quickstart

```bash
make audit
make verify
make test-all
```

期待結果：

```text
main audit: PASS
artifact manifest: ALL_OK
Layer A obligation graph: PROVEN_BY_EXHAUSTIVE_ENUMERATION_OF_DECLARED_OBLIGATION_GRAPH
proper_subset_pass_count: 0
repository manifest: ALL_OK
```

## 最終位置づけ

最も強く、かつ正確な表現：

> 現代的大規模言語モデルの Layer 0 運用機能核に関する、再現可能な数学的機能必要条件定理および有限実行証明パッケージ。
