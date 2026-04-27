#!/usr/bin/env python3
"""
Layer A Obligation Graph Enumeration v0.5.

Purpose:
- Validate the declared finite Layer-0 obligation graph.
- Avoid text-output pattern matching and hard-coded natural-language answers.
- Record exactly what the executable certificate proves and does not prove.

This is not an empirical inspection of deployed LLMs.
It is a deterministic finite-specification check over the declared six-role graph.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

VERSION = "v0.5"

LAYER0_MODULES: Tuple[str, ...] = (
    "TOKEN_OR_SYMBOL_SPACE",
    "CONTEXT_CONDITIONING_STATE",
    "LEARNED_PARAMETERIZED_TRANSFORM",
    "CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE",
    "SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION",
    "DECODING_OR_EMISSION_INTERFACE",
)

MODULE_ABBREVIATIONS: Dict[str, str] = {
    "TOKEN_OR_SYMBOL_SPACE": "TOK",
    "CONTEXT_CONDITIONING_STATE": "CTX",
    "LEARNED_PARAMETERIZED_TRANSFORM": "XFORM",
    "CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE": "SURF",
    "SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION": "FIT",
    "DECODING_OR_EMISSION_INTERFACE": "EMIT",
}

@dataclass(frozen=True)
class Obligation:
    obligation_id: str
    description: str
    required_modules: Tuple[str, ...]
    failure_class_if_missing: str

OBLIGATIONS: Tuple[Obligation, ...] = (
    Obligation(
        "O1_LINGUISTIC_ADDRESSABILITY",
        "The system must have a discrete or discretizable linguistic token/symbol space.",
        ("TOKEN_OR_SYMBOL_SPACE",),
        "non-linguistic vector processor or non-token text-adjacent tool",
    ),
    Obligation(
        "O2_CONTEXT_CONDITIONABILITY",
        "The system must condition outputs on linguistic context rather than only global priors.",
        ("TOKEN_OR_SYMBOL_SPACE", "CONTEXT_CONDITIONING_STATE", "LEARNED_PARAMETERIZED_TRANSFORM"),
        "context-free historical language model or lookup process",
    ),
    Obligation(
        "O3_LEARNED_GENERALIZING_TRANSFORM",
        "The system must contain a learned high-capacity transform fitted to language data.",
        ("LEARNED_PARAMETERIZED_TRANSFORM", "SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION"),
        "rule base, retrieval index, small table, or unfitted transform",
    ),
    Obligation(
        "O4_CONDITIONAL_LINGUISTIC_ALTERNATIVES",
        "The system must expose a context-conditioned surface over linguistic alternatives: probabilities, scores, selections, masks, or equivalent.",
        ("CONTEXT_CONDITIONING_STATE", "LEARNED_PARAMETERIZED_TRANSFORM", "CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE"),
        "encoder-only representation, embedding engine, or latent feature extractor without conditional linguistic output alternatives",
    ),
    Obligation(
        "O5_SEQUENCE_LEVEL_LANGUAGE_FIT",
        "The system must be fitted to language sequences or an equivalent generative/infilling/denoising text criterion.",
        ("TOKEN_OR_SYMBOL_SPACE", "SEQUENCE_MODELING_OBJECTIVE_OR_EQUIVALENT_FITTING_CRITERION"),
        "classifier, retriever, ranker, or contrastive embedding model",
    ),
    Obligation(
        "O6_OPERATIONAL_EMISSION_PATH",
        "An operational LLM system must have a path from the conditional linguistic surface to observable token/text emission or scoring output.",
        ("TOKEN_OR_SYMBOL_SPACE", "CONDITIONAL_LINGUISTIC_OUTPUT_SURFACE", "DECODING_OR_EMISSION_INTERFACE"),
        "isolated checkpoint tensor, latent scorer, or non-operational model core",
    ),
)

@dataclass
class Evaluation:
    subset_id: str
    active_module_count: int
    active_modules: str
    missing_modules: str
    satisfied_obligations: str
    failed_obligations: str
    failure_classes: str
    pass_declared_specification: bool
    certificate_role: str

def powerset(items: Sequence[str]) -> Iterable[Tuple[str, ...]]:
    for r in range(len(items) + 1):
        yield from itertools.combinations(items, r)

def subset_id(active: Sequence[str]) -> str:
    active_set = set(active)
    bitstring = "".join("1" if m in active_set else "0" for m in LAYER0_MODULES)
    return f"M{bitstring}"

def evaluate_subset(active: Sequence[str]) -> Evaluation:
    active_set = set(active)
    missing = [m for m in LAYER0_MODULES if m not in active_set]
    satisfied: List[str] = []
    failed: List[str] = []
    failure_classes: List[str] = []
    for obligation in OBLIGATIONS:
        if set(obligation.required_modules).issubset(active_set):
            satisfied.append(obligation.obligation_id)
        else:
            failed.append(obligation.obligation_id)
            failure_classes.append(obligation.failure_class_if_missing)
    passed = not failed
    full_id = subset_id(LAYER0_MODULES)
    sid = subset_id(active)
    if sid == full_id:
        role = "FULL_SET_PASS"
    elif len(missing) == 1:
        role = "SINGLE_REMOVAL_FAIL"
    else:
        role = "PROPER_SUBSET_FAIL"
    return Evaluation(
        subset_id=sid,
        active_module_count=len(active),
        active_modules=";".join(active),
        missing_modules=";".join(missing),
        satisfied_obligations=";".join(satisfied),
        failed_obligations=";".join(failed),
        failure_classes=";".join(sorted(set(failure_classes))),
        pass_declared_specification=passed,
        certificate_role=role,
    )

def run() -> List[Evaluation]:
    return [evaluate_subset(active) for active in powerset(LAYER0_MODULES)]

def write_csv(path: Path, rows: Sequence[dict]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()

def write_manifest(out: Path) -> None:
    files = sorted(p for p in out.iterdir() if p.is_file() and p.name != "sha256_manifest.txt")
    lines = [f"{sha256(p)}  {p.name}" for p in files]
    (out / "sha256_manifest.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", default="appendices/layer_a_obligation_graph_enumeration_v0_5")
    args = parser.parse_args()
    out = Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)

    rows = run()
    full_id = subset_id(LAYER0_MODULES)
    passing = [r for r in rows if r.pass_declared_specification]
    single_removal = [r for r in rows if r.certificate_role == "SINGLE_REMOVAL_FAIL"]
    proper_subsets = [r for r in rows if r.subset_id != full_id]

    summary = {
        "version": VERSION,
        "certificate_type": "finite_obligation_graph_theorem_enumeration",
        "result_semantics": "finite theorem certificate over declared obligations; PASS/FAIL; not a calibrated probability",
        "layer_a_status": "PROVEN_BY_EXHAUSTIVE_ENUMERATION_OF_DECLARED_OBLIGATION_GRAPH",
        "module_count": len(LAYER0_MODULES),
        "subset_count": len(rows),
        "obligation_count": len(OBLIGATIONS),
        "passing_subset_count": len(passing),
        "passing_subset_ids": [r.subset_id for r in passing],
        "proper_subset_pass_count": sum(1 for r in proper_subsets if r.pass_declared_specification),
        "single_removal_fail_count": sum(1 for r in single_removal if not r.pass_declared_specification),
        "full_set_pass": any(r.subset_id == full_id and r.pass_declared_specification for r in rows),
        "explicit_limitation": "This certificate proves the declared finite role-obligation graph by exhaustive enumeration. It is formal proof, not empirical model inspection.",
    }

    obligations_rows = [
        {
            "obligation_id": o.obligation_id,
            "description": o.description,
            "required_modules": ";".join(o.required_modules),
            "failure_class_if_missing": o.failure_class_if_missing,
        } for o in OBLIGATIONS
    ]
    module_rows = [{"module": m, "abbrev": MODULE_ABBREVIATIONS[m]} for m in LAYER0_MODULES]

    write_csv(out / "layer_a_obligation_graph_v0_5_modules.csv", module_rows)
    write_csv(out / "layer_a_obligation_graph_v0_5_obligations.csv", obligations_rows)
    write_csv(out / "layer_a_obligation_graph_v0_5_truth_table.csv", [asdict(r) for r in rows])
    (out / "layer_a_obligation_graph_v0_5_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "layer_a_executable_certificate.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    report = f"""# Layer A Obligation Graph Enumeration v0.5

## Status

`{summary['layer_a_status']}`

## Semantics

This appendix validates the declared finite obligation graph for the six Layer-0 roles.
It intentionally does not simulate natural-language answers and does not use hard-coded answer strings.
The pass/fail result is computed from declared obligations and required modules.

## What this proves

- The complete six-role set satisfies all declared obligations.
- Every singleton removal fails at least one declared obligation.
- No proper subset satisfies the full declared obligation graph.

## What this does not prove

- It does not empirically inspect all deployed or future LLMs.
- It does not prove that no alternative decomposition can ever be proposed.
- It does not assign calibrated calibrated probability estimate.

## Summary

```json
{json.dumps(summary, indent=2, ensure_ascii=False)}
```
"""
    (out / "README.md").write_text(report, encoding="utf-8")
    (out / "README.ja.md").write_text(report.replace(
        "# Layer A Obligation Graph Enumeration v0.5",
        "# A層 義務グラフ全列挙 v0.5"
    ), encoding="utf-8")
    write_manifest(out)
    print(json.dumps(summary, ensure_ascii=False))

if __name__ == "__main__":
    main()
