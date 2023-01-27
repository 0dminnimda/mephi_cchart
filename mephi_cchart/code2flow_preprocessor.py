import re

EMPTY_START = re.compile(r"\[label= \"\".+\]")
EMPTY_FILL = "shape= box, shape = point ,style= \"solid,filled\" fillcolor= \"#000000\",color=\"#000000\", width= 0.142857142857143,height= 0.142857142857143"


def process_dot(text: str) -> str:
    pass


# def process_code(code: str) -> str:
#     code = code.replace("*", "\\*")

