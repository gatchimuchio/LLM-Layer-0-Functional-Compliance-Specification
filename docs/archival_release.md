# Archival Release Checklist

This package intentionally avoids fake GitHub URLs, fake DOI values, and fake ORCID identifiers.

Before claiming archival permanence:

1. Create the public GitHub repository.
2. Add the final repository URL to `CITATION.cff` as `repository-code`.
3. Add the author's ORCID if available.
4. Create a tagged GitHub release.
5. Connect the repository to Zenodo.
6. Add the Zenodo DOI to `CITATION.cff`, `README.md`, and `README.ja.md`.
7. Re-run `make test`.
8. Recompute `REPOSITORY_SHA256_MANIFEST.txt`.

Rationale: GitHub URLs can be renamed, moved, force-pushed, or deleted. A DOI-backed release is the proper archival reference point.
