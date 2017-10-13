from collections import deque


def search(lines, patterns, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous lines
        previous_lines.append(line)
