import os
import shlex
import subprocess
from pathlib import Path

os.chdir(str(Path(__file__).absolute().parent))

from public_data import repl


def make_final_html(template: str, repl: dict, final: str) -> None:
    text = Path(template).read_text("utf-8")

    for name, value in repl.items():
        text = text.replace("{" + name + "}", str(value))

    Path(final).write_text(text, "utf-8")


def render_pdf(inp, out):
    args = shlex.split(
        f"ChromeHtmlToPdf/ChromeHtmlToPdfConsole.exe --input {inp} --output {out}"
    )
    return subprocess.call(args)


template = "./source/template.html"
final = "./source/final.html"

make_final_html(template, repl, final)
print(render_pdf(final, final[:-4] + "pdf"))
