from .utilities import *

def test_0000():
    # --version
    assert sh("uw app-setup --version", cap=True).out == VERSION

def test_0001():
    # --help
    assert sh("uw app-setup --help", cap=True).out == str(
        "uw app-setup\n"
        "\n"
        "Modify .bashrc to register uw completion and aliases.\n"
        "\n"
        "Optional arguments:\n"
        "  --help       Print the help text, then exit.\n"
        "  --version    Print the version, then exit.\n"
    )

def test_0002():
    sh("uw app-setup")
    file = open(f"{HOME}/.bashrc")
    assert UW_SOURCE in file.readlines()
