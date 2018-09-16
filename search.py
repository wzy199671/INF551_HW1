import requests
import json
import ast
import sys
url ="https://inf551-13d00.firebaseio.com/motivation.json"
data = requests.get(url)
payload=ast.literal_eval(data.text)[ast.literal_eval(data.text).keys()[0]]
num=len(sys.argv)

for i in range(1,num):
    if sys.argv[i] in payload:
        print(payload[sys.argv[i]])
    else:
        print("None")