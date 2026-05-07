# LLM Layer-0 機能必然性定理

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE-MIT)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE-CC-BY-4.0)
[![make audit](https://img.shields.io/badge/make%20audit-PASS-brightgreen.svg)](#クイックスタート)
[![make verify](https://img.shields.io/badge/make%20verify-PASS-brightgreen.svg)](#クイックスタート)
[![Layer A](https://img.shields.io/badge/Layer%20A-PROVEN%20BY%20EXHAUSTIVE%20ENUMERATION-blue.svg)](appendices/layer_a_obligation_graph_enumeration_v0_5/layer_a_executable_certificate.json)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19826582.svg)](https://doi.org/10.5281/zenodo.19826582)

> **バージョン:** v3.0 / Layer A 付録 v0.5
> **形式ステータス:** `FORMAL_MATHEMATICAL_FUNCTIONAL_NECESSITY_THEOREM`
> **実行ステータス:** `PROVEN_BY_EXHAUSTIVE_ENUMERATION_OF_DECLARED_OBLIGATION_GRAPH`
> **🇬🇧 English:** [README.md](README.md)

---

## 🚀 1分でわかる Layer-0

**主張。** 現代の Large Language Model（LLM）は必ず **6 つの機能役割** を実装する。1 つでも、その機能等価物まで含めて欠ければ、それはもう LLM ではない。

6 つの役割：

1. **TOKEN_OR_SYMBOL_SPACE** — 入出力されるトークン／記号空間
2. **CONTEXT_CONDITIONING_STATE** — 予測を条件づける文脈状態
3. **LEARNED_PARAMETERIZED_TRANSFORM** — 学習されるパラメータ化モデル本体
4. **CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE** — 条件付き出力面
5. **SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION** — 系列学習目的関数（または等価な適合基準）
6. **DECODING_OR_EMISSION_INTERFACE** — 出力放出インタフェース

**証明手法。** 6 役割の 64 部分集合を有限全列挙。フル集合で PASS、真部分集合では全て FAIL。`make audit` / `make verify` で再現可能。

**アーキテクチャ非依存。** Transformer、Dense、MoE、SSM/Mamba、RWKV はすべて Layer-0 の **下層** にある実装枝。6 役割は変わらない。

---

## 🎯 これ何の役に立つ？

| 用途 | Layer-0 が提供するもの |
| --- | --- |
| **監査** | 責任境界が 6 つに固定されているため、雰囲気ではなく再現可能な準拠チェックが回る。`make audit` が決定論的に PASS/FAIL と実行可能証明書を返す。 |
| **規制・標準化** | 「これは LLM か？」という問いに対する、引用根拠付きの形式的境界。アーキテクチャ世代交代（Transformer → MoE → SSM → 次の何か）に耐える。 |
| **アーキテクチャ議論** | *LLM とは何か* と *どう実装するか* を分離する共通語彙。Attention、MoE、RoPE、RMSNorm、SwiGLU、MLA、GQA はすべて Layer-0 の **下** に位置する。 |
| **反例プロトコル** | 反証ルールが明示されている。批判者は「より厳しい分解」または「妥当な LLM 反例」を提出する必要がある。「定義依存だ」は反証にならない。 |

**1 行要約。** Layer-0 は、LLM の監査・規制・議論をマーケティング用語に逆戻りさせずに行うための共通言語。

---

## ⚡ クイックスタート

```
make audit
make verify
make test-all
```

期待される出力：

```
main audit: PASS
artifact manifest: ALL_OK
Layer A obligation graph: PROVEN_BY_EXHAUSTIVE_ENUMERATION_OF_DECLARED_OBLIGATION_GRAPH
proper_subset_pass_count: 0
repository manifest: ALL_OK
```

**主成果物:** `llm_minimal_architecture_groups_v3_0.py`
**Layer A 証明書:** `appendices/layer_a_obligation_graph_enumeration_v0_5/layer_a_executable_certificate.json`

---

## Layer-0 定理ステートメント

本リポジトリは、**Large Language Model（LLM）** の Layer-0 最小構成について、機能必然性定理を提示し検証する。

定理は意図的に強い：

> 現代的な Large Language Model に該当するシステムは、以下 6 つの Layer-0 役割を、明示的にあるいは機能等価物として実装しなければならない。これら役割のいずれかとその全機能等価物を欠くシステムは、AI システム、テキストツール、分類器、検索器、エンコーダ、または歴史的な言語モデルではあり得るが、現代の技術的意味における LLM ではない。

これは全展開済みモデルのサーベイではない。明示的に固定した技術クラス上の形式定理である。数学的証明は定義・公理・有限列挙から進めてよく、「定義依存だ」と言うことはそれだけでは反証にならない。批判者はより良い形式境界か、妥当な反例を提示する必要がある。

```
TOKEN_OR_SYMBOL_SPACE
+ CONTEXT_CONDITIONING_STATE
+ LEARNED_PARAMETERIZED_TRANSFORM
+ CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE
+ SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION
+ DECODING_OR_EMISSION_INTERFACE
```

## なぜ LLM の境界が私見ではないか

定理ドメインは、主要 LLM プロバイダ／メンテナによる収束的な公式用法に錨付けされている：

* OpenAI は LLM を、続くテキストを予測する text-to-text システムとして記述。
* Anthropic は LLM を、膨大なテキストデータで学習され人間に近いテキストを生成可能な高パラメータ AI 言語モデルとして記述。
* xAI は Grok を Large Language Model のファミリとして公式分類。
* Meta の Llama 3.1 モデルカードは Llama を、最適化された Transformer アーキテクチャを使用する自己回帰型言語モデルとして分類。
* Mistral AI は LLM を、人間言語を理解・生成するよう学習された AI システムとして記述。
* DeepSeek-AI、GLM/THUDM、Qwen/Alibaba は、公式モデルファミリ記述付きで言語モデル／LLM ファミリのシステムを公開している。

プロバイダの言語が定理ドメインを錨付けする。6 役割分解はプロバイダの文言からのみ推論されるのではなく、役割分離、結合／分割解析、除去義務、有限全列挙によって正当化される。

参照：

* `docs/official_llm_reference_bundle.md`
* `docs/reference_strength_matrix.md`
* `docs/component_granularity_justification.md`

## 主張階層

| 階層 | 何を確立するか | 検証／支持 | 境界 |
| --- | --- | --- | --- |
| Layer 0 | 6 つの LLM 役割の数学的機能必然性 | 用語境界公理 + 役割分離議論 | 形式定理ドメイン |
| Layer A | 有限義務グラフ定理 | 64 部分集合の全列挙 | 形式実行可能証明書 |
| Layer B | 既知の公開 LLM ファミリの Layer 0 への対応 | 公式参照と公開モデルファミリ証拠 | 公開証拠マッピング |
| Layer 1+ | Transformer/Dense/MoE/SSM/RWKV の枝配置 | 公開アーキテクチャ記述 | Layer 0 下層の実装枝 |

## Layer A 実行可能定理証明書

付録は 6 つの Layer-0 役割の 64 部分集合すべてを列挙し、宣言された義務が満たされるかを検査する。

期待結果：

```
layer_a_status = PROVEN_BY_EXHAUSTIVE_ENUMERATION_OF_DECLARED_OBLIGATION_GRAPH
full_set_pass = true
proper_subset_pass_count = 0
single_removal_fail_count = 6
```

これは宣言された義務グラフ上の有限数学的証明である。展開済み全モデルの経験的検査ではない。主張が形式的でありサーベイ的でないからである。

## なぜ 6 コンポーネントか

6 役割は、英語ラベルとして唯一可能なものだと主張しているわけではない。これらは LLM システムの運用に必要な、責任境界の最小集合である：

| 役割 | 境界 |
| --- | --- |
| TOKEN_OR_SYMBOL_SPACE | 表現境界 |
| CONTEXT_CONDITIONING_STATE | 推論状態境界 |
| LEARNED_PARAMETERIZED_TRANSFORM | 学習モデル対象境界 |
| CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE | 条件付き出力代替境界 |
| SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION | 訓練／適合境界 |
| DECODING_OR_EMISSION_INTERFACE | 運用放出境界 |

5 コンポーネント結合は責任境界を隠蔽する。7 以上への分割は Layer-0 ルートより下、実装精緻化に踏み込む。批判者は別の分解を提案してよいが、本定理を覆すには、より良い境界保存性をもつより厳しい最小分解、あるいは妥当な LLM 反例を提示しなければならない。

## 反例プロトコル

妥当な反例は以下を両方満たす必要がある：

1. 候補が通常の技術的用法において現代の Large Language Model であることを確立する；かつ
2. 少なくとも 1 つの Layer-0 役割と、その全機能等価物を欠いていることを確立する。

大規模学習された文脈言語モデリングを欠くシステムは LLM 反例ではない。それは別の AI ／ テキストシステムである。

## 異議方針

* 「定義依存だ」は反証ではない。数学定理は構成上、定義と公理に依存する。
* 「全モデルの経験的検査ではない」は反証ではない。定理は形式的であり、経験的証拠マッピングは Layer B の役割。
* 「将来のアーキテクチャは違うかもしれない」は反証ではない。LLM であれば 6 役割または等価物を実装しなければならない。実装しないなら別の AI クラスか、用語改訂を強制する。
* 「Large に固定パラメータ閾値はない」は反証ではない。`Large` は現代的技術スケール条件であり、定理の作動機構ではない。

## 何を主張しているか

* LLM ステータスは数学的に 6 つの Layer-0 役割または機能等価物を要求する。
* Transformer attention、MoE、RoPE、RMSNorm、SwiGLU、MLA、GQA は実装／性能の枝であり、Layer-0 ルートではない。
* Mamba/SSM および RWKV／再帰型言語モデルはアーキテクチャ非依存の Layer-0 枠組みを支持する。
* 公開の公式参照は用語境界を支持する。公開アーキテクチャ証拠は Layer B マッピングを支持する。

## 何を主張していないか

* 意識、理解、意味、エージェンシー、人間等価の推論は主張しない。
* クローズド重みの内部の経験的検査は主張しない。
* 6 つの英語ラベルが唯一可能な語彙だとは主張しない。
* Transformer、attention、MoE、RoPE、RMSNorm、SwiGLU、MLA、GQA が普遍的 LLM ルートだとは主張しない。

## 引用

本リポジトリを利用する場合は、[CITATION.cff](CITATION.cff) または上部の Zenodo DOI バッジ経由で引用してください。

## ライセンス

デュアルライセンス：コードは [MIT](LICENSE-MIT)、ドキュメント・仕様は [CC-BY-4.0](LICENSE-CC-BY-4.0)。

## 最終位置づけ

> 現代 Large Language Model の Layer-0 運用コアに対する、再現可能な数学的機能必然性定理および有限実行可能証明パッケージ。