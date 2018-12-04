
# https://apscheduler.readthedocs.io/en/latest/userguide.html
# https://github.com/agronholm/apscheduler/tree/master/examples

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
 
import datetime
import time
import logging
 
def job_function():
    print "Hello World" + " " + str(datetime.datetime.now())
 
if __name__ == '__main__':
    log = logging.getLogger('apscheduler.executors.default')
    log.setLevel(logging.INFO)  # DEBUG
 
    fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
    h = logging.StreamHandler()
    h.setFormatter(fmt)
    log.addHandler(h)
 
    print('start to do it')
 
    sched = BlockingScheduler()
    
    @sched.scheduled_job('interval', seconds=3)
    def timed_job():
      print('This job is run every three minutes.')
 
    @sched.scheduled_job('cron', day_of_week='mon-fri', hour='0-9', minute='30-59', second='*/3')
    def scheduled_job():
      print('This job is run every weekday at 5pm.')
 
    # Schedules job_function to be run on the third Friday
    #  of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
    sched.add_job(job_function, 'cron', day_of_week='mon-fri', hour='0-9', minute="*", second="*/4")
    
    # scheduler.remove_job('my_job_id')
 
    sched.start()
