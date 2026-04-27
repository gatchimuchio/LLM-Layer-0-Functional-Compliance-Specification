# Official LLM Reference Bundle

## Purpose

This bundle addresses the objection: **"your LLM definition is just your opinion."**

The repository definition is not based on private preference. It is a term-explication of the convergent public usage of "Large Language Model" and "language model" across major LLM developers and maintainers.

The cited sources are official public sources from OpenAI, Anthropic, xAI, Google DeepMind, Meta, Mistral AI, DeepSeek-AI, GLM/THUDM, and Qwen/Alibaba Cloud. Short excerpts are included only to anchor the audit; use the URLs for full context.

## Cross-provider convergence

| Provider | Official source | Short official excerpt | Layer-0 implication |
|---|---|---|---|
| OpenAI | `https://developers.openai.com/cookbook/articles/how_to_work_with_large_language_models` | "map text to text" / "predicts the text" | text input/output, contextual prediction, learned sequence modeling |
| Anthropic | `https://www.anthropic.com/research/tracing-thoughts-language-model` | "trained on large amounts of data" | learned parameterized model, internal computation, linguistic output |
| xAI | `https://docs.x.ai/developers/introduction` | "Grok is a family of Large Language Models" | official LLM classification; Grok-1 separately documents large MoE scale |
| Google DeepMind | `https://deepmind.google/models/gemini-diffusion/` | "foundation of generative AI" | text generation remains the function even when generation mechanism changes |
| Meta | `https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct` | "sequence of words" / "predicts a next word" | linguistic sequence, context conditioning, conditional output surface |
| Mistral AI | `https://help.mistral.ai/en/articles/424368-what-s-a-large-language-model-llm` | "understand and generate human language" | learned language modeling and generation |
| DeepSeek-AI | `https://github.com/deepseek-ai/DeepSeek-LLM` | "67 billion parameters" / "2 trillion tokens" | large learned model trained on language tokens |
| GLM / THUDM | `https://github.com/THUDM/GLM` | "autoregressive blank-filling objective" | sequence fitting criterion can be next-token, infilling, or equivalent |
| Qwen / Alibaba Cloud | `https://github.com/QwenLM/Qwen3` | "large language model series" | official LLM family label; implementation branch is not root definition |

## Derived common core

Across these official sources, the common technical usage has the following shared structure:

1. The object is **large-scale** or high-capacity.
2. It is **learned/trained**, not merely hand-written rules.
3. It operates over **text, language, words, tokens, or linguistic sequences**.
4. It uses context or prompt-like input to produce, score, complete, or generate linguistic output.
5. It exposes output through text generation, scoring, completion, chat, API, or equivalent emission interface.

This is exactly what the six Layer-0 components formalize:

```text
TOKEN_OR_SYMBOL_SPACE
+ CONTEXT_CONDITIONING_STATE
+ LEARNED_PARAMETERIZED_TRANSFORM
+ CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE
+ SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION
+ DECODING_OR_EMISSION_INTERFACE
```

## Audit conclusion

The repository definition is not an authorial feeling. It is a formal decomposition of the convergent technical usage of "Large Language Model" across official source material.

A critic may still propose a different taxonomy, but a valid counterexample must show a system that is still an LLM in this contemporary technical usage while lacking at least one Layer-0 component and every functional equivalent of that component.


## Reference strength matrix

For source strength and coverage limits, see `docs/reference_strength_matrix.md`.
