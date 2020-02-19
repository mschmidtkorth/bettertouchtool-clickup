import requests
import calendar, datetime
d = datetime.datetime.utcnow()

url = 'https://api.clickup.com/api/v2/list/1234567/task'
params = {}
# params['space_ids[]'] = '1234567' # Enable to receive task for additional Space
# params['project_ids[]'] = '1234567' # Enable to receive task for additional Project
params['list_ids[]'] = '1234567' # Enable to receive task for additional List
params['order_by'] = 'due_date'
params['due_date_lt'] = calendar.timegm(d.timetuple()) * 1000 # Add ms
headers = {}
headers['Authorization'] = 'pk_1234567'
headers['Content-Type'] = 'application/json'

r = requests.get(url, headers = headers)
result = r.json()

print(len(result['tasks']))
