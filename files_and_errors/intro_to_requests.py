import requests
import json
from pprint import pprint

post_code_req = requests.get("http://api.postcodes.io/postcodes/aghodgio")

print(post_code_req.json())

# json_body = json.dumps({"postcodes": ["kwjfgijsfbgsfb"]})
# headers = {"Content-Type": "application/json"}
#
# post_multi_req = requests.post("http://api.postcodes.io/postcodes", headers=headers, data=json_body)
#
# pprint(post_multi_req.json())
