import os
import shlex

from blockdiag.command import main

os.chdir(os.path.dirname(__file__))

main(shlex.split("ggg.diag -T SVG --debug"))
