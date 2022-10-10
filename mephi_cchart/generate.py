import os
from pathlib import Path

from html2pdf import render_pdf
from public_data import repl
from terminal import render_terminal_png
from tester import compile_program, run_program


def run_n_record(filename: str, terminal: str) -> str:
    exe = compile_program(filename)

    runs = []
    os.system(exe)

    result = run_program(exe, "100")
    print(result.stdout.lstrip("\n"))

    render_terminal_png(
        terminal,
        repl["SCREENSHOTS"],
        margin=30,
        line_offset=6,
        font="Consola",
        min_line_length=30,
    )

    return "user: ".join(runs)


def make_final_html(template: str, repl: dict, final: str) -> None:
    text = Path(template).read_text("utf-8")

    for name, value in repl.items():
        text = text.replace("{" + name + "}", str(value))

    Path(final).write_text(text, "utf-8")


if __name__ == "__main__":
    import fix_dir

    template = "./source/template.html"
    final = "./source/final.html"
    image = "./source/terminal.png"
    name = "myprogram.c"

    repl["TEST-EXAMPLES"] = run_n_record(name, image)
    make_final_html(template, repl, final)
    print(render_pdf(final))
