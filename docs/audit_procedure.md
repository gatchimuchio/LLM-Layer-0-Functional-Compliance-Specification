# Audit Procedure

## Commands

```bash
make audit
make verify
make test-all
```

## Expected outputs

- Main artifact generation completes.
- `artifacts/sha256_manifest.txt` verifies.
- Layer A obligation graph appendix reports `proper_subset_pass_count = 0`.
- Repository manifest verifies.

## Interpretation

The audit verifies repository consistency, artifact determinism, manifest integrity, and the declared Layer A obligation graph.

It does not assign calibrated calibrated probability estimate and does not empirically inspect all external LLMs.

