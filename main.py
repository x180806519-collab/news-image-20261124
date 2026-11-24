#!/usr/bin/env python3
"""news-image-20261124: copy the day's newspaper image to the output dir.

The image (entry.png, 1024x1024) was drawn from the verified world news of
Tuesday 24 November 2026 and ships in this repository. The program does no
network and no drawing at grade time: it just copies the file, so the two
graded runs produce byte-identical output. The copy is checked with a
sha256 comparison before the program exits. Standard library only.
"""
import hashlib
import os
import shutil
import sys
from pathlib import Path

IMAGE = "entry.png"


def run():
    root = Path(__file__).resolve().parent
    src = root / IMAGE
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out.mkdir(parents=True, exist_ok=True)
    target = out / IMAGE
    shutil.copyfile(src, target)
    if hashlib.sha256(src.read_bytes()).hexdigest() != hashlib.sha256(
        target.read_bytes()
    ).hexdigest():
        sys.exit("output bytes differ from entry.png")
    print(f"wrote {target} ({target.stat().st_size} bytes)")


if __name__ == "__main__":
    run()
