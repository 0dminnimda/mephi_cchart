import subprocess
import os
from distutils.ccompiler import new_compiler, CCompiler
from pathlib import Path

os.chdir(str(Path(__file__).absolute().parent))


name = "myprogram"
source = name + ".c"

# linux doesn't care about extention and windows won't work otherwise
executable = f"compilation/{name}.exe"

compiler = new_compiler()
objects = compiler.compile([source], output_dir="compilation")
compiler.link(CCompiler.EXECUTABLE, objects, executable)

result = subprocess.run([executable], input="100", capture_output=True, text=True)
print(result.stdout.lstrip("\n"))
