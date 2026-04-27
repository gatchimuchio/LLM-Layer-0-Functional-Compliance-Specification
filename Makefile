.PHONY: audit verify test clean help

PYTHON ?= python3
PYFLAGS ?= -S
OUTDIR ?= artifacts
SCRIPT := llm_minimal_architecture_groups_v3_0.py
MANIFEST := $(OUTDIR)/sha256_manifest.txt

help:
	@echo "Targets:"
	@echo "  make audit   - regenerate artifacts"
	@echo "  make verify  - verify artifacts against sha256 manifest"
	@echo "  make test    - run audit and verify"
	@echo "  make clean   - remove generated artifacts directory and Python cache"

$(OUTDIR):
	mkdir -p $(OUTDIR)

audit: $(OUTDIR)
	$(PYTHON) $(PYFLAGS) $(SCRIPT) --outdir $(OUTDIR)

verify:
	$(PYTHON) $(PYFLAGS) scripts/verify_manifest.py $(MANIFEST)

test: audit verify

clean:
	rm -rf $(OUTDIR) __pycache__

.PHONY: obligation-graph verify-obligation-graph test-all

ABLATION_DIR := appendices/layer_a_obligation_graph_enumeration_v0_5
ABLATION_SCRIPT := $(ABLATION_DIR)/layer_a_obligation_graph_enumeration_v0_5.py

obligation-graph:
	$(PYTHON) $(PYFLAGS) $(ABLATION_SCRIPT) --outdir $(ABLATION_DIR)

verify-obligation-graph:
	$(PYTHON) $(PYFLAGS) scripts/verify_manifest.py $(ABLATION_DIR)/sha256_manifest.txt

test-all: test obligation-graph verify-obligation-graph manifest-repository verify-repository


.PHONY: manifest-repository verify-repository

manifest-repository:
	$(PYTHON) $(PYFLAGS) scripts/generate_repository_manifest.py

verify-repository:
	$(PYTHON) $(PYFLAGS) scripts/verify_manifest.py REPOSITORY_SHA256_MANIFEST.txt
