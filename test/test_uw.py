from .utilities import *

def test_0000():
    # --version
    assert sh("uw --version", cap=True).out == VERSION

def test_0001():
    # --help (outside a workspace)
    assert sh("uw --help", cap=True).out == str(
        f"uw ...\n"
        f"\n"
        f"Uniform Workspace version {VERSION[:-1]}.\n"
        f"\n"
        f"Commands:\n"
        f"  app-update    Download the latest version.\n"
        f"  app-setup     Modify .bashrc to register uw completion and aliases.\n"
        f"  app-reset     Revert changes to .bashrc made by app-setup.\n"
        f"  init          Create an empty workspace.\n"
        f"\n"
        f"Optional arguments:\n"
        f"  --bashrc     Setup completion and aliases, then exit.\n"
        f"  --version    Print the version, then exit.\n"
        f"  --help       Print the help text, then exit.\n"
        f"\n"
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
        f"uw ...\n"
        f"\n"
        f"Uniform Workspace version {VERSION[:-1]}.\n"
        f"\n"
        f"Commands:\n"
        f"  uwa           Attach to the hardware.\n"
        f"  uwd           Detach from the hardware.\n"
        f"  uwp           Manage the power state of the hardware.\n"
        f"  uwc           Copy file between the local machine and the hardware.\n"
        f"  uws           The hardware shell.\n"
        f"  uwf           Fetch the software.\n"
        f"  uwb           Build the software.\n"
        f"  uwi           Install the software.\n"
        f"  uwt           Test the software.\n"
        f"  uwx           Extensions - custom actions.\n"
        f"  app-update    Download the latest version.\n"
        f"  app-setup     Modify .bashrc to register uw completion and aliases.\n"
        f"  app-reset     Revert changes to .bashrc made by app-setup.\n"
        f"  init          Create an empty workspace.\n"
        f"\n"
        f"Optional arguments:\n"
        f"  --bashrc     Setup completion and aliases, then exit.\n"
        f"  --version    Print the version, then exit.\n"
        f"  --help       Print the help text, then exit.\n"
        f"\n"
    )
