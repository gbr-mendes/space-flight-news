from apscheduler.schedulers.blocking import BlockingScheduler
from core import models

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    models.Test.objects.create(name='Teste')


sched.start()