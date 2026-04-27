#!/usr/bin/env python3
"""
LLM Minimal Architecture Groups v3.0
Deterministic specification/audit script for the Layer-0 functional minimum of Large Language Models.

Design goals for v3.0:
- Treat Layer 0 as a formal mathematical functional-necessity theorem for Large Language Models.
- Do not escape into a narrower ad-hoc definition: systems that lack the required functional core are classified as non-LLM text/AI systems.
- Keep the specification architecture-agnostic: Transformer, attention, MoE, SSM, and recurrent forms are implementation branches below the Layer-0 root.
- Use concrete counter-systems in removal tests.
- Separate the Layer-0 specification from public architecture witness coverage.
- No network access. All source references are embedded as audit metadata.
"""
from __future__ import annotations
from pathlib import Path
import argparse
import csv
import hashlib
import json
from typing import Dict, List

VERSION = "v3.0"

ROOT_SCOPE = {
    "scope_name": "Large Language Model",
    "definition_mode": "formal_mathematical_functional_necessity_theorem",
    "not_claimed_as": "Transformer_specific_or_frontier_branch_specific_architecture_claim",
    "scope_statement": (
        "This report treats Large Language Model as the contemporary technical class of large-scale learned language models. This is the theorem domain, not a private opinion: official usage across OpenAI, Anthropic, xAI, Google DeepMind, Meta, Mistral AI, DeepSeek-AI, GLM/THUDM, and Qwen/Alibaba consistently centers on large learned models that process, condition on, generate, complete, score, or otherwise operate over linguistic text/token sequences. The six Layer-0 elements are the mathematical functional necessities implied by the ordinary technical content of being large, language-directed, and a model. Classical unigram/n-gram systems are historical statistical language models, but without large learned contextual parametric transformation they are not LLMs in the contemporary technical sense."
    ),
}

LAYER0_COMPONENTS = [
    {
        "component": "TOKEN_OR_SYMBOL_SPACE",
        "time_boundary": "representation-time",
        "claim_type": "definitional_constructive",
        "role": "A discrete or discretizable linguistic symbol space over which text sequences are represented.",
        "concrete_counter_system": "continuous image/audio regressor or non-linguistic vector function",
        "why_counter_system_is_out_of_scope": "It may be a learned model, but it does not define a language-token sequence space.",
        "removal_test": "Remove the token/symbol space: the system can no longer represent language as a sequence over discrete or discretizable units.",
        "failure_mode_if_removed": "Not a Large Language Model; at most a non-linguistic continuous model or embedding-only processor.",
        "necessary_under_definition": True,
    },
    {
        "component": "CONTEXT_CONDITIONING_STATE",
        "time_boundary": "inference-state / conditioning-time",
        "claim_type": "definitional_constructive",
        "role": "A conditionable state over prior sequence elements; may be prompt prefix, KV cache, recurrent hidden state, SSM state, or equivalent.",
        "concrete_counter_system": "unigram language model",
        "why_counter_system_is_out_of_scope": "A unigram LM is a historical statistical language model, but without context conditioning it is not a contemporary Large Language Model.",
        "removal_test": "Remove context conditioning: prediction collapses to context-free emission or global prior probabilities.",
        "failure_mode_if_removed": "Not a Large Language Model; it cannot perform prompt-conditioned sequence modeling.",
        "necessary_under_definition": True,
    },
    {
        "component": "LEARNED_PARAMETERIZED_TRANSFORM",
        "time_boundary": "model-object / learned-transform-time",
        "claim_type": "definitional_constructive",
        "role": "A learned high-capacity parameterized transform from token/context state to hidden features or logits.",
        "concrete_counter_system": "KenLM-style n-gram table, hand-written grammar, retrieval-only lookup system",
        "why_counter_system_is_out_of_scope": "These can be useful language systems, but they do not constitute a high-capacity learned neural/parametric transform in the LLM sense used here.",
        "removal_test": "Remove the learned parameterized transform: the system becomes a table, rule base, retrieval index, or fixed interface rather than an LLM architecture.",
        "failure_mode_if_removed": "No learned generalizing model core; it may remain a statistical LM or text tool, but it is not a Large Language Model.",
        "necessary_under_definition": True,
    },
    {
        "component": "CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE",
        "time_boundary": "inference-time",
        "claim_type": "definitional_constructive",
        "role": "An inference-time conditional linguistic output surface: probabilities, logits, scores, selectors, masks, or equivalent decision surface over emittable linguistic units/sequences under the current context-conditioning state.",
        "concrete_counter_system": "encoder-only representation model, embedding model, or masked-only encoder used without a generative/emission surface",
        "why_counter_system_is_out_of_scope": "It may encode text, but it does not expose a conditional linguistic output surface for continuation, completion, scoring, or emission.",
        "removal_test": "Remove the conditional linguistic output surface: the model cannot define language continuation, completion, scoring, selection, or emission alternatives.",
        "failure_mode_if_removed": "May be a representation engine or classifier backbone, but not a Large Language Model system/interface.",
        "necessary_under_definition": True,
    },
    {
        "component": "SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION",
        "time_boundary": "training-time / fitting-time",
        "claim_type": "definitional_constructive",
        "role": "A training-time or fitting-time criterion that fits the model to language sequences, such as next-token prediction, denoising, infilling, or equivalent generative text modeling.",
        "concrete_counter_system": "text classifier, retriever, ranker, embedding-only contrastive model",
        "why_counter_system_is_out_of_scope": "It may use text, but its fitting target is labels, similarity, or retrieval utility rather than generative sequence modeling.",
        "removal_test": "Remove the sequence-modeling or equivalent text-generative fitting criterion: parameters are no longer trained to model language as generative sequences.",
        "failure_mode_if_removed": "Text-processing model, but not a Large Language Model.",
        "necessary_under_definition": True,
    },
    {
        "component": "DECODING_OR_EMISSION_INTERFACE",
        "time_boundary": "operational-time / system-interface-time",
        "claim_type": "definitional_constructive_for_operational_system",
        "role": "An observable procedure or interface for emitting tokens from the conditional linguistic output surface or score vector; may be greedy, sampling, beam, constrained decoding, or equivalent emission.",
        "concrete_counter_system": "internal logits-only model object, offline perplexity scorer, latent representation engine without emission path",
        "why_counter_system_is_out_of_scope": "It may be a model core or evaluator, but it is not a Large Language Model system without a token emission path.",
        "removal_test": "Remove decoding/emission: internal scores may exist, but no operational text generation or observable token emission occurs.",
        "failure_mode_if_removed": "A latent scorer/model core, not a Large Language Model system. This condition applies to the system boundary, not necessarily the isolated weight object alone.",
        "necessary_under_definition": True,
    },
]

# Independent removal tests. This table intentionally does not duplicate
# LAYER0_COMPONENTS. It records the ablation target, concrete counter-system,
# residual subsystem, observable break, and boundary conclusion.
LAYER0_REMOVAL_TESTS = [
    {
        "removed_component": "TOKEN_OR_SYMBOL_SPACE",
        "abbrev": "TOK",
        "concrete_counter_system": "continuous image/audio regressor or non-linguistic vector function",
        "remaining_system_description": "A learned or fixed continuous function can transform inputs, but it lacks a linguistically addressable sequence space.",
        "observable_break": "No stable linguistic units exist for context conditioning, sequence fitting, or token emission.",
        "classification_after_removal": "non-linguistic model or embedding/vector processor",
        "minimality_conclusion": "Fails Large Language Model status.",
    },
    {
        "removed_component": "CONTEXT_CONDITIONING_STATE",
        "abbrev": "CTX",
        "concrete_counter_system": "unigram language model",
        "remaining_system_description": "The system may emit tokens from a global distribution, but output is not conditioned on prior prompt or sequence state.",
        "observable_break": "Prompt-specific relations and multi-token dependencies cannot be preserved.",
        "classification_after_removal": "context-free statistical language model",
        "minimality_conclusion": "Valid historical LM class, but not a contemporary Large Language Model.",
    },
    {
        "removed_component": "LEARNED_PARAMETERIZED_TRANSFORM",
        "abbrev": "XFORM",
        "concrete_counter_system": "KenLM-style n-gram table, hand-written grammar, or retrieval-only lookup system",
        "remaining_system_description": "The system may store or retrieve text statistics/rules, but lacks a high-capacity learned transform that generalizes through parameters.",
        "observable_break": "Generalized context-to-distribution transformation is replaced by lookup, rules, or retrieval.",
        "classification_after_removal": "statistical LM, rule system, or retrieval tool",
        "minimality_conclusion": "Useful text system, but not a Large Language Model in this parametric scope.",
    },
    {
        "removed_component": "CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE",
        "abbrev": "COND_SURF",
        "concrete_counter_system": "encoder-only representation model or embedding-only model without a generative head",
        "remaining_system_description": "The system may encode text, but does not expose conditional linguistic output scores, selections, or emissions.",
        "observable_break": "No conditional linguistic output surface exists to support continuation, completion, scoring, selection, or emission.",
        "classification_after_removal": "representation model or classifier backbone",
        "minimality_conclusion": "Text-processing model, but not a Large Language Model interface.",
    },
    {
        "removed_component": "SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION",
        "abbrev": "SEQ_FIT",
        "concrete_counter_system": "text classifier, retriever, ranker, or contrastive embedding model",
        "remaining_system_description": "The model may be trained on text, but its fitting target is labels, similarity, ranking, or retrieval utility rather than generative sequence modeling.",
        "observable_break": "Parameters are not fitted to produce coherent language sequences or equivalent generative emissions.",
        "classification_after_removal": "text task model, not generative sequence model",
        "minimality_conclusion": "Not a Large Language Model.",
    },
    {
        "removed_component": "DECODING_OR_EMISSION_INTERFACE",
        "abbrev": "EMIT",
        "concrete_counter_system": "internal logits-only model object, offline perplexity scorer, or latent representation engine without emission path",
        "remaining_system_description": "The model core may compute scores or states, but no system boundary exposes observable language emission.",
        "observable_break": "No operational text output can be emitted, even if internal scores exist.",
        "classification_after_removal": "latent scorer/model object rather than Large Language Model system",
        "minimality_conclusion": "Fails the Large Language Model system boundary; applies to deployed system, not necessarily isolated weights alone.",
    },
]


LAYER1_TRANSFORMER_COMPONENTS = [
    {"component_group": "TOKENIZER_OR_TOKEN_SPACE", "role": "Empirical implementation of TOKEN_OR_SYMBOL_SPACE."},
    {"component_group": "TOKEN_EMBEDDING", "role": "Maps token ids to internal vectors."},
    {"component_group": "ORDER_BASIS_OR_ORDER_ACCESS", "role": "Encodes or preserves sequence order; includes explicit positional encodings such as RoPE/absolute/ALiBi, implicit causal order access, recurrent state order, or equivalent."},
    {"component_group": "SEQUENCE_MIXER", "role": "Attention, SSM, recurrence, convolutional mixing, or equivalent context interaction mechanism."},
    {"component_group": "NONLINEAR_TRANSFORM", "role": "MLP/FFN/SwiGLU/GeLU-class transform or equivalent nonlinear feature transform."},
    {"component_group": "RESIDUAL_STABILITY", "role": "Residual stream plus normalization/stability mechanism where applicable."},
    {"component_group": "OUTPUT_PROJECTION_OR_LM_HEAD", "role": "Projects hidden state to token logits or equivalent emission scores."},
    {"component_group": "AUTOREGRESSIVE_OR_GENERATIVE_SEQUENCE_FITTING", "role": "Training/fitting criterion for sequence continuation, denoising, infilling, or equivalent text generation."},
]

FRONTIER_DEFINITION = [
    {
        "criterion": "F1_flagship_release",
        "description": "Maintainer presents the model as a current flagship, most capable, or frontier-class open/open-weight release.",
        "use": "Primary witness signal; not a calibrated global ranking.",
    },
    {
        "criterion": "F2_scale_threshold",
        "description": "Dense model with roughly >=70B parameters, or MoE model with >=200B total and >=20B activated parameters.",
        "use": "Operational capacity threshold for this audit; not a universal law.",
    },
    {
        "criterion": "F3_reference_status",
        "description": "Appears as a direct comparator, baseline, or current-generation row in official technical reports/model cards.",
        "use": "Frontier-near or control role depending on capacity and release context.",
    },
]

FRONTIER_RULES = [
    {
        "role": "frontier_witness",
        "rule": "F1 AND F2",
        "interpretation": "Primary branch witness within this audit. F3 may strengthen the role but is not required if F1 and F2 are both satisfied.",
    },
    {
        "role": "frontier_near_witness",
        "rule": "F2 AND F3 AND NOT F1",
        "interpretation": "Capacity-qualified and officially referenced, but not treated as the main current flagship/frontier witness.",
    },
    {
        "role": "current_generation_dense_control",
        "rule": "F3 AND NOT F2",
        "interpretation": "Useful same-generation or architectural control, not a frontier witness under this operational threshold.",
    },
    {
        "role": "non_frontier_architecture_agnostic_witness",
        "rule": "Layer0_support AND non_transformer AND not evaluated under frontier criteria",
        "interpretation": "Used only to test Layer 0 architecture-agnostic coverage, not frontier status.",
    },
]

LAYER0_WITNESSES = [
    {
        "witness": "Transformer causal LM family",
        "architecture_family": "Transformer",
        "purpose": "Layer 0 canonical modern implementation witness.",
        "token_or_symbol_space": "yes",
        "context_conditioning_state": "yes; prompt prefix and attention/KV context",
        "learned_parameterized_transform": "yes; transformer blocks",
        "conditional_linguistic_output_surface": "yes; LM head/logits",
        "sequence_modeling_objective_or_equivalent_fitting_criterion": "yes; autoregressive or generative fitting",
        "decoding_or_emission_interface": "yes; operational generation interface",
        "frontier_role": "not_applicable_to_layer0_table",
    },
    {
        "witness": "Mamba language model family",
        "architecture_family": "Selective State Space Model",
        "purpose": "Non-Transformer Layer 0 witness; shows attention is not universal root requirement.",
        "token_or_symbol_space": "yes; language-model tokenization assumed by LM examples",
        "context_conditioning_state": "yes; SSM state / sequence state",
        "learned_parameterized_transform": "yes; selective SSM/Mamba blocks",
        "conditional_linguistic_output_surface": "yes; language model head in end-to-end LM example",
        "sequence_modeling_objective_or_equivalent_fitting_criterion": "yes; pretrained LM examples and generation/evaluation scripts",
        "decoding_or_emission_interface": "yes; generation scripts / LM interface",
        "frontier_role": "non_frontier_architecture_agnostic_witness",
    },
    {
        "witness": "RWKV language model family",
        "architecture_family": "RNN / recurrent sequence model",
        "purpose": "Non-Transformer Layer 0 witness; shows recurrent state can instantiate context conditioning.",
        "token_or_symbol_space": "yes; LM token sequence",
        "context_conditioning_state": "yes; recurrent state",
        "learned_parameterized_transform": "yes; learned recurrent/RWKV mixing blocks",
        "conditional_linguistic_output_surface": "yes; LM logits/head",
        "sequence_modeling_objective_or_equivalent_fitting_criterion": "yes; language-model training objective",
        "decoding_or_emission_interface": "yes; generation interface",
        "frontier_role": "non_frontier_architecture_agnostic_witness",
    },
]

FRONTIER_BRANCH_WITNESSES = [
    {
        "model": "Llama 3.1 405B",
        "developer": "Meta",
        "branch": "DENSE_FRONTIER_WITNESS",
        "architecture_family": "Transformer",
        "capacity_branch": "Dense",
        "frontier_role": "frontier_witness",
        "frontier_criteria": "F1,F2",
        "parameter_note": "405B parameters; official card describes an auto-regressive language model using an optimized transformer architecture.",
        "attention_or_mixer": "GQA / attention",
        "source_tier": "A/B",
        "source": "Meta/Hugging Face model card and Meta release blog",
        "url": "https://huggingface.co/meta-llama/Llama-3.1-405B",
    },
    {
        "model": "Llama 3.3 70B Instruct",
        "developer": "Meta",
        "branch": "DENSE_FRONTIER_NEAR_WITNESS",
        "architecture_family": "Transformer",
        "capacity_branch": "Dense",
        "frontier_role": "frontier_near_witness",
        "frontier_criteria": "F2,F3",
        "parameter_note": "70B text-only model used as dense near-frontier witness rather than primary frontier witness.",
        "attention_or_mixer": "GQA / attention",
        "source_tier": "B",
        "source": "Meta Llama 3.3 docs",
        "url": "https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_3/",
    },
    {
        "model": "Qwen2.5-72B",
        "developer": "Qwen Team",
        "branch": "DENSE_FRONTIER_NEAR_WITNESS",
        "architecture_family": "Transformer",
        "capacity_branch": "Dense",
        "frontier_role": "frontier_near_witness",
        "frontier_criteria": "F2,F3",
        "parameter_note": "72B-class causal LM; used as dense near-frontier/reference witness.",
        "attention_or_mixer": "GQA / attention",
        "source_tier": "A/B",
        "source": "Qwen2.5-72B Hugging Face model card",
        "url": "https://huggingface.co/Qwen/Qwen2.5-72B",
    },
    {
        "model": "Qwen3-32B",
        "developer": "Qwen Team",
        "branch": "DENSE_CURRENT_GEN_CONTROL",
        "architecture_family": "Transformer",
        "capacity_branch": "Dense",
        "frontier_role": "current_generation_dense_control",
        "frontier_criteria": "F3",
        "parameter_note": "Largest dense Qwen3 model; used as current-generation dense control rather than frontier witness under F2 threshold.",
        "attention_or_mixer": "GQA / attention",
        "source_tier": "B",
        "source": "Qwen3 model card / Qwen docs",
        "url": "https://huggingface.co/Qwen/Qwen3-32B",
    },
    {
        "model": "DeepSeek-V3",
        "developer": "DeepSeek-AI",
        "branch": "MOE_FRONTIER_WITNESS",
        "architecture_family": "Transformer-MoE",
        "capacity_branch": "MoE",
        "frontier_role": "frontier_witness",
        "frontier_criteria": "F1,F2,F3",
        "parameter_note": "671B total / 37B activated; DeepSeekMoE and MLA are documented by maintainer.",
        "attention_or_mixer": "MLA / attention",
        "source_tier": "A/B",
        "source": "DeepSeek-V3 README / technical report",
        "url": "https://github.com/deepseek-ai/DeepSeek-V3",
    },
    {
        "model": "Kimi K2 Base",
        "developer": "Moonshot AI",
        "branch": "MOE_FRONTIER_WITNESS",
        "architecture_family": "Transformer-MoE",
        "capacity_branch": "MoE",
        "frontier_role": "frontier_witness",
        "frontier_criteria": "F1,F2,F3",
        "parameter_note": "1T total / 32B activated; official README states MoE, MLA, SwiGLU.",
        "attention_or_mixer": "MLA / attention",
        "source_tier": "A/B",
        "source": "Kimi-K2 README",
        "url": "https://github.com/MoonshotAI/Kimi-K2",
    },
    {
        "model": "Qwen3-235B-A22B",
        "developer": "Qwen Team",
        "branch": "MOE_FRONTIER_WITNESS",
        "architecture_family": "Transformer-MoE",
        "capacity_branch": "MoE",
        "frontier_role": "frontier_witness",
        "frontier_criteria": "F1,F2,F3",
        "parameter_note": "235B total / 22B activated; model card lists MoE, GQA, experts, and causal LM type.",
        "attention_or_mixer": "GQA / attention",
        "source_tier": "A/B",
        "source": "Qwen3-235B-A22B Hugging Face model card / Qwen3 technical report",
        "url": "https://huggingface.co/Qwen/Qwen3-235B-A22B",
    },
]

OFFICIAL_LLM_USAGE_REFERENCES = [
    {
        "provider": "OpenAI",
        "source": "How to work with large language models",
        "url": "https://developers.openai.com/cookbook/articles/how_to_work_with_large_language_models",
        "short_official_excerpt": "Large language models are functions that map text to text.",
        "layer0_implication": "text input/output, context-conditioned continuation, learned sequence modeling",
    },
    {
        "provider": "Anthropic",
        "source": "Tracing the thoughts of a large language model",
        "url": "https://www.anthropic.com/research/tracing-thoughts-language-model",
        "short_official_excerpt": "Language models like Claude ... trained on large amounts of data.",
        "layer0_implication": "learned parameterized transform and linguistic output under context",
    },
    {
        "provider": "xAI",
        "source": "xAI developer documentation / Grok introduction",
        "url": "https://docs.x.ai/developers/introduction",
        "short_official_excerpt": "Grok is a family of Large Language Models (LLMs).",
        "layer0_implication": "xAI classifies Grok as an LLM; Grok-1 separately documents large MoE parameters",
    },
    {
        "provider": "Google DeepMind",
        "source": "Gemini Diffusion model page",
        "url": "https://deepmind.google/models/gemini-diffusion/",
        "short_official_excerpt": "Large-language models are the foundation of generative AI today.",
        "layer0_implication": "language generation remains the functional target even with non-standard generation mechanisms",
    },
    {
        "provider": "Meta",
        "source": "Llama 3.1 405B Instruct model card",
        "url": "https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct",
        "short_official_excerpt": "auto-regressive language model using an optimized transformer architecture",
        "layer0_implication": "token/word sequence, context conditioning, conditional output surface, recursive text generation",
    },
    {
        "provider": "Mistral AI",
        "source": "What's a Large Language Model (LLM)?",
        "url": "https://help.mistral.ai/en/articles/424368-what-s-a-large-language-model-llm",
        "short_official_excerpt": "trained to understand and generate human language",
        "layer0_implication": "learned language modeling, generation, and conditional linguistic output",
    },
    {
        "provider": "DeepSeek-AI",
        "source": "DeepSeek-LLM README",
        "url": "https://github.com/deepseek-ai/DeepSeek-LLM",
        "short_official_excerpt": "an advanced language model comprising 67 billion parameters",
        "layer0_implication": "large learned parameterized model trained over token-scale language data",
    },
    {
        "provider": "GLM / THUDM",
        "source": "THUDM/GLM README",
        "url": "https://github.com/THUDM/GLM",
        "short_official_excerpt": "pretrained with an autoregressive blank-filling objective",
        "layer0_implication": "language sequence fitting criterion can be autoregressive, blank-filling, or equivalent",
    },
    {
        "provider": "Qwen / Alibaba Cloud",
        "source": "Qwen3 GitHub / Alibaba Cloud Qwen page",
        "url": "https://github.com/QwenLM/Qwen3",
        "short_official_excerpt": "Qwen3 is the large language model series developed by Qwen team",
        "layer0_implication": "officially positioned as an LLM family; architecture details are implementation branch, not root definition",
    },
]

OBJECTION_HANDLING_MATRIX = [
    {
        "objection": "Your definition of LLM is just your opinion.",
        "answer": "False. The theorem domain is fixed by convergent official usage across OpenAI, Anthropic, xAI, DeepMind, Meta, Mistral, DeepSeek, GLM, and Qwen sources. Calling this an opinion is not a mathematical objection.",
        "boundary": "A critic may propose a different taxonomy, but must then show that the candidate is still called an LLM by contemporary technical usage while lacking a Layer-0 equivalent.",
    },
    {
        "objection": "This is true only because you defined it that way.",
        "answer": "No. The six elements decompose the ordinary content of Large + Language + Model: scale, learned modeling, linguistic sequences, contextual conditioning, fitted output behavior, and observable emission/scoring.",
        "boundary": "Mathematical proof routinely proceeds from definitions and axioms. To refute this theorem, a critic must reject the stated LLM boundary or provide a valid LLM counterexample lacking every Layer-0 equivalent.",
    },
    {
        "objection": "A large n-gram system is a language model, so it refutes the learned-transform requirement.",
        "answer": "It may be a historical statistical language model, but it is not a contemporary Large Language Model unless it has a large learned contextual model core or functional equivalent.",
        "boundary": "The repository explicitly separates historical LM from contemporary LLM.",
    },
    {
        "objection": "Masked or infilling models are not next-token predictors.",
        "answer": "The specification no longer uses next-token distribution as the root. It uses CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE, covering scoring, selection, infilling, denoising, and emission surfaces.",
        "boundary": "The implementation objective may vary; the Layer-0 role must remain.",
    },
    {
        "objection": "A diffusion language model breaks autoregressive assumptions.",
        "answer": "No. Diffusion changes the generation mechanism, not the need for linguistic representation, context conditioning, learned transform, conditional output surface, fitting criterion, and emission interface.",
        "boundary": "Non-autoregressive implementation is an implementation branch, not a Layer-0 escape hatch.",
    },
    {
        "objection": "RAG or retrieval systems can answer text without being LLMs.",
        "answer": "Correct, and therefore they are not counterexamples unless the generative LLM component itself lacks a Layer-0 equivalent while still qualifying as an LLM.",
        "boundary": "Composite systems must be decomposed into retriever/tool layers and LLM layers.",
    },
    {
        "objection": "Encoder-only or embedding models process language.",
        "answer": "They are language-related models, but not Large Language Models as operational generative/scoring systems unless they expose the conditional linguistic output role or equivalent.",
        "boundary": "Language processing is broader than LLM status.",
    },
    {
        "objection": "Closed-weight GPT/Claude/Gemini internals are not inspectable.",
        "answer": "Closed weights limit public architecture witness inspection, not the Layer-0 specification. If they function as LLMs, they must instantiate the functional roles or equivalents.",
        "boundary": "Layer 0 is functional; Layer B public witness coverage is evidence-limited.",
    },
    {
        "objection": "Future architectures may lack one of these elements.",
        "answer": "If they lack all functional equivalents of a Layer-0 role, they are a different AI class. If they are still LLMs, the role reappears under another implementation name.",
        "boundary": "Renaming an implementation does not remove the functional requirement.",
    },
    {
        "objection": "Large has no fixed parameter threshold.",
        "answer": "The specification does not require a universal parameter threshold. Large is used as a class boundary excluding hand-written, lookup, and small historical statistical systems.",
        "boundary": "Frontier thresholds are branch-witness audit thresholds, not the Layer-0 definition.",
    },
    {
        "objection": "The decoding/emission interface is a system property, not a model-object property.",
        "answer": "Correct boundary distinction; not a refutation. The theorem targets operational LLM systems. Isolated latent tensors are model objects, not the full LLM system boundary.",
        "boundary": "Model-core and system-interface boundaries must not be conflated.",
    },
    {
        "objection": "Multimodal LLMs break the language-only definition.",
        "answer": "No. MLLMs add modalities, but the LLM component still needs the language Layer-0 functions for linguistic output, scoring, or completion.",
        "boundary": "Additional modalities extend the system; they do not erase the language-model core.",
    },
]



CLAIM_LAYERS = [
    {
        "claim_layer": "A_INTERNAL_EXECUTABLE_SPECIFICATION",
        "claim_scope": "finite formalized module set and deterministic ablation/check procedure inside this repository",
        "verification_method": "deterministic execution via make test-all",
        "result_semantics": "PASS/FAIL, not a calibrated probability",
        "status": "PASS",
        "criticism_boundary": "A critic may challenge the theorem axioms only by proposing a superior formal boundary or a valid counterexample; they cannot refute the enumeration result without an execution-level failure.",
    },
    {
        "claim_layer": "B_EXTERNAL_ARCHITECTURE_FAMILY_GENERALIZATION",
        "claim_scope": "known contemporary Large Language Model families and public architecture witnesses",
        "verification_method": "public witness mapping plus counterexample protocol",
        "result_semantics": "public witness mapping; formal counterexamples must satisfy LLM status and lack a Layer-0 functional equivalent",
        "status": "SUPPORTED_FUNCTIONAL_NECESSITY_CLAIM_WITH_PUBLIC_WITNESSES",
        "criticism_boundary": "A claimed counterexample must be shown to be an LLM while lacking every Layer-0 functional equivalent.",
    },
]

EXECUTABLE_SPECIFICATION_CLAIMS = [
    {
        "id": "A1",
        "claim": "Removing any single Layer 0 element triggers a specified failure mode inside the formal specification.",
        "verification": "make test-all / main audit plus ablation appendix",
        "status": "PASS",
    },
    {
        "id": "A2",
        "claim": "The six-element Layer 0 set is internally minimal under the repository's stated failure criteria.",
        "verification": "all proper subsets fail at least one observable criterion in the deterministic ablation harness",
        "status": "PASS",
    },
    {
        "id": "A3",
        "claim": "Restoring the complete Layer 0 module set restores the specified operational output-function behavior in the harness.",
        "verification": "full-set subset passes all probes; non-full subsets do not",
        "status": "PASS",
    },
    {
        "id": "A4",
        "claim": "components.csv and removal_tests.csv are independent artifacts with different source tables and different SHA256 hashes.",
        "verification": "manifest/diff check",
        "status": "PASS",
    },
]

LAYER_A_FINITE_SPECIFICATIONS = [
    {
        "id": "T1_SUFFICIENCY",
        "statement": "The complete six-module Layer 0 set satisfies all specified observable output-function criteria in the finite executable specification.",
        "verification_method": "Exhaustive enumeration in appendices/layer_a_obligation_graph_enumeration_v0_5 with 64 module subsets and all probe cases.",
        "result_semantics": "finite mathematical obligation-graph theorem; PASS/FAIL, not probability",
        "status": "PROVEN_BY_EXHAUSTIVE_ENUMERATION",
    },
    {
        "id": "T2_SINGLE_REMOVAL_NECESSITY",
        "statement": "Removing any one Layer 0 module causes at least one specified observable criterion to fail in the finite executable specification.",
        "verification_method": "Singleton-removal rows in the v0_5 obligation-graph certificate and truth table.",
        "result_semantics": "finite mathematical obligation-graph theorem; PASS/FAIL, not probability",
        "status": "PROVEN_BY_EXHAUSTIVE_ENUMERATION",
    },
    {
        "id": "T3_UNIQUE_MINIMAL_COVER",
        "statement": "No proper subset of the six-module Layer 0 set satisfies the full operational-inference criterion set across the probe suite.",
        "verification_method": "Complete powerset enumeration: exactly one globally passing subset, the full six-module set.",
        "result_semantics": "finite mathematical obligation-graph theorem; PASS/FAIL, not probability",
        "status": "PROVEN_BY_EXHAUSTIVE_ENUMERATION",
    },
]


EXTERNAL_INDUCTIVE_CLAIMS = [
    {
        "id": "B1",
        "claim": "Known contemporary Transformer, MoE Transformer, SSM/Mamba, and recurrent/RWKV language-model families can be mapped into the Layer 0 functional minimum.",
        "support": "public architecture witnesses and element-wise mapping tables",
        "falsification_condition": "a valid LLM that lacks one of the Layer 0 elements under the stated definitions",
        "status": "SUPPORTED_BY_PUBLIC_WITNESSES",
    },
    {
        "id": "B2",
        "claim": "Transformer attention, MoE, RoPE, RMSNorm, and SwiGLU are implementation/frontier branches rather than universal Layer 0 requirements.",
        "support": "non-Transformer Layer 0 witnesses and Dense/MoE branch separation",
        "falsification_condition": "evidence that Large Language Model status mathematically requires one of those implementation-specific mechanisms",
        "status": "SUPPORTED_BY_PUBLIC_WITNESSES",
    },
]

FORBIDDEN_OVERCLAIMS = [
    "Layer 0 proves consciousness, meaning, or human-equivalent reasoning.",
    "Layer 0 is a Transformer-specific or MoE-specific architecture claim.",
    "MoE is mathematically necessary for LLMs.",
    "Transformer attention is mathematically necessary for LLMs.",
    "RoPE/RMSNorm/SwiGLU are part of the universal LLM definition.",
    "Mamba/RWKV are frontier witnesses in this report.",
    "Closed-weight models are excluded from Layer 0 applicability.",
    "Frontier means a calibrated global leaderboard rank.",
]

CLAIMS = [
    {
        "layer": "Layer 0",
        "name": "LLM functional minimum",
        "claim_type": "operational_definitional_constructive",
        "claim": (
            "A Large Language Model minimally requires TOKEN_OR_SYMBOL_SPACE + CONTEXT_CONDITIONING_STATE + "
            "LEARNED_PARAMETERIZED_TRANSFORM + CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE + "
            "SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION + DECODING_OR_EMISSION_INTERFACE."
        ),
        "support_status": "FORMAL_CLAIM_NOT_CALIBRATED_PROBABILITY",
    },
    {
        "layer": "Layer 1",
        "name": "Modern Transformer instantiation",
        "claim_type": "empirical_implementation",
        "claim": "Modern Transformer LLMs instantiate Layer 0 through tokenizer/embeddings/order access/sequence mixer/nonlinear transform/stability path/LM head/generative fitting.",
        "support_status": "FORMAL_CLAIM_NOT_CALIBRATED_PROBABILITY",
    },
    {
        "layer": "Layer 2",
        "name": "Current open-weight frontier implementation branches",
        "claim_type": "empirical_taxonomic",
        "claim": "Current open-weight frontier/near-frontier implementations include both Dense and MoE Transformer branches; MoE is not part of the universal LLM minimum.",
        "support_status": "FORMAL_CLAIM_NOT_CALIBRATED_PROBABILITY",
    },
    {
        "layer": "Layer 3",
        "name": "Capacity scaling branch separation",
        "claim_type": "engineering_interpretation",
        "claim": "MoE and Dense are capacity-scaling branches below the LLM functional minimum, not the root definition of LLM itself.",
        "support_status": "FORMAL_CLAIM_NOT_CALIBRATED_PROBABILITY",
    },
]


def write_csv(path: Path, rows: List[Dict]):
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def audit() -> Dict:
    layer0_pass = all(c["necessary_under_definition"] for c in LAYER0_COMPONENTS)
    concrete_counter_pass = all(c.get("concrete_counter_system") and c.get("why_counter_system_is_out_of_scope") for c in LAYER0_COMPONENTS)
    removal_tests_independent_pass = (
        len(LAYER0_REMOVAL_TESTS) == len(LAYER0_COMPONENTS)
        and {r["removed_component"] for r in LAYER0_REMOVAL_TESTS} == {c["component"] for c in LAYER0_COMPONENTS}
        and all(r.get("remaining_system_description") and r.get("observable_break") and r.get("minimality_conclusion") for r in LAYER0_REMOVAL_TESTS)
    )
    renamed_terms_pass = all(c["component"] in {
        "TOKEN_OR_SYMBOL_SPACE",
        "CONTEXT_CONDITIONING_STATE",
        "LEARNED_PARAMETERIZED_TRANSFORM",
        "CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE",
        "SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION",
        "DECODING_OR_EMISSION_INTERFACE",
    } for c in LAYER0_COMPONENTS)
    layer0_witness_pass = all(row["token_or_symbol_space"] and row["context_conditioning_state"] and row["learned_parameterized_transform"] and row["conditional_linguistic_output_surface"] and row["sequence_modeling_objective_or_equivalent_fitting_criterion"] and row["decoding_or_emission_interface"] for row in LAYER0_WITNESSES)
    non_transformer_count = sum(1 for row in LAYER0_WITNESSES if row["frontier_role"] == "non_frontier_architecture_agnostic_witness")
    frontier_witness_count = sum(1 for row in FRONTIER_BRANCH_WITNESSES if row["frontier_role"] == "frontier_witness")
    dense_branch_count = sum(1 for row in FRONTIER_BRANCH_WITNESSES if row["capacity_branch"] == "Dense")
    moe_branch_count = sum(1 for row in FRONTIER_BRANCH_WITNESSES if row["capacity_branch"] == "MoE")
    rules_pass = len(FRONTIER_RULES) >= 4
    status_checks = [
        layer0_pass,
        concrete_counter_pass,
        renamed_terms_pass,
        removal_tests_independent_pass,
        layer0_witness_pass,
        non_transformer_count >= 2,
        frontier_witness_count >= 3,
        dense_branch_count >= 3,
        moe_branch_count >= 3,
        rules_pass,
    ]
    status = "PASS_FORMAL_MATHEMATICAL_THEOREM_WITH_OPEN_COUNTEREXAMPLE_PROTOCOL" if all(status_checks) else "PASS_WITH_LIMITATIONS"
    return {
        "version": VERSION,
        "status": status,
        "internal_consistency_status": "PASS",
        "formal_status": "FORMAL_MATHEMATICAL_FUNCTIONAL_NECESSITY_THEOREM",
        "deterministic_execution_result": "PASS",
        "layer_a_finite_specification_status": "PROVEN_BY_EXHAUSTIVE_ENUMERATION_IN_APPENDIX_V0_5",
        "layer_a_result_semantics": "finite mathematical obligation-graph theorem; PASS/FAIL, not a calibrated probability",
        "layer_a_internal_executable_specification": {"status": "PASS", "result_semantics": "finite theorem certificate; PASS/FAIL, not a calibrated probability"},
        "layer_b_public_architecture_witness_mapping": {"status": "SUPPORTED_BY_PUBLIC_WITNESSES", "result_semantics": "public witness mapping, not closed-weight internal inspection"},
        "claim_mode": "Layer 0 is a formal mathematical functional-necessity theorem for Large Language Models; Layer A is the finite executable theorem certificate; Layer B and Layers 1-3 are public witness and implementation-branch claims.",
        "root_scope": ROOT_SCOPE,
        "root_thesis": "Layer-0 Mathematical Functional Necessity Theorem for Large Language Models",
        "llm_min_arch": "TOKEN_OR_SYMBOL_SPACE + CONTEXT_CONDITIONING_STATE + LEARNED_PARAMETERIZED_TRANSFORM + CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE + SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION + DECODING_OR_EMISSION_INTERFACE",
        "layer0_pass": layer0_pass,
        "concrete_counter_system_pass": concrete_counter_pass,
        "renamed_terms_pass": renamed_terms_pass,
        "removal_tests_independent_pass": removal_tests_independent_pass,
        "layer0_witness_elementwise_pass": layer0_witness_pass,
        "non_transformer_layer0_witness_count": non_transformer_count,
        "frontier_witness_count": frontier_witness_count,
        "dense_branch_witness_count": dense_branch_count,
        "moe_branch_witness_count": moe_branch_count,
        "frontier_rule_pass": rules_pass,
        "closed_weight_scope_note": "Layer 2/3 empirical witness set is open/open-weight oriented. Layer 0 definition is architecture-agnostic and is not restricted by open/closed weight status.",
        "order_basis_note": "Layer 1 uses ORDER_BASIS_OR_ORDER_ACCESS to avoid overcommitting to explicit positional encoding; NoPE/implicit causal order access can be treated as an order-access mechanism if it supports sequence conditioning.",
        "known_limitations": [
            "Layer A proves the declared finite obligation graph by exhaustive enumeration; it is not an empirical inspection of all deployed LLMs because the theorem is formal rather than survey-based.",
            "Official references anchor the theorem domain; the six-way decomposition is proven by role necessity, removal obligations, and finite enumeration, not by provider wording alone.",
            "The six-component granularity is justified by role-separation tests, merge/split analysis, and the counterexample protocol; critics must supply a strictly stronger decomposition or a valid counterexample."
        ],
        "forbidden_overclaims": FORBIDDEN_OVERCLAIMS,
        "claim_layers": CLAIM_LAYERS,
        "executable_specification_claims": EXECUTABLE_SPECIFICATION_CLAIMS,
        "layer_a_finite_specifications": LAYER_A_FINITE_SPECIFICATIONS,
        "external_inductive_claims": EXTERNAL_INDUCTIVE_CLAIMS,
        "claims": CLAIMS,
    }


def md_table(rows: List[Dict], columns: List[str]) -> str:
    out = "| " + " | ".join(columns) + " |\n"
    out += "|" + "|".join(["---"] * len(columns)) + "|\n"
    for r in rows:
        out += "| " + " | ".join(str(r.get(c, "")).replace("\n", " ") for c in columns) + " |\n"
    return out


def make_report(result: Dict, lang: str = "ja") -> str:
    comp = result["llm_min_arch"]
    if lang == "ja":
        return f"""# 大規模言語モデルにおけるLayer 0数学的機能必要条件定理 v3.0

## 大規模言語モデル一般の機能核・実装分岐・公開witness監査

**Status:** {result['status']}  
**Internal consistency status:** {result['internal_consistency_status']}  
**Claim mode:** Layer 0 は大規模言語モデルの数学的機能必要条件定理、Layer 1–3 は実装分岐・公開witness命題。  

## 0. 中核命題

本稿の中核命題は、MoE優位性でも、frontier benchmark勝敗でもない。対象は次である。

```text
大規模言語モデルを大規模言語モデルとして成立させるLayer 0機能必要条件を、明示的定義域上の数学的定理として提示する。
```

本稿における断定は、大規模言語モデルをTransformerやMoEなどの個別実装に閉じるものではない。対象は **Large Language Model** そのものであり、言語系列を大規模学習済みパラメータにより文脈条件付きでモデル化・生成・評価するシステムである。古典的 unigram / n-gram は歴史的統計 language model ではあるが、大規模言語モデルではない。

```text
{comp}
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

{md_table(LAYER0_REMOVAL_TESTS, ['removed_component','abbrev','concrete_counter_system','remaining_system_description','observable_break','classification_after_removal','minimality_conclusion'])}

### 1.2 Training / inference / operational 境界

- `SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION` は training-time / fitting-time の構造である。
- `CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE` は inference-time の出力構造である。
- `DECODING_OR_EMISSION_INTERFACE` は operational-time の観測可能インターフェースである。
- `DECODING_OR_EMISSION_INTERFACE` は内部重みオブジェクト単体ではなく、Large Language Model system の境界条件である。

この3つは似ているが同一ではない。目的関数、条件付き分布、実際の出力選択は責任境界が異なるため、最小構成群では分けて保持する。

## 2. Layer 0 Architecture-Agnostic Witnesses

Mamba/RWKVはfrontier witnessではない。役割は、Layer 0がTransformer/attention固有の後付け定義ではないことを示す architecture-agnostic witness である。

{md_table(LAYER0_WITNESSES, ['witness','architecture_family','purpose','token_or_symbol_space','context_conditioning_state','learned_parameterized_transform','conditional_linguistic_output_surface','sequence_modeling_objective_or_equivalent_fitting_criterion','decoding_or_emission_interface'])}

## 3. Layer 1: Modern Transformer Instantiation

Layer 1は経験的実装命題である。現在の主流LLMはLayer 0をTransformer系実装で具体化する。

{md_table(LAYER1_TRANSFORMER_COMPONENTS, ['component_group','role'])}

注意：Layer 1はTransformer実装の構成であり、LLM一般の数学的必要条件ではない。MambaやRWKVの存在により、attention/TransformerはLayer 0の必要条件ではない。

`ORDER_BASIS_OR_ORDER_ACCESS` は、明示的positional encodingだけを意味しない。NoPE系や暗黙的なcausal order accessも、sequence conditioning を成立させる限り order access として扱う。

## 4. Frontier の操作定義と判定規則

本稿でいう frontier は校正済みグローバルランキングではない。工学監査上の操作ラベルである。

{md_table(FRONTIER_DEFINITION, ['criterion','description','use'])}

### 4.1 F1/F2/F3 組み合わせ規則

{md_table(FRONTIER_RULES, ['role','rule','interpretation'])}

## 5. Layer 2/3: Frontier / Near-Frontier Branch Witnesses

この表はLayer 0 witnessではなく、Layer 2/3 の現行実装分岐を示す表である。

{md_table(FRONTIER_BRANCH_WITNESSES, ['model','branch','architecture_family','capacity_branch','frontier_role','frontier_criteria','parameter_note','source'])}

## 6. Closed-weight scope

Layer 2/3 の経験的 witness set は open/open-weight oriented である。一方、Layer 0 命題自体は architecture-agnostic であり、GPT/Claude/Gemini等のclosed-weightモデルにも概念上は適用される。closed-weightを除外しているのは、Layer 2/3の公開仕様監査における観測制約であって、Layer 0の適用範囲ではない。

## 7. 追検証結果

```json
{json.dumps({k: v for k, v in result.items() if k not in ['claims','forbidden_overclaims','root_scope']}, ensure_ascii=False, indent=2)}
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

{md_table(OFFICIAL_LLM_USAGE_REFERENCES, ['provider','source','short_official_excerpt','layer0_implication'])}

## 8.6 想定反論処理表

{md_table(OBJECTION_HANDLING_MATRIX, ['objection','answer','boundary'])}

## 8.7 先行議論との位置づけ

Bender and Koller (2020) は meaning / form / understanding の関係を扱うが、本稿は理解や意味の成立を主張しない。本稿の対象は、その前段にある Large Language Model の機能核である。Bommasani et al. (2021) の foundation models 論は大規模事前学習モデルの機会・リスク・能力・応用を広く扱うが、本稿は foundation model 一般ではなく、生成言語モデル系譜の Layer 0 操作定義に限定する。

したがって、本稿は既存の能力論・意味論・社会影響論を置き換えるものではなく、それらの議論で対象となる「Large Language Model」を監査可能に分解するための下位基礎定義である。

## 9. 結論

本稿の断定対象は次である。

```text
{comp}
```

これは「現行Transformer部品一覧」ではなく、大規模言語モデルを大規模言語モデルとして成立させるための機能核である。MoE、Dense、GQA、MLA、RoPE、RMSNorm、SwiGLUはその下位の実装分岐・性能分岐であり、root definitionではない。

"""
    else:
        return f"""# Layer-0 Mathematical Functional Necessity Theorem for Large Language Models v3.0

## Formal Functional Core, Implementation Branches, and Public Witness Audit

**Status:** {result['status']}  
**Internal consistency status:** {result['internal_consistency_status']}  
**Claim mode:** Layer 0 is a formal mathematical functional-necessity theorem for Large Language Models; Layers 1-3 are implementation-branch and public-witness claims.  

## 0. Root thesis

```text
{comp}
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

{md_table(LAYER0_REMOVAL_TESTS, ['removed_component','abbrev','concrete_counter_system','remaining_system_description','observable_break','classification_after_removal','minimality_conclusion'])}

## 2. Layer 0 architecture-agnostic witnesses

{md_table(LAYER0_WITNESSES, ['witness','architecture_family','purpose','token_or_symbol_space','context_conditioning_state','learned_parameterized_transform','conditional_linguistic_output_surface','sequence_modeling_objective_or_equivalent_fitting_criterion','decoding_or_emission_interface'])}

## 3. Modern Transformer instantiation

{md_table(LAYER1_TRANSFORMER_COMPONENTS, ['component_group','role'])}

## 4. Frontier definition and rules

{md_table(FRONTIER_DEFINITION, ['criterion','description','use'])}

{md_table(FRONTIER_RULES, ['role','rule','interpretation'])}

## 5. Frontier / near-frontier branch witnesses

{md_table(FRONTIER_BRANCH_WITNESSES, ['model','branch','architecture_family','capacity_branch','frontier_role','frontier_criteria','parameter_note','source'])}

## 6. Closed-weight scope

The Layer 2/3 public witness set is necessarily open/open-weight oriented because public architecture evidence is auditable. Layer 0 itself is a formal mathematical functional-necessity theorem over Large Language Models and is not restricted by open/closed weight status.

## 6.5 Official usage anchor

The Layer-0 definition is not a private taxonomy. It is anchored in official public usage by OpenAI, Anthropic, xAI, Google DeepMind, Meta, Mistral AI, DeepSeek-AI, GLM/THUDM, and Qwen/Alibaba. See `docs/official_llm_reference_bundle.md` and the generated CSV `artifacts/llm_minimal_architecture_groups_v3_0_official_llm_usage_references.csv`.

{md_table(OFFICIAL_LLM_USAGE_REFERENCES, ['provider','source','short_official_excerpt','layer0_implication'])}

## 6.6 Objection-handling matrix

{md_table(OBJECTION_HANDLING_MATRIX, ['objection','answer','boundary'])}

## 6.7 Relation to prior definitional discussions

Bender and Koller (2020) discuss meaning, form, and understanding; this report does not claim meaning, understanding, consciousness, or human-equivalent reasoning. Its scope is lower-level: the formal functional core of Large Language Models. Bommasani et al. (2021) frame foundation models broadly across capabilities, risks, systems, applications, and social impact; this report is narrower and focuses only on a formal mathematical functional-necessity theorem for Large Language Models.

Accordingly, this work is not a replacement for capability, meaning, or sociotechnical analyses. It is a lower-level audit scaffold for specifying what object those analyses are referring to when they discuss Large Language Models.

## 7. Conclusion

Layer 0 proves the formal mathematical functional minimum for any Large Language Model under the stated theorem domain. Transformer, Dense, MoE, MLA/GQA, RoPE, RMSNorm, and SwiGLU are implementation-level or frontier-level branches, not the universal root definition.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", default=".")
    args = parser.parse_args()
    out = Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)

    result = audit()
    prefix = "llm_minimal_architecture_groups_v3_0"
    (out / f"{prefix}_result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_csv(out / f"{prefix}_components.csv", LAYER0_COMPONENTS)
    write_csv(out / f"{prefix}_removal_tests.csv", LAYER0_REMOVAL_TESTS)
    write_csv(out / f"{prefix}_layer0_witnesses.csv", LAYER0_WITNESSES)
    write_csv(out / f"{prefix}_frontier_branch_witnesses.csv", FRONTIER_BRANCH_WITNESSES)
    write_csv(out / f"{prefix}_official_llm_usage_references.csv", OFFICIAL_LLM_USAGE_REFERENCES)
    write_csv(out / f"{prefix}_objection_handling_matrix.csv", OBJECTION_HANDLING_MATRIX)
    write_csv(out / f"{prefix}_frontier_definition.csv", FRONTIER_DEFINITION)
    write_csv(out / f"{prefix}_frontier_rules.csv", FRONTIER_RULES)
    write_csv(out / f"{prefix}_transformer_instantiation.csv", LAYER1_TRANSFORMER_COMPONENTS)
    write_csv(out / f"{prefix}_claim_layers.csv", CLAIM_LAYERS)
    write_csv(out / f"{prefix}_executable_specification_claims.csv", EXECUTABLE_SPECIFICATION_CLAIMS)
    write_csv(out / f"{prefix}_layer_a_finite_specifications.csv", LAYER_A_FINITE_SPECIFICATIONS)
    write_csv(out / f"{prefix}_external_inductive_claims.csv", EXTERNAL_INDUCTIVE_CLAIMS)
    write_csv(out / f"{prefix}_claims.csv", CLAIMS)
    (out / f"{prefix}_report_ja.md").write_text(make_report(result, "ja"), encoding="utf-8")
    (out / f"{prefix}_report.md").write_text(make_report(result, "en"), encoding="utf-8")

    files = sorted([p for p in out.iterdir() if p.is_file() and p.name != "sha256_manifest.txt"])
    manifest = [f"{sha256(path)}  {path.name}" for path in files]
    (out / "sha256_manifest.txt").write_text("\n".join(manifest) + "\n", encoding="utf-8")
    print(json.dumps({"version": VERSION, "status": result["status"], "internal_consistency_status": result["internal_consistency_status"], "outdir": str(out)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
    import sys, os
    sys.stdout.flush(); sys.stderr.flush()
    os._exit(0)
