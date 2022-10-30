#!/usr/bin/env python3
import time

NS = 1000000000


def taptempo(samples, reset):
    times = []

    prompt = "Start tapping enter..."

    while True:
        try:
            r = input(prompt)
        except KeyboardInterrupt as e:
            print()
            raise e

        if r == "q":
            break

        now = time.monotonic_ns()

        if len(times) > 0 and (now - times[-1]) >= (reset * NS):
            times = [now]
        else:
            times.append(now)
            times = times[-samples:]

        occurences = len(times)
        if occurences > 1:
            elapsed = times[-1] - times[0]
            interval = elapsed / (occurences - 1)
            bpm = round((60 * NS) / interval)
            prompt = f"{bpm} bpm"
        else:
            prompt = "Keep tapping enter..."


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="A command line tool to help determine the BPM of a song",
        epilog="Inspired by taptempo: https://taptempo.tuxfamily.org/",
    )

    parser.add_argument(
        "--samples",
        type=int,
        default=5,
        help="How many of the last inputs to consider when calculating BPM",
    )
    parser.add_argument(
        "--reset",
        type=float,
        default=5,
        help="After how many seconds of no inputs to restart the calculation",
    )

    args = parser.parse_args()

    try:
        taptempo(args.samples, args.reset)
    except KeyboardInterrupt:
        pass
