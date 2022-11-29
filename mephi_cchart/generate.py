import html
import os
from pathlib import Path

from html2pdf import render_pdf
from public_data import repl
from terminal import render_terminal_png
from tester import compile_program, run_program

# def run_n_record(filename: str, terminal: str) -> str:
#     exe = compile_program(filename)

#     runs = []
#     os.system(exe)

#     result = run_program(exe, "100")
#     print(result.stdout.lstrip("\n"))

#     render_terminal_png(
#         terminal,
#         repl["SCREENSHOTS"],
#         margin=30,
#         line_offset=6,
#         font="Consola",
#         min_line_length=30,
#     )

#     return "user: ".join(runs)


def add_code(key: str, *files: str) -> None:
    repl[key] = ""
    template = repl[key + "-TEMPLATE"]
    for ind, file in enumerate(files):
        path = Path(file)
        text = path.read_text()
        lines = text.splitlines()
        max_len = len(str(len(lines)))
        lines = [
            str(i) + " " * (max_len - len(str(i)) + 2) + ln
            for i, ln in enumerate(lines)
        ]
        repl[key] += template.format(
            number=ind + 1,
            filename=path.stem,
            filepath=path.name,
            code=html.escape("\n".join(lines)),
        )


def make_final_html(template: str, repl: dict, final: str) -> None:
    text = Path(template).read_text("utf-8")

    for name, value in repl.items():
        text = text.replace("{" + name + "}", str(value))

    Path(final).write_text(text, "utf-8")


def filter_files(directory: str, *filters: str) -> list[str]:
    glob = Path(directory).glob
    return [str(file) for filter in filters for file in glob(filter)]


if __name__ == "__main__":
    import fix_dir

    template = "./source/template.html"
    final = "./source/final.html"
    image = "./source/terminal.png"
    lab_folder = "../../mephi_labs/lab" + str(repl["LAB-ID"])

    add_code("PROGRAMS", *filter_files(lab_folder, "*.h", "*.c"))
    # repl["TEST-EXAMPLES"] = run_n_record(name, image)
    make_final_html(template, repl, final)
    print(render_pdf(final))
