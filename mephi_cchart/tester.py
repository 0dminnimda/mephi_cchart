import time
import subprocess
import os
from distutils.ccompiler import new_compiler, CCompiler
from pathlib import Path

os.chdir(str(Path(__file__).absolute().parent))


def wait_till_file_updated(path: str) -> None:
    file = Path(path)

    try:
        other_time = file.stat().st_mtime_ns
    except OSError:
        # Support writing a fresh file (which is always newer than a non-existant one)
        other_time = None

    while other_time is None or other_time >= file.stat().st_mtime_ns:
        
        file.open(mode="rb")
        file.touch()


name = "myprogram"
source = name + ".c"

# linux doesn't care about extention and windows won't work otherwise
executable = f"compilation/{name}.exe"

compiler = new_compiler()
objects = compiler.compile([source], output_dir="compilation")

try:
    os.remove(executable)
except FileNotFoundError:
    pass

compiler.link(CCompiler.EXECUTABLE, objects, executable)

# exit()

# wait_till_file_updated(executable)

result = subprocess.run([executable], input="100", capture_output=True, text=True)
print(result.stdout.lstrip("\n"))
