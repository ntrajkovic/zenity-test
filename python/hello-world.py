#!/usr/bin/env python3

# ********************************************************************
# hello-world.py
# Display "Hello World!" using zenity
# (C) 2022 Nenad Trajkovic, MIT License
# https://github.com/ntrajkovic/zenity-test
# ********************************************************************

import subprocess
import shutil
import sys

if __name__ == "__main__":

    if shutil.which("zenity") is None:
        print("\nZenity not found.\n")
        sys.exit(1)

    print("\n",
          "Zenity Test\n",
          "Test Info dialog\n", sep = "")

    subprocess.run(["zenity",
        "--info",
        "--width=200",
        "--title=Zenity Test",
        "--text=Hello World!"],
        stderr = subprocess.PIPE, text = True)

    print("https://github.com/ntrajkovic/zenity-test\n")
