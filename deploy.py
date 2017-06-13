from pathlib import Path
import sys
import os
import shutil

target = Path.cwd().parent / "WinterTechForum.github.io"

for item in target.iterdir():
    if item.name == ".git":
        continue
    elif item.is_file():
        print("removing FILE: {}".format(item))
        item.unlink()
    elif item.is_dir():
        print("removing DIR: {}".format(item))
        shutil.rmtree(item)
    else:
        print("UNKNOWN ITEM")
        sys.exit(1)

for src in (Path.cwd() / "public").iterdir():
    print(src)
    if src.is_file():
        print("copying FILE: {}".format(src))
        shutil.copy(src, target)
    elif src.is_dir():
        print("copying DIR: {}".format(src))
        shutil.copytree(src, target/ src.name)
    else:
        print("UNKNOWN ITEM")
        sys.exit(1)
