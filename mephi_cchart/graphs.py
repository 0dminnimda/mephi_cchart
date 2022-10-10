from pathlib import Path

import requests  # type: ignore


# possible types:
# https://github.com/yuzutech/kroki/blob/c60c44066ac38378be802c44fd5cca2cb54f530d/server/src/main/java/io/kroki/server/Server.java#L105
# https://github.com/yuzutech/kroki/blob/a853c5422f168cfdd04f331e04b92a6e21eae43a/tests/smoke/smoke.js#L1
def render_graph(source: str, type: str, format: str) -> bytes:
    json = {
        "diagram_source": source,
        "diagram_type": type,
        "output_format": format,
    }
    return requests.post("https://kroki.io/", json=json).content


def save_graph(source: str, type: str, path: str) -> None:
    file = Path(path)
    file.write_bytes(render_graph(source, type, file.suffix[1:]))


if __name__ == "__main__":
    import fix_dir
    # from public_data import repl

    # render_graph(repl["MERMAID-CODE"], "mermaid", "svg")

    gg = """
blockdiag admin {
  n0_0 [label = "maximize(n)"];
  n0_1 [label = "size = ceil(log10(n))"];
  n0_2 [label = "sorted = 0"];
  n0_3 [label = "sorted = 1"];
  n0_4 [label = "offset = 1"];
  n0_5 [label = "i = 0; i < size - 1; i++", shape = flowchart.loopin];
  n0_6 [label = "digit1 = n / (offset*10) % 10"];
  n0_7 [label = "digit2 = n / (offset   ) % 10"];
  n0_8 [label = "digit1 > digit2", shape = flowchart.condition];
  n0_9 [label = "n = n - digit1 * offset * 10 + digit2 * offset * 10"];
  n0_10 [label = "n = n - digit2 * offset      + digit1 * offset     "];
  n0_11 [label = "sorted = 0"];
  n0_12 [label = "offset *= 10"];
  n0_13 [label = "sorted != 1"];
  n0_0 -> n0_1;
  n0_1 -> n0_2;
  n0_2 -> n0_3;
  n0_3 -> n0_4;
  n0_4 -> n0_5
  n0_5 -> n0_13;
  n0_13 -> n0_3 [label = "true"];
  n0_5 -> n0_6;
  n0_6 -> n0_7;
  n0_7 -> n0_8;
  n0_8 -> n0_9  [label = "true"];
  n0_9 -> n0_10;
  n0_10 -> n0_11;
  n0_11 -> n0_12;
  n0_8 -> n0_12  [label = "false"];
  // n0_12 -> n0_5;
}
    """
    save_graph(gg, "blockdiag", "t.svg")
