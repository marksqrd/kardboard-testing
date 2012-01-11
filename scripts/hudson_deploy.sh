#!/bin/sh 
# Hudson runs this version in master directly for deployments.
# first supplied argument is the environment name as passed from Hudson. (test or prod)

set -e

KB_ENV=$1
[ -z "$KB_ENV" ] && KB_ENV="prod"

pushd /services/kardboard/kardboard-$KB_ENV/kardboard-$KB_ENV

if [[ $KB_ENV == prod ]]; then
    GIT_ORIGIN="master"
else
    GIT_ORIGIN="$KB_ENV"
fi

function prcmd() {
    echo
    echo "[vcs.ddtc:\$PWD] Running cmd: $BASH_COMMAND"
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

git diff origin/$GIT_ORIGIN | grep . && { echo "Failed to deploy"; exit 1; }

python -OO -m compileall .
python -O -m compileall .

kardboard/runtests.py && echo "Unit tests passed!!!"

# Graceful shutdown of Celery/Celerybeat.  supervisord auto restarts.
pkill -f python.\*-$KB_ENV\$
# Graceful shutdown of WSGI deamons, this resets both test and prod code bases.  apache auto restarts.
pkill -2 -f python.\*-MEDLEY_DASH
