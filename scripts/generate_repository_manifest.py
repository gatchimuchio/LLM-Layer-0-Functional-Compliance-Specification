#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'REPOSITORY_SHA256_MANIFEST.txt'


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    files = []
    for p in ROOT.rglob('*'):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT)
        if '.git' in rel.parts or '__pycache__' in rel.parts:
            continue
        if rel.suffix == '.pyc':
            continue
        if rel.as_posix() == 'REPOSITORY_SHA256_MANIFEST.txt':
            continue
        files.append(rel)
    lines = [f"{sha256(ROOT / rel)}  {rel.as_posix()}" for rel in sorted(files, key=lambda x: x.as_posix())]
    MANIFEST.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'WROTE {MANIFEST} ({len(lines)} files)')
    return 0

if __name__ == '__main__':
    import sys, os
    rc = main()
    sys.stdout.flush(); sys.stderr.flush()
    os._exit(rc)
