import random
import pathlib
import sys
import subprocess


def create_input(filename="input.txt"):
    text = []
    n = random.randint(3, 1000)
    text.append(str(n))
    for _ in range(n):
        text.append(" ".join([str(random.randint(1, 100)) for _ in range(5)]))
    with open(filename, "w") as f:
        f.write("\n".join(text))


def main():
    print(pathlib.Path.cwd())
    n = int(input())
    for i in range(n):
        create_input()
        cat = subprocess.Popen(["cat", "input.txt"], stdout=subprocess.PIPE)
        proc = subprocess.Popen(
            ["./a.out", "<", "input.txt"],
            encoding="utf-8",
            stdin=cat.stdout,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        proc.wait()
        print("stdout: ", [proc.stdout.readline() for _ in range(10)])
        print("stderr: ", [proc.stderr.readline() for _ in range(10)])


if __name__ == "__main__":
    main()
