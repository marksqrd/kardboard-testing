# This simple fragment of code is inserted into Hudson to run the deploy process for both environments.

ssh vcs <<eoh

set -e

pushd /services/kardboard/kardboard-$KB_ENV/kardboard-$KB_ENV

function prcmd() {
        echo
            echo "[vcs.ddtc:\$PWD] Running cmd: \$BASH_COMMAND"
                echo
}

function prerr() {
        echo
            echo "Failed to complete deploy, red balling"
                echo
}

trap prerr ERR
trap prcmd DEBUG

source ../kardboard-venv-$KB_ENV/bin/activate

git clean -fdx

git pull 

python -OO -m compileall .
python -O -m compileall .

kardboard/runtests.py && echo "Unit tests passed!!!"

# Graceful shutdown of Celery/Celerybeat.  supervisord auto restarts.
pkill -f python.\*-$KB_ENV\$
# Graceful shutdown of WSGI deamons, this resets both test and prod code bases.  apache auto restarts.
pkill -2 -f python.\*-MEDLEY_DASH

eoh
