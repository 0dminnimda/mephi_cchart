import shlex
import subprocess
from pathlib import Path
from typing import Optional


def render_pdf_pdfkit(html_path: str, pdf_path: str) -> None:
    import pdfkit  # type: ignore

    # print("wait 20 secs")
    options = {
        "enable-local-file-access": None,
        # "enable-javascript": None,
        # "javascript-delay": 20000,
    }
    config = pdfkit.configuration(wkhtmltopdf="wkhtmltox/bin/wkhtmltopdf.exe")
    pdfkit.from_file(
        html_path, pdf_path, configuration=config, options=options, verbose=True
    )


def render_pdf(html_path: str, pdf_path: Optional[str] = None):
    if pdf_path is None:
        pdf_path = str(Path(html_path).with_suffix(".pdf"))

    exe = "ChromeHtmlToPdf/ChromeHtmlToPdfConsole.exe"
    args = shlex.split(f"{exe} --input {html_path} --output {pdf_path}")
    return subprocess.call(args)


if __name__ == "__main__":
    import fix_dir

    template = "./source/template.html"
    final = "./source/final.html"

    print(render_pdf(final))

    # render_pdf_pdfkit("build/html/index.html", "out.pdf")
