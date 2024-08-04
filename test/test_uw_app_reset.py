from .utilities import *

def test_0000():
    # --version
    assert sh("uw app-reset --version", cap=True).out == VERSION

def test_0001():
    # --help
    assert sh("uw app-reset --help", cap=True).out == str(
        "uw app-reset\n"
        "\n"
        "Revert changes to .bashrc made by app-setup.\n"
        "\n"
        "Optional arguments:\n"
        "  --help       Print the help text, then exit.\n"
        "  --version    Print the version, then exit.\n"
        "\n"
    )

def test_0002():
    file = open(f"{HOME}/.bashrc")
    sh("uw app-setup")
    assert UW_SOURCE in file.readlines()
    sh("uw app-reset")
    assert UW_SOURCE not in file.readlines()
