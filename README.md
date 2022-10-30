# taptempo.py

A simple port of [taptempo](https://taptempo.tuxfamily.org/) to pure
Python. Calculate the BPM of a song from your terminal.

```
usage: taptempo.py [-h] [--samples SAMPLES] [--reset RESET]

A command line tool to help determine the BPM of a song

options:
  -h, --help         show this help message and exit
  --samples SAMPLES  How many of the last inputs to consider when calculating BPM
  --reset RESET      After how many seconds of no inputs to restart the calculation

Inspired by taptempo: https://taptempo.tuxfamily.org/
```