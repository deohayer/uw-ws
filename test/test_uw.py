from .utilities import *

def test_0000():
    # --version
    assert sh("uw --version", cap=True).out == VERSION

def test_0001():
    # --help (outside a workspace)
    assert sh("uw --help", cap=True).out == str(
        "uw ...\n"
        "\n"
        "Uniform Workspace version 0.7.2.\n"
        "\n"
        "Commands:\n"
        "  app-update    Download the latest version.\n"
        "  app-setup     Modify .bashrc to register uw completion and aliases.\n"
        "  app-reset     Revert changes to .bashrc made by app-setup.\n"
        "  init          Create an empty workspace.\n"
        "\n"
        "Optional arguments:\n"
        "  --bashrc     Setup completion and aliases, then exit.\n"
        "  --version    Print the version, then exit.\n"
        "  --help       Print the help text, then exit.\n"
        "\n"
    )

def test_0002():
    # --help (inside a workspace)
    ws = f"{HOME}/ws_test_uw"
    out = sh("true"
        f" && mkdir -p {ws}/.uw"
        f" && cd {ws}"
        f" && uw --help"
        f" && rm -r {ws}"
        f";", cap=True).out
    assert out == str(
        "uw ...\n"
        "\n"
        "Uniform Workspace version 0.7.2.\n"
        "\n"
        "Commands:\n"
        "  uwa           Attach to the hardware.\n"
        "  uwd           Detach from the hardware.\n"
        "  uwp           Manage the power state of the hardware.\n"
        "  uwc           Copy file between the local machine and the hardware.\n"
        "  uws           The hardware shell.\n"
        "  uwf           Fetch the software.\n"
        "  uwb           Build the software.\n"
        "  uwi           Install the software.\n"
        "  uwt           Test the software.\n"
        "  uwx           Extensions - custom actions.\n"
        "  app-update    Download the latest version.\n"
        "  app-setup     Modify .bashrc to register uw completion and aliases.\n"
        "  app-reset     Revert changes to .bashrc made by app-setup.\n"
        "  init          Create an empty workspace.\n"
        "\n"
        "Optional arguments:\n"
        "  --bashrc     Setup completion and aliases, then exit.\n"
        "  --version    Print the version, then exit.\n"
        "  --help       Print the help text, then exit.\n"
        "\n"
    )
