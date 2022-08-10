from stat import FILE_ATTRIBUTE_SYSTEM
from textwrap import wrap
import time
import sys
import random

def give_time_stdout():
    for i in range(100):
        time.sleep(0.01)
        sys.stdout.write(f"\u001b[1000D{i + 1}%")
        sys.stdout.flush()
    return


def give_time_print():
    sys.stdout.flush()
    for i in range(100):
        time.sleep(0.01)
        print(f"\u001b[1000D{i + 1}%", flush=True, end='')
    return


def yield_testing():
    for i in range(10):
        yield i


def progress_temp(length: int = 35):
    for i in range(100):
        time.sleep(0.01)
        width = i * (length - 1) // 100
        print(f"\u001b[1000D[{width * '#':<{length - 2}}]", flush=True, end='')

def loading(count):
    all_progress = [0] * 4
    print("\n" * count, end="")
    ppp = 0
    while any(x < 100 for x in all_progress):
        # time.sleep(0.01)
        unfinished = [(i, v) for (i, v) in enumerate(all_progress) if v < 100]
        index, _ = random.choice(unfinished)
        all_progress[index] += 1
        print("\u001b[1000D", end="")
        print("\u001b[" + str(count) + "A", end="")
        for progress in all_progress:
            width = progress // 4
            print("[" + "#" * width + " " * (25 - width) + "]", flush=True)
        ppp += 1


def downloading_files():
    l = list()
    n = 37
    for x in range(0, n):
        time.sleep(0.1)
        l.append(0)
        yield (x, n)
    print("\nFini")


def progress_bar(progression: int, total: int, size: int = 25):
    print(f"\u001b[1000D[{int((progression / total) * size) * '#':<{size - 1}}]", flush=True, end='')

def wrapper():
    for x, y in downloading_files():
        progress_bar(x, y)
    

if __name__ == "__main__":
    ...
    # give_time_print()
    # for x in yield_testing():
    #     print(x)
    # print("#" * 50)
    # progress_temp()
    # loading(4)
    # downloading_files()
    wrapper()
    