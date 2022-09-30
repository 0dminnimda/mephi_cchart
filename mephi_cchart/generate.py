import os
import shlex
import subprocess
from pathlib import Path

os.chdir(str(Path(__file__).absolute().parent))

inp = "./source/index.html"
out = "./index.pdf"
args = shlex.split(
    f"ChromeHtmlToPdf/ChromeHtmlToPdfConsole.exe --input {inp} --output {out}"
)
p = subprocess.call(args)
print(p)
