#!/usr/bin/env python3
"""Verify a sha256_manifest.txt file.

Manifest format:
    <sha256>  <filename>

The file paths are resolved relative to the manifest directory.
"""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import sys


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('manifest', help='Path to sha256_manifest.txt')
    args = parser.parse_args()

    manifest = Path(args.manifest)
    if not manifest.exists():
        print(f'ERROR manifest not found: {manifest}', file=sys.stderr)
        return 2

    base = manifest.parent
    ok = True
    lines = [line.strip() for line in manifest.read_text(encoding='utf-8').splitlines() if line.strip()]
    for line in lines:
        try:
            expected, name = line.split(None, 1)
        except ValueError:
            print(f'ERROR invalid manifest line: {line}', file=sys.stderr)
            ok = False
            continue
        path = base / name.strip()
        if not path.exists():
            print(f'MISSING  {path}')
            ok = False
            continue
        actual = sha256(path)
        if actual == expected:
            print(f'OK       {path}')
        else:
            print(f'FAILED   {path}\n  expected: {expected}\n  actual:   {actual}')
            ok = False
    if ok:
        print('ALL_OK')
        return 0
    return 1


if __name__ == '__main__':
    import os
    rc = main()
    sys.stdout.flush(); sys.stderr.flush()
    os._exit(rc)
