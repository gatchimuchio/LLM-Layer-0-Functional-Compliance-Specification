# Official LLM Usage Reference Strength Matrix

This document is not an ISO-style standards table. It records why the Layer-0 definition is not a private author opinion. The target is a term-explication of convergent provider usage around Large Language Models.

| Provider | Reference strength | Public source role | Layer-0 implication | Limitation handled |
|---|---|---|---|---|
| OpenAI | Direct explanatory definition | Describes LLMs as text-to-text systems that predict following text. | Text input/output, context-conditioned continuation, learned language modeling. | Explanatory provider source, not a formal standards body. |
| Anthropic | Official family classification + training-context witness | Describes Claude as a family of large language models and discusses training on large data. | Large learned model family with language capability. | Classification and training context, not a standalone formal definition. |
| xAI | Direct official classification | Describes Grok as a family of Large Language Models. | Official LLM-family classification. | Classification source; architecture details are branch-level. |
| Google DeepMind | Language-model class witness + non-autoregressive boundary witness | Describes text diffusion as a new kind of language model for text generation and uses LLM terminology for factuality evaluation. | Language-model status is not restricted to autoregressive implementation. | Supports architecture independence; not a complete definition alone. |
| Meta | Direct explanatory definition + model-family witness | Describes LLaMA as taking word sequences and predicting next words to generate text. | Token/word sequence, context conditioning, conditional output surface, recursive generation. | Autoregressive example; does not limit all LLMs to that branch. |
| Mistral AI | Direct explanatory definition | Describes LLMs as AI trained to understand and generate human language, with statistical word/sentence prediction framing. | Learned language modeling, generation, and conditional linguistic output. | Provider help article, not a standards document. |
| DeepSeek-AI | Model-family witness + scale/training witness | Describes DeepSeek LLM as an advanced language model with 67B parameters trained on 2T tokens. | Large learned parameterized model trained over token-scale language data. | Model witness; not a universal definition source. |
| GLM / THUDM | Objective-diversity witness | Describes GLM as pretrained with an autoregressive blank-filling objective. | Sequence fitting can be blank-infilling or equivalent, not only next-token prediction. | GLM is a general language model witness; scale/frontier status is separate. |
| Qwen / Alibaba Cloud | Official model-family classification + scale witness | Introduces Qwen3 as a family of large language models with dense and MoE branches. | Official LLM-family classification across implementation branches. | Family witness; details vary by model member. |

## Consequence

The definition used in this repository is not: “the author says these six things are LLMs.”

It is: “major provider usage converges on large learned language-sequence systems; the six Layer-0 roles are the minimal functional decomposition of that convergent usage.”

A valid objection must therefore do more than say “definition.” It must either:

1. show that provider usage does not converge on this functional core; or
2. provide a contemporary system recognized as an LLM that lacks at least one Layer-0 role and every functional equivalent of that role.
