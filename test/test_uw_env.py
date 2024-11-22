from .utilities import *

WS=f"{HOME}/ws_env"

class Test:
    def setup_method(self):
        sh(f"uw init {WS}")
        # Customize env.sh to contain VAR.
        with open(f"{WS}/.uw/env.sh", "w+") as file:
            file.write('VAR="My variable"')
        # Customize uwx.sh: help, TGT values, print VAR.
        with open(f"{WS}/.uw/uwx.sh", "w+") as file:
            file.write(
                '#!/usr/bin/env bash\n' \
                'declare -r UW_HELP="A customized help text."\n'
                'declare -ra UW_TGTS=("command" "cmd")\n'
                'uw_init "$@"\n'
                '\n'
                'echo "$VAR"\n'
                'printf "%s\n" "$@"\n'
            )

    def teardown_method(self):
        sh(f"rm -r {WS}")

    def test_0001(self):
        # --help
        assert sh(f"cd {WS} && uw uwx --help", cap=True).out == str(
            "uw uwx [TGT...]\n"
            "\n"
            "A customized help text.\n"
            "\n"
            "Positional arguments:\n"
            "  TGT    Targets for the operation.\n"
            "          * command\n"
            "          * cmd\n"
            "\n"
            "Optional arguments:\n"
            "  --help       Print the help text, then exit.\n"
            "  --version    Print the version, then exit.\n"
            "\n"
        )

    def test_0002(self):
        # Execution - no args.
        assert sh(f"cd {WS} && uw uwx", cap=True).out == "My variable\n\n"

    def test_0003(self):
        # Execution - single arg.
        assert sh(f"cd {WS} && uw uwx cmd", cap=True).out == str(
            "My variable\n"
            "cmd\n"
        )

    def test_0004(self):
        # Execution - multiple args.
        assert sh(f"cd {WS} && uw uwx cmd command command", cap=True).out == str(
            "My variable\n"
            "cmd\n"
            "command\n"
            "command\n"
        )
