# 6要素粒度の正当化

## 問い

なぜ5要素でも7要素でもなく、Layer 0 を6役割で置くのか。

## 答え

6役割は、唯一可能な語彙だとは主張しない。採用理由は、各役割が異なる責任境界を守っているためである。代替語彙を出すなら、この境界を保存するか、ある境界がLLM状態に不要であることを説明する必要がある。

## 6つの境界

| Component | 守る境界 | 冗長でない理由 |
|---|---|---|
| TOKEN_OR_SYMBOL_SPACE | 表現境界 | 言語的addressabilityがなければ、言語系列ドメインがない。 |
| CONTEXT_CONDITIONING_STATE | 推論状態境界 | 文脈条件がなければ、文脈非依存統計へ落ちる。 |
| LEARNED_PARAMETERIZED_TRANSFORM | 学習済みモデルオブジェクト境界 | 学習済み変換がなければ、ルール表、検索器、非汎化テキストツールになる。 |
| CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE | 条件付き候補境界 | これがなければ、textをencodeできても continuation/completion/scoring 候補を定義できない。 |
| SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION | 訓練・適合境界 | 言語系列適合がなければ、分類器、検索器、ranker、embedding modelになる。 |
| DECODING_OR_EMISSION_INTERFACE | 運用出力境界 | emission/scoring path がなければ、latent core や checkpoint tensor であって、運用LLM systemではない。 |

## 5要素統合テスト

| 統合案 | 失敗 |
|---|---|
| output surface + emission interface | 潜在的な条件付き候補と運用出力の差が潰れる。 |
| learned transform + fitting criterion | model object と training/fitting source の差が潰れる。 |
| token space + context state | representation と conditioning の差が潰れる。 |
| context state + output surface | 状態保持と条件付き候補選択の差が潰れる。 |

## 7要素以上への分割テスト

7要素以上は、実装詳細としては可能。たとえばTransformerでは learned transform を attention、MLP、normalization、residual path、order access、LM head に分けられる。だがそれは Layer 1 実装詳細であり、Layer 0 root ではない。

## 規則

- 実装固有分割なら Layer 0 より下に置く。
- 責任境界を潰す統合は Layer 0 として拒否する。
- 6境界を保存する代替語彙なら、本リポジトリと互換であり、反証ではない。

