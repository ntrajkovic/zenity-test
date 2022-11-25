#!/usr/bin/env python3

# ********************************************************************
# hello-world.py
# Display "Hello World!" using zenity
# (C) 2022, Nenad Trajkovic, MIT License
# https://github.com/ntrajkovic/zenity-test
# ********************************************************************

import subprocess

if __name__ == "__main__":
    subprocess.run(["zenity",
        "--info",
        "--width=200",
        "--title=Zenity Test",
        "--text=Hello World!"])