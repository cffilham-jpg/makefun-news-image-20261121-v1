"""Copy the pre-rendered front page to the make.fun output directory.

Standard library only. The entry image (entry.png) sits beside this file;
both runs write the same bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PNG_MAGIC = b"\x89PNG"


def entry_path():
    return os.path.join(HERE, "entry.png")


def validate_png(path):
    """Return an error message unless path is a readable PNG file."""
    if not os.path.exists(path):
        return "entry image missing: %s" % path
    if not os.path.isfile(path):
        return "entry image is not a regular file: %s" % path
    with open(path, "rb") as handle:
        header = handle.read(len(PNG_MAGIC))
    if header != PNG_MAGIC:
        return "entry image is not a PNG file: %s" % path
    return None


def copy_entry(src, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


def main():
    src = entry_path()
    error = validate_png(src)
    if error is not None:
        print("error: %s" % error, file=sys.stderr)
        return 1
    copy_entry(src, os.environ["MAKEFUN_OUTPUT_DIR"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
