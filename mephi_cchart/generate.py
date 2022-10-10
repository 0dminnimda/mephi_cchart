from pathlib import Path

from html2pdf import render_pdf
from public_data import repl
from terminal import render_terminal_png


def make_final_html(template: str, terminal: str, repl: dict, final: str) -> None:
    text = Path(template).read_text("utf-8")

    for name, value in repl.items():
        text = text.replace("{" + name + "}", str(value))

    Path(final).write_text(text, "utf-8")

    render_terminal_png(
        terminal,
        repl["SCREENSHOTS"],
        margin=30,
        line_offset=6,
        font="Consola",
        min_line_length=30,
    )


if __name__ == "__main__":
    import fix_dir

    template = "./source/template.html"
    final = "./source/final.html"
    image = "./source/terminal.png"

    make_final_html(template, image, repl, final)
    print(render_pdf(final))
