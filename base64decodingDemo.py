import base64
import json
from itertools import permutations
import requests

urlObject = ["lwUUxTZS1nQUx1eFBKanJPVEZ2MnpCX0FSQVFBbEtGRHlYdTVS","bGlzbGFtJTQwZ21haWwuY29tLWRkYUN6WERJVno5YUYydkcmZW","50cnkuMTk1NDA1MDMwND1hbWVlcnVsaXNsYW1AZ21haWwuY29t","b2xHcGxablNvLUw2akFBL3ZpZXdmb3JtP3VzcD1wcF91cmwmZW","aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vZm9ybXMvZC9lLzFGQU","50cnkuMTAxMzkwOTE1PW9neTk1dWp0MDcxR3BxbUctYW1lZXJ1"]

urllen = len(urlObject)


allPermutations = list(permutations(urlObject, 6))
perinlist = list(map(list, allPermutations))
print(len(perinlist))
value_list =[]
for j in perinlist:
    coded_string = j[0]+j[1]+j[2]+j[3]+j[4]+j[5]
    value = base64.b64decode(coded_string)
    value_list.append(value)

for i in value_list: 
    try:
        response = requests.get(i.decode('utf-8'))
        if(response.status_code == 200 ):
            print(i)
    except UnicodeDecodeError:
        pass
    except requests.exceptions.InvalidSchema:
        pass
    finally:
        pass
