# 公式LLM用例 Reference Bundle

## 目的

本資料は、想定反論 **「そのLLM定義はあなたの感想ではないか」** を処理するための一次情報束である。

本リポジトリの定義は私的な好みではない。OpenAI、Anthropic、xAI、Google DeepMind、Meta、Mistral AI、DeepSeek-AI、GLM/THUDM、Qwen/Alibaba Cloud の公式公開用例に共通する「Large Language Model / language model」の内包を、機能要件として展開したものである。

短い引用は監査アンカーであり、全文脈は各URLを参照する。

## 公式用例の収束

| Provider | 公式source | 短い公式表現 | Layer 0への含意 |
|---|---|---|---|
| OpenAI | `https://developers.openai.com/cookbook/articles/how_to_work_with_large_language_models` | "map text to text" / "predicts the text" | text入力/出力、文脈的予測、学習済み系列モデリング |
| Anthropic | `https://www.anthropic.com/research/tracing-thoughts-language-model` | "trained on large amounts of data" | 学習済みパラメータモデル、内部計算、言語出力 |
| xAI | `https://docs.x.ai/developers/introduction` | "Grok is a family of Large Language Models" | Grokを公式にLLM系列と分類。Grok-1では大規模MoEも別途明記 |
| Google DeepMind | `https://deepmind.google/models/gemini-diffusion/` | "foundation of generative AI" | generation mechanismが変わってもtext generationが機能対象 |
| Meta | `https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct` | "sequence of words" / "predicts a next word" | 言語系列、文脈条件、条件付き出力面 |
| Mistral AI | `https://help.mistral.ai/en/articles/424368-what-s-a-large-language-model-llm` | "understand and generate human language" | 学習済み言語モデリングと生成 |
| DeepSeek-AI | `https://github.com/deepseek-ai/DeepSeek-LLM` | "67 billion parameters" / "2 trillion tokens" | 大規模な学習済み言語tokenモデル |
| GLM / THUDM | `https://github.com/THUDM/GLM` | "autoregressive blank-filling objective" | 系列適合基準はnext-token、infilling、または同等物でよい |
| Qwen / Alibaba Cloud | `https://github.com/QwenLM/Qwen3` | "large language model series" | 公式にLLM familyとして位置づけ。実装分岐はroot定義ではない |

## 導出される共通核

公式用例から共通して抽出される技術的内包は以下である。

1. 対象は **大規模 / high-capacity** である。
2. 手書きルールではなく **学習済み / trained** である。
3. **text / language / word / token / linguistic sequence** を扱う。
4. context / prompt 的入力に条件付けられ、言語出力を生成・評価・補完する。
5. text generation、scoring、completion、chat、API、または同等の emission interface を持つ。

これは次の6要素に対応する。

```text
TOKEN_OR_SYMBOL_SPACE
+ CONTEXT_CONDITIONING_STATE
+ LEARNED_PARAMETERIZED_TRANSFORM
+ CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE
+ SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION
+ DECODING_OR_EMISSION_INTERFACE
```

## 監査結論

本リポジトリのLLM定義は著者の感想ではない。主要LLM開発元・公開元の公式用例に収束している技術的意味を、機能要件へ分解したものである。

批判者が別分類を提案することは可能だが、有効な反例にするには「現代技術語としてなおLLMである」かつ「Layer 0要素またはその機能同値物を欠く」ことを同時に示す必要がある。


## 参照強度マトリクス

参照強度と射程限界は `docs/reference_strength_matrix.ja.md` を参照。
