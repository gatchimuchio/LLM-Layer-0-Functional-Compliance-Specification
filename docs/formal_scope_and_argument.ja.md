# Formal Scope and Argument

## 定理の定義域

`LLM` を、現代技術用語としての大規模学習済み言語モデルのクラスとする。すなわち、言語トークン/記号系列に対して、文脈条件付きに、学習済みパラメータ変換を用い、条件付き言語出力候補を持ち、言語系列または同等の生成的text基準へ適合され、運用上のdecode/emission経路を持つシステムである。

この境界は、公式provider用例と公開model-family witnessによりアンカーされる。私的定義ではない。

## 定理

任意のシステム `S` について、`S` が定義域内の Large Language Model であるなら、`S` は以下6役割を明示的または機能同値的に必ず持つ。

1. `TOKEN_OR_SYMBOL_SPACE`
2. `CONTEXT_CONDITIONING_STATE`
3. `LEARNED_PARAMETERIZED_TRANSFORM`
4. `CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE`
5. `SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION`
6. `DECODING_OR_EMISSION_INTERFACE`

## 証明スケッチ

`S` がLLMであると仮定する。6役割のうち任意の1つを除去する。

- token/symbol space がなければ、`S` は言語系列上で動作しない。
- context conditioning がなければ、prompt/sequence条件付き言語モデリングではない。
- learned parameterized transform がなければ、LLM coreではなくtable/rule/retrieval systemである。
- conditional linguistic output surface がなければ、生成・補完・採点・選択のための言語候補を定義できない。
- sequence-modelingまたは同等fitting criterionがなければ、言語系列モデルとして訓練/適合されていない。
- decoding/emission interfaceがなければ、運用LLM systemとして観測可能な言語出力経路を持たない。

各除去はLLM状態を崩すか、候補を別種のAI/text-systemへ移す。したがって6役割はすべて必要である。

A層はさらに、全64部分集合の全列挙により有限義務グラフを証明する。全義務を満たすのはfull setのみである。

## 反例条件

有効な反例は、LLMであり、かつ少なくとも1つの役割と全機能同値物を欠く必要がある。それ以外は分類論争、実装差、または非LLM systemである。
