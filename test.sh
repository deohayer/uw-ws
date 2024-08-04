#!/bin/bash
set -e
ROOT="$(realpath $(dirname "${BASH_SOURCE[0]}"))"

# Python-Ubuntu versions.
VERSIONS=(
    "3.6 18.04"
    "3.7 19.10"
    "3.8 20.04"
    "3.9 21.10"
    "3.10 22.04"
    "3.11 23.10"
    "3.12 24.04"
)
RESULTS=()
for i in "${!VERSIONS[@]}"; do
    # Split Python and Ubuntu versions.
    VERPAIR=(${VERSIONS[$i]})
    PYTHON="${VERPAIR[0]}"
    DOCKER="${VERPAIR[1]}"
    # Define directories for local, mount, and docker.
    ROOT_MOUNT="/tmp/root"
    OUT_LOCAL="${ROOT}/out/test/${DOCKER}"
    OUT_MOUNT="${ROOT_MOUNT}/out/test/${DOCKER}"
    OUT_HOME="\${HOME}/out"
    TEST_MOUNT="${ROOT_MOUNT}/test"
    TEST_HOME="\${HOME}/test"
    # Re-create local output directory specific to version
    rm -rf "${OUT_LOCAL}"
    mkdir -p "${OUT_LOCAL}"
    chmod 777 "${OUT_LOCAL}"
    # Print banner.
    echo "--------------------------------------------------"
    echo "Ubuntu ${DOCKER}"
    # Prepare Docker image.
    echo "Prepare image."
    docker build \
        --quiet \
        --build-arg VERSION=${DOCKER} \
        --tag uw:${DOCKER} \
        "${ROOT}/test" > /dev/null
    # Execute tests in Docker.
    echo "Execute tests."
    docker run \
        --rm \
        --volume="${ROOT}:${ROOT_MOUNT}" \
        uw:${DOCKER} \
        /bin/bash -c "true \
            &&  source \${HOME}/venv/bin/activate \
            &&  cp "$ROOT_MOUNT/uw/uw" "\$HOME/.local/bin/uw" \
            &&  chmod +x "\$HOME/.local/bin/uw" \
            &&  mkdir -p ${TEST_HOME} \
            &&  cp -RaT ${TEST_MOUNT} ${TEST_HOME} \
            &&  mkdir -p ${OUT_HOME} \
            &&  for TEST in \${HOME}/test/test_*.py; do \
                    export TEST_NAME=\$(basename \${TEST}); \
                    export TEST_LOG=${OUT_HOME}/\${TEST_NAME}.log; \
                    export TEST_TXT=${OUT_HOME}/\${TEST_NAME}.txt; \
                    python3 -m pytest -vv \${TEST} > \${TEST_LOG}; \
                    if [[ \$? != 0 ]]; then \
                        echo "FAIL" > \${TEST_TXT}; \
                        touch ${OUT_HOME}/failed; \
                        mv ${OUT_HOME}/failed ${OUT_MOUNT}/failed; \
                        chmod 777 ${OUT_MOUNT}/failed; \
                    else \
                        echo PASS > \${TEST_TXT}; \
                    fi; \
                    printf '%-43s : %s\\n' \${TEST_NAME} \$(cat \${TEST_TXT}); \
                    chmod 777 ${OUT_HOME}/\${TEST_NAME}.*; \
                    mv ${OUT_HOME}/\${TEST_NAME}.* ${OUT_MOUNT}/; \
                done \
            "
    set +e
    [[ -f "${OUT_LOCAL}/failed" ]]
    RESULTS[$i]=$?
    set -e
done
echo "--------------------------------------------------"
# Print global results.
GLOBAL=PASS
for i in "${!VERSIONS[@]}"; do
    VERPAIR=(${VERSIONS[$i]})
    PYTHON="${VERPAIR[0]}"
    DOCKER="${VERPAIR[1]}"
    if [[ ${RESULTS[$i]} == 1 ]]; then
        RESULT=PASS
    else
        RESULT=FAIL
        GLOBAL=FAIL
    fi
    printf 'Result %-36s : %s\n' ${DOCKER} ${RESULT}
done
printf 'Result %-36s : %s\n' "" ${GLOBAL}
