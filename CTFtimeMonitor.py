# -*- coding: utf-8 -*-

import arrow
import requests
import json
import telepot
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()
group = group_integer_id
bot = telepot.Bot('api-here')

@sched.scheduled_job('interval', weeks=1)
def sendCTF():
    print 'Sending'
    now = arrow.now()
    past = now.replace(day=+30)
    api = "https://ctftime.org/api/v1/events/?limit=%d&start=%d&finish=%d" % (3,now.timestamp,past.timestamp)
    r = requests.get(api)
    results = json.loads(r.content)

    for result in results:
        msg = ''
        msg += 'Organizer : %s\n' % result['organizers'][0]['name']
        msg += 'Title: %s\n' % result['title']
        msg += 'Description\n'
        msg += result['description']
        msg += '\CTF Website: %s\n' % result['url']
        msg += 'CTF Style: %s\n' % result['format']
        msg += 'CTF Start: %s\n' % result['start']
        msg += 'CTF End: %s\n' % result['finish']
        bot.sendMessage(group,msg)

def main():
    sched.start()

while 1:
    main()
