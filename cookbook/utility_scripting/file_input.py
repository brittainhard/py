#!/usr/bin/env python3
import fileinput


if __name__ == "__main__":
    with fileinput.input() as f_input:
        for line in f_input:
            print(line, end='')
