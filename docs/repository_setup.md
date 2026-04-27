# Repository Setup Notes

This package is intended to be uploaded to a newly created GitHub repository.

## Recommended steps

1. Create a new GitHub repository.
2. Copy the contents of this folder to the repository root.
3. Run:

```bash
make test-all
```

4. Commit all files.
5. Create a tagged release, for example:

```bash
git tag v1.0.0
git push origin v1.0.0
```

6. Connect the repository to Zenodo and generate an archival DOI.
7. Update `CITATION.cff` with:

- `repository-code`, once the GitHub URL exists,
- `doi`, once Zenodo issues it,
- `orcid`, if the author wants ORCID attribution.

8. Regenerate the repository manifest if citation metadata changes.

## Why placeholders are not included

This repository package does not include fake URLs, fake DOIs, or fake ORCID IDs. Those values are publication metadata and must be added only after the actual repository and archival record exist.
