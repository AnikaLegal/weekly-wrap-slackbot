#!/bin/bash
set -e
HOST=13.211.109.142

echo ">>> Setting up server"
ssh root@${HOST} /bin/bash << EOF
    echo ">>> Creating deploy dir"
    mkdir -p /srv/slackbot
    if [ ! -d /srv/slackbot/env ]
    then
        echo ">>> Creating virtualenv"
        virtualenv -p python3 /srv/slackbot/env
    fi
EOF
echo ">>> Copying files"
scp ./requirements.txt root@${HOST}:/srv/slackbot/
scp ./run.py root@${HOST}:/srv/slackbot/
scp ./secrets.py root@${HOST}:/srv/slackbot/
scp ./setup-cron.py root@${HOST}:/srv/slackbot/
scp ./run.sh root@${HOST}:/srv/slackbot/
echo ">>> Installing requirements"
ssh root@${HOST} /bin/bash << EOF
    . /srv/slackbot/env/bin/activate
    pip3 install -r /srv/slackbot/requirements.txt
    echo ">>> Setting up cron job"
    python3 /srv/slackbot/setup-cron.py
EOF
echo ">>> Deployment finished"
