import sys
import subprocess
import threading

import pathlib
import shutil

import onlinejudge_command.main


def download_samples(contest_name, problem_name, force=False):
    problem_dir = pathlib.Path("test/" + contest_name + "/" + problem_name)
    if problem_dir.exists():
        if force:
            shutil.rmtree(problem_dir)
        else:
            return
    args = [
        "dl",
        "-d",
        str(problem_dir),
        f"https://atcoder.jp/contests/{contest_name}/tasks/{contest_name}_{problem_name}",
    ]
    th = threading.Thread(target=onlinejudge_command.main.main, args=(args,))
    th.start()
    th.join()


def build_source(file_path: pathlib.Path) -> str:
    print("building", file_path)
    file_name = file_path.name
    file_suffix = file_path.suffix
    exec_file = pathlib.Path.cwd() / "a.out"
    if file_suffix == ".py":
        return f"python3 {file_path}"
    elif file_suffix == ".cpp":
        ret = subprocess.run(
            ["g++", "-o", str(exec_file), str(file_path)],
            stdout=sys.stdout,
            stderr=sys.stderr,
        )
        if ret.check_returncode():
            sys.exit()
        return str(exec_file)
    else:
        print(f"Unsupported file {file_name}.{file_suffix}")
        sys.exit()


def test_cases(contest_name, problem_name, exec_command):
    args = [
        "test",
        "-c",
        exec_command,
        "-d",
        f"test/{contest_name}/{problem_name}",
    ]
    th = threading.Thread(target=onlinejudge_command.main.main, args=(args,))
    th.start()
    th.join()


def main():
    file_path = pathlib.Path(sys.argv[1])
    if file_path.parent.parent.name != "contests":
        print(str(file_path), "does not exist in contests folder!")
        return

    problem_name = file_path.stem
    contest_name = file_path.parent.name

    download_samples(contest_name, problem_name)

    exec_command = build_source(file_path)

    test_cases(contest_name, problem_name, exec_command)


if __name__ == "__main__":
    main()
