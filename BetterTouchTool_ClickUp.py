#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
import requests
import calendar, datetime

d = datetime.datetime.utcnow()
url = 'https://api.clickup.com/api/v2/team/1234567/task'
params = {}
# params['space_ids[]'] = '1234567' # Enable to receive task for additional space
params['project_ids[]'] = '1234567'
#params['list_ids[]'] = '1234567' # Enable to receive task for additional list
params['order_by'] = 'due_date'
params['due_date_lt'] = calendar.timegm(d.timetuple()) * 1000 # Add ms
headers = {}
headers['Authorization'] = 'pk_1234567'
headers['Content-Type'] = 'application/json'

r = requests.get(url, params = params, headers = headers)

result = r.json()

for task in result['tasks']:
	if task['name']:
		name = task['name']
		bgColor = '133,115,224,255'
		fColor = '255,255,255,255'
		if task['priority'] and 'id' in task['priority']:
			if task['priority']['id'] == "1":
				bgColor = '255,0,0,255'
			if task['priority']['id'] == "2":
				bgColor = '255,255,0,255'
				fColor = '0,0,0,255'
		print(u'{\"text\":\"' + name + '\", \"background_color\": \"' + bgColor + '\", \"font_color\": \"' + fColor + '\", \"font_size\": 10}')
	break
