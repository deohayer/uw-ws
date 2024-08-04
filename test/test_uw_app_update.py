from .utilities import *

def test_0000():
    # --version
    assert sh("uw app-update --version", cap=True).out == VERSION

def test_0001():
    # --help
    assert sh("uw app-update --help", cap=True).out == str(
        "uw app-update\n"
        "\n"
        "Download the latest version.\n"
        "\n"
        "Optional arguments:\n"
        "  --help       Print the help text, then exit.\n"
        "  --version    Print the version, then exit.\n"
        "\n"
    )

def test_0002():
    sh(f"cp $(which uw) {HOME}/uw")
    sh(f"uw app-update")
    sh(f"cp $(which uw) {HOME}/uw-upd")
    sh(f"cp {HOME}/uw $(which uw)")
    sh(f"curl -o {HOME}/uw-new https://raw.githubusercontent.com/deohayer/uw/main/uw")
    md5_1 = sh(f"md5sum {HOME}/uw-upd").out
    md5_2 = sh(f"md5sum {HOME}/uw-new").out
    assert md5_1 == md5_2
