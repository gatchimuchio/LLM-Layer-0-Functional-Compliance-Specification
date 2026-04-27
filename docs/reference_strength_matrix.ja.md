# 公式LLM用例：参照強度マトリクス

本ドキュメントはISO規格表ではない。目的は、Layer 0定義が著者の私的感想ではなく、主要providerの公式用例に収束する技術的意味を用語展開したものだと示すことである。

| Provider | 参照強度 | 公開ソース上の役割 | Layer 0への含意 | 処理済みの限界 |
|---|---|---|---|---|
| OpenAI | 直接的な説明定義 | LLMをtext-to-text system、後続text予測として説明。 | text入出力、文脈条件付き継続、学習済み言語モデリング。 | provider説明であり、標準化団体の定義ではない。 |
| Anthropic | 公式family分類 + training context witness | Claudeをlarge language modelsのfamilyとして説明し、大規模データ訓練にも言及。 | 大規模学習済みモデルfamilyと言語能力。 | 分類・訓練文脈であり、単独の形式定義ではない。 |
| xAI | 直接的な公式分類 | GrokをLarge Language Modelsのfamilyと説明。 | 公式LLM family分類。 | 分類ソースであり、architecture詳細は下位branch。 |
| Google DeepMind | language-model class witness + 非自己回帰境界witness | text diffusionをtext generationのための新しいlanguage modelと説明し、LLM factuality評価でもLLM語を使用。 | language model性はautoregressive実装に限定されない。 | architecture非依存性の補強であり、単独の完全定義ではない。 |
| Meta | 直接的な説明定義 + model-family witness | LLaMAをword sequence入力、next word予測、text生成として説明。 | token/word sequence、context conditioning、conditional output surface、recursive generation。 | autoregressive例であり、全LLMをそのbranchに限定しない。 |
| Mistral AI | 直接的な説明定義 | LLMをhuman languageを理解・生成するよう訓練されたAI、word/sentence predictionを行う統計モデルとして説明。 | 学習済み言語モデリング、生成、条件付き言語出力。 | provider help記事であり、標準規格ではない。 |
| DeepSeek-AI | model-family witness + scale/training witness | DeepSeek LLMを67B parameters・2T tokensで訓練されたadvanced language modelとして説明。 | 大規模学習済みパラメータモデル、token-scale training、sequence modeling。 | model witnessであり、普遍定義ソースではない。 |
| GLM / THUDM | objective-diversity witness | GLMをautoregressive blank-filling objectiveで事前学習されたGeneral Language Modelとして説明。 | sequence fitting criterionはnext-tokenに限らずblank-infilling等も含む。 | GLMはgeneral language model witnessであり、scale/frontier性は別論点。 |
| Qwen / Alibaba Cloud | 公式model-family分類 + scale witness | Qwen3をlarge language modelsのfamilyとして紹介し、dense/MoE branchを含む。 | 公式LLM family分類。実装branchとLayer 0定義は別。 | family witnessであり、詳細はモデルmemberごとに異なる。 |

## 帰結

本リポジトリの定義は、以下ではない。

> 著者が「これをLLMと呼ぶ」と決めた。

正しくは以下である。

> 主要providerの公式用例は、大規模・学習済み・言語系列システムへ収束しており、その共通核を6つのLayer 0機能役割へ分解している。

したがって、「定義だから」という批判だけでは足りない。有効な批判には、少なくとも以下のどちらかが必要である。

1. provider用例がこの機能核へ収束していないことを示す。
2. 現代技術語としてLLMと認められる具体システムが、Layer 0役割の少なくとも1つとその全機能同値物を欠くことを示す。
