import os
from pathlib import Path

import requests

os.chdir(str(Path(__file__).absolute().parent))


def render(source: str, path: str) -> None:
    file = Path(path)
    resp = requests.post(
        "https://kroki.io/",
        json={
            "diagram_source": source,
            "diagram_type": "mermaid",
            "output_format": file.suffix[1:],
        },
    )
    file.write_bytes(resp.content)


g = """
flowchart RL
   subgraph SG0 [" "]
      direction TB
      n0_0["maximize(n)"] --> n0_1["size = ceil(log10(n))"]
      n0_1 --> n0_2["sorted = 0"]
      n0_2 --> n0_3["sorted = 1"]
      n0_3 --> n0_4["offset = 1"]
      n0_4 --> n0_5{{"i = 0; i < size - 1; i++"}}
      n0_5 --> n0_13{"sorted != 1"}
      n0_13 --> |true| n0_3
      n0_5 --> n0_6["digit1 = n / (offset*10) % 10"]
      n0_6 --> n0_7["digit2 = n / (offset   ) % 10"]
      n0_7 --> n0_8{"digit1 > digit2"}
      n0_8 --> |true| n0_9["n = n - digit1 * offset * 10 + digit2 * offset * 10"]
      n0_9 --> n0_10["n = n - digit2 * offset      + digit1 * offset     "]
      n0_10 --> n0_11["sorted = 0"]
      n0_11 --> n0_12["offset *= 10"]
      n0_8 --> |false| n0_12
      n0_12 --> n0_5
       
   end
"""
render(g, "source/_static/graph.svg")
