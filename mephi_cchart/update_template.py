import os
from pathlib import Path


def find_start_end(text: str, start: str, end: str) -> tuple[int, int]:
    s = text.find(start)
    if s != -1:
        s += len(start)
        e = text.find(end, s)
        if e != -1:
            return s, e
    return 0, 0


def get_between(text: str, start: str, end: str) -> str:
    s, e = find_start_end(text, start, end)
    return text[s:e]


def set_between(text: str, start: str, end: str, repl: str) -> str:
    s, e = find_start_end(text, start, end)
    return text[:s] + repl + text[e:]


def format_html(text: str) -> str:
    # from bs4 import BeautifulSoup

    # soup = BeautifulSoup(text)
    # return soup.prettify(formatter="html")

    # from lxml import etree, html

    # document_root = html.fromstring(text)
    # return etree.tostring(document_root, encoding="utf-8", pretty_print=True).decode("utf-8")

    return text


def implant_html(from_file: str, to_file: str) -> None:
    START = "<!-- TEMPLATE-START -->\n"
    END = "<!-- TEMPLATE-END -->\n"

    made = Path(from_file)
    target = Path(to_file)

    changed_html = get_between(made.read_text("utf-8"), START, END)
    new_html = set_between(target.read_text("utf-8"), START, END, changed_html)
    target.write_text(format_html(new_html), "utf-8")


def regenerate_template(
    to_file: str, from_file: str = "./build/html/template.html"
) -> None:
    os.system("make html")
    implant_html(from_file, to_file)


if __name__ == "__main__":
    import fix_dir

    template = "./source/template.html"
    regenerate_template(template)
