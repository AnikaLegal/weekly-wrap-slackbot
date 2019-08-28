"""
To remove existing jobs

import crontab
cron = crontab.CronTab(user='root')
for job in cron.find_command("slackbot"):
    cron.remove(job)

cron.write()

See https://www.freeformatter.com/cron-expression-generator-quartz.html
"""
from crontab import CronTab

print("Setting up slackbot cron job")
cron = CronTab(user="root")

existing_jobs = [j for j in cron.find_command("slackbot")]
if not existing_jobs:
    print("\nCreating new slackbot cron job")
    job = cron.new(command="bash /srv/slackbot/run.sh")
    # Run every saturday at the start of the day
    job.minute.on(0)
    job.hour.on(0)
    job.dow.on("SUN")
    print("New job created:", job)
    print("Job executions per year: ", job.frequency())
    assert job.is_valid(), "Job is not valid"
    cron.write()
else:
    print("\nSlackbot cron job already exists:", existing_jobs)

print("Done setting up cron job")
