import html
import os
import sys
from pathlib import Path

from html2pdf import render_pdf
from public_data import repl
from terminal import render_terminal_png
from tester import compile_program, run_program
from update_template import regenerate_template

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


def break_line_by_length(line: str, max_length: int = 90, sep: str = "\n") -> str:
    sub_lines = []
    while line:
        sub_lines.append(line[:max_length])
        line = line[max_length:]
    return sep.join(sub_lines)


def as_code(text: str) -> str:
    lines = text.splitlines()
    max_lineno_len = len(str(len(lines)))
    out_lines = []
    for i, line in enumerate(lines):
        prefix = str(i) + " " * (max_lineno_len - len(str(i)) + 2)
        line = prefix + break_line_by_length(line, sep="\n" + " " * len(prefix))
        out_lines.append(line)
    return html.escape("\n".join(out_lines))


def add_code(key: str, *files: str) -> None:
    repl[key] = ""
    template = repl[key + "-TEMPLATE"]
    for ind, file in enumerate(files):
        path = Path(file)
        repl[key] += template.format(
            number=ind + 1,
            filename=path.stem,
            filepath=path.name,
            code=as_code(path.read_text("utf-8")),
        )


def escape_custom_html(string: str) -> str:
    return string.replace("\<", html.escape("<")).replace("\>", html.escape(">"))


def make_final_html(template: str, repl: dict, final: str) -> None:
    text = Path(template).read_text("utf-8")

    for name, value in repl.items():
        text = text.replace("{" + name + "}", escape_custom_html(str(value)))

    Path(final).write_text(text, "utf-8")


def filter_files(directory: str, *filters: str) -> list[str]:
    glob = Path(directory).glob
    return [str(file) for filter in filters for file in glob(filter)]


def get_test_cases(directory: str, run: bool = True) -> str:
    path = Path(directory)

    if run:
        os.system(f"{sys.executable!r} {path / 'test.py'} make_cases")

    # namespace = {"__builtins__": __builtins__, "__name__": ""}
    # exec((path / "test.py").read_text("utf-8"), namespace, {})
    # namespace["main"]([__file__, "make_cases"])  # type: ignore

    return (path / "test_cases.txt").read_text("utf-8")


def get_test_output(directory: str, run: bool = True) -> str:
    path = Path(directory)

    if run:
        os.system(f"{sys.executable!r} {path / 'test.py'}")

    return (path / "test.output").read_text("utf-8")


if __name__ == "__main__":
    import fix_dir

    template = "./source/template.html"
    final = "./source/final.html"
    image = "./source/terminal.png"
    lab_folder = "../../mephi_labs/lab" + str(repl["LAB-ID"])

    regenerate_template(template)

    add_code("PROGRAMS", *filter_files(lab_folder, "*.h", "*.c"))
    add_code("TESTER", *filter_files(lab_folder, "test.py"))

    repl["TEST-EXAMPLES"] = (
        f"<pre>\n" + as_code(get_test_output(lab_folder)) + "</pre>"
        # f"<pre>\n" + as_code(get_test_cases(lab_folder, run=False)) + "</pre>"
    )
    # repl["TEST-EXAMPLES"] = run_n_record(name, image)

    make_final_html(template, repl, final)
    # print(render_pdf(final))
    print("End")
