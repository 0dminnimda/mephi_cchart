from PIL import Image, ImageDraw, ImageFont


def render_terminal_png(
    path: str,
    message: str,
    *,
    color: tuple[int, int, int] = (255, 255, 255),
    background: tuple[int, int, int] = (0, 0, 0),
    size: int = 40,
    margin: int = 0,
    line_offset: int = 0,
    min_line_length: int = 10,
    font: str = "arial"
) -> None:
    message = message.strip("\n")
    lines = message.split("\n")

    imgfont = ImageFont.truetype(font.lower() + ".ttf", size=size)

    longest_line = max(lines, key=len)
    longest_line += " " * (min_line_length - len(longest_line))

    left, top, right, bottom = imgfont.getbbox(longest_line)
    width = right - left
    height = bottom - top

    img = Image.new(
        "RGB",
        (
            width + margin * 2 - left,
            (height + line_offset) * len(lines) + margin * 2 - top,
        ),
        color=background,
    )
    imgDraw = ImageDraw.Draw(img)

    for i, line in enumerate(lines):
        imgDraw.text(
            (margin - left, margin - top + (height + line_offset) * i),
            line,
            font=imgfont,
            fill=color,
        )
    img.save(path)


if __name__ == "__main__":
    import fix_dir
    from public_data import repl

    image = "./source/terminal.png"

    # Consolas, Monaco, Lucida Console, Liberation Mono, DejaVu Sans Mono,
    # Bitstream Vera Sans Mono, Courier New, monospace
    render_terminal_png(
        image, repl["SCREENSHOTS"], margin=30, line_offset=6, font="Consola"
    )
