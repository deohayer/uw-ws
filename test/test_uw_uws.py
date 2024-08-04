from .utilities import *

WS=f"{HOME}/ws_uw"
CMD="uws"
HELP=str(
    "uw uws [TGT] [CMD...]\n"
    "\n"
    "The hardware shell.\n"
    "\n"
    "Positional arguments:\n"
    "  CMD    A command to execute. If empty - start an interactive session.\n"
    "  TGT    A target for shell.\n"
    "\n"
    "Optional arguments:\n"
    "  --help       Print the help text, then exit.\n"
    "  --version    Print the version, then exit.\n"
)

class Test:
    def setup_method(self):
        sh(f"uw init {WS}")

    def teardown_method(self):
        sh(f"rm -r {WS}")

    def test_0000(self):
        # --version
        assert sh(f"cd {WS} && uw {CMD} --version", cap=True).out == VERSION

    def test_0001(self):
        # --help
        assert sh(f"cd {WS} && uw {CMD} --help", cap=True).out == HELP

    def test_0002(self):
        # Default case.
        assert sh(f"cd {WS} && uw {CMD}", cap=True, chk=False).out == "Not implemented.\n"
