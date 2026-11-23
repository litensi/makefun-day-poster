"""Copy the day's front page to /output/entry.png."""

import os
from pathlib import Path
from shutil import copyfile


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    # The contest's one-image rule allows a single output file.
    copyfile(Path(__file__).with_name("entry.jpg"), output_dir / "entry.png")


if __name__ == "__main__":
    main()
