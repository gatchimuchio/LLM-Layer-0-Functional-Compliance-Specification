# Formal Scope and Argument

## Theorem domain

Let `LLM` denote the contemporary technical class of large-scale learned language models: systems that operate over linguistic token/symbol sequences, condition on context, use learned parameterized transformations, expose conditional linguistic output alternatives, are fitted to language sequences or equivalent generative text criteria, and provide an operational decoding/emission path.

This boundary is anchored by official provider usage and public model-family witnesses. It is not a private stipulation.

## Theorem

For any system `S`, if `S` is a Large Language Model in the theorem domain, then `S` must instantiate each of the following roles, either explicitly or through a functional equivalent:

1. `TOKEN_OR_SYMBOL_SPACE`
2. `CONTEXT_CONDITIONING_STATE`
3. `LEARNED_PARAMETERIZED_TRANSFORM`
4. `CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE`
5. `SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION`
6. `DECODING_OR_EMISSION_INTERFACE`

## Proof sketch

Assume `S` is an LLM. Remove any one of the six roles.

- Without token/symbol space, `S` does not operate over linguistic sequences.
- Without context conditioning, `S` is not prompt/sequence-conditioned language modeling.
- Without learned parameterized transformation, `S` is a table/rule/retrieval system rather than an LLM core.
- Without conditional linguistic output surface, `S` cannot define linguistic alternatives for generation, completion, scoring, or selection.
- Without a sequence-modeling or equivalent fitting criterion, `S` is not trained/fitted as a language sequence model.
- Without decoding/emission interface, the operational LLM system has no observable linguistic output path.

Each removal collapses LLM status or moves the candidate into another AI/text-system class. Therefore all six roles are necessary.

Layer A then proves the finite obligation graph by exhaustive enumeration of all 64 subsets. Only the full set satisfies all declared obligations.

## Counterexample condition

A valid counterexample must be an LLM and must lack at least one role and every functional equivalent. Anything else is a taxonomy dispute, implementation variation, or non-LLM system.
