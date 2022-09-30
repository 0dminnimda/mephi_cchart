import os
from pathlib import Path

import pdfkit

os.chdir(str(Path(__file__).absolute().parent))

# print("wait 20 secs")
options = {
    "enable-local-file-access": None,
    # "enable-javascript": None,
    # "javascript-delay": 20000,
}
config = pdfkit.configuration(wkhtmltopdf="wkhtmltox/bin/wkhtmltopdf.exe")
pdfkit.from_file(
    "build/html/index.html", "out.pdf", configuration=config, options=options, verbose=True
)
