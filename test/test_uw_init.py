from .utilities import *

WS=f"{HOME}/ws_uw_init"

def check_uw(ws):
    assert os.path.exists(f"{ws}/.uw")
    assert os.path.exists(f"{ws}/.uw/env.sh")
    assert os.path.exists(f"{ws}/.uw/uwa.sh")
    assert os.path.exists(f"{ws}/.uw/uwd.sh")
    assert os.path.exists(f"{ws}/.uw/uwp.sh")
    assert os.path.exists(f"{ws}/.uw/uws.sh")
    assert os.path.exists(f"{ws}/.uw/uwc.sh")
    assert os.path.exists(f"{ws}/.uw/uwf.sh")
    assert os.path.exists(f"{ws}/.uw/uwb.sh")
    assert os.path.exists(f"{ws}/.uw/uwi.sh")
    assert os.path.exists(f"{ws}/.uw/uwt.sh")
    assert os.path.exists(f"{ws}/.uw/uwx.sh")

def test_0000():
    # --version
    assert sh("uw init --version", cap=True).out == VERSION

def test_0001():
    # --help
    assert sh("uw init --help", cap=True).out == str(
        "uw init [DIR]\n"
        "\n"
        "Create an empty workspace.\n"
        "\n"
        "Positional arguments:\n"
        "  DIR    A directory to initialize, defaults to PWD.\n"
        "\n"
        "Optional arguments:\n"
        "  --help       Print the help text, then exit.\n"
        "  --version    Print the version, then exit.\n"
    )

def test_0002():
    # Default case.
    sh(f"true"
        f" && rm -rf {WS}"
        f" && mkdir -p {WS}"
        f" && cd {WS}"
        f" && uw init"
        f";")
    check_uw(WS)

def test_0003():
    # Default case failure.
    out = sh(f"true"
        f" && rm -rf {WS}"
        f" && mkdir -p {WS}/.uw"
        f" && cd {WS}"
        f" && uw init"
        f";", cap=True, chk=False).out
    sh(f"rm -r {WS}")
    assert out == f"uw init: Already initialized: {WS}\n"

def test_0004():
    # Specific case.
    out = sh(f"true"
        f" && rm -rf {WS}"
        f" && uw init {WS}"
        f";", cap=True, chk=False).out
    check_uw(WS)

def test_0005():
    # Specific case failure.
    out = sh(f"true"
        f" && rm -rf {WS}"
        f" && mkdir -p {WS}/.uw"
        f" && uw init {WS}"
        f";", cap=True, chk=False).out
    sh(f"rm -r {WS}")
    assert out == f"uw init: Already initialized: {WS}\n"
