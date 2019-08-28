# Weekly Wrap Slackboot

A simple bot that periodically posts a reminder to a Slack channel via a webhook.

To run you need to add a `secrets.py` file with the slack webhooks URL

```python
PROD_WEBHOOK_URL = "https://hooks.slack.com/services/xxx/yyy/zzz"
TEST_WEBHOOK_URL = "https://hooks.slack.com/services/xxx/yyy/zzz"
```

then install the required Python libraries, and run the script

```bash
pip3 install -r requirements.txt
python3 ./run.py
```

to deploy, edit `HOST` in `./deploy.sh` to point to a server that you can SSH into, and run the script

```bash
./deploy.sh
```
