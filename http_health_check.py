#!"C:\Program Files\Python312\python.exe"

import requests

r = requests.get("http://10.1.100.100")

print(r.status_code)