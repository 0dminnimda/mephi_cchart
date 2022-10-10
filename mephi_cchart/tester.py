import io
import subprocess
from distutils.ccompiler import new_compiler, CCompiler


def compile_program(filename: str) -> str:
    # linux doesn't care about the extension and windows won't work otherwise
    executable = f"compilation/{'.'.join(filename.split('.')[:-1])}.exe"

    compiler = new_compiler()
    objects = compiler.compile([filename], output_dir="compilation")
    compiler.link(
        CCompiler.EXECUTABLE, objects, executable  # type: ignore[attr-defined]
    )

    return executable


def run_program(executable: str, input: str) -> subprocess.CompletedProcess:
    result = subprocess.run(
        [executable],
        input=input,
        text=True,
        # capture_output=True,
    )
    return result


if __name__ == "__main__":
    import fix_dir

    name = "myprogram.c"
    exe = compile_program(name)
    result = run_program(exe, "100")
    # print(result.stdout.lstrip("\n"))

    # exe = "compilation\myprogram.exe"
    # p = subprocess.Popen([exe], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # for line in iter(p.stdout.readline, b""):
    #     print(">>> " + line.rstrip())

    # p = subprocess.Popen(
    #     [exe],
    #     shell=True,
    #     bufsize=64,
    #     stdin=subprocess.PIPE,
    #     stderr=subprocess.PIPE,
    #     stdout=subprocess.PIPE,
    # )

    # print(p.communicate(b"100"))

    # for line in p.stdout:
    #     print(">>> " + str(line.rstrip()))
    #     p.stdout.flush()
