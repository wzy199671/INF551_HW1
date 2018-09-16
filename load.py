import requests
import json
import re
import sys
class Obj:
    id=0
    motivation=""
    def __init__(self,x,y):
        self.id=x
        self.motivation=y

f=open("stopwords.txt")
stopword=f.read()
objs=[]
resultlist=[]
filename=sys.argv[1]
fileobject=open(filename)
payload=fileobject.read()
url ="https://inf551-13d00.firebaseio.com/motivation.json"
#res =requests.post(url,data=payload)
data = json.loads(payload)
num=len(data['prizes'])
for i in range(0,num):
    for j in range(0, len(data['prizes'][i]['laureates'])):
        if 'motivation' in data['prizes'][i]['laureates'][j]:
            objt = Obj(data['prizes'][i]['laureates'][j]['id'], data['prizes'][i]['laureates'][j]['motivation'].lower())
            objs.append(objt)
n=-1
di=dict()
for i in range(0,len(objs)):
    for j in range(0, len(re.findall(r"[\w]+", objs[i].motivation))) :

        if re.findall(r"[\w]+", objs[i].motivation)[j] not in stopword:
            if n  == -1 :
                di[re.findall(r"[\w]+", objs[i].motivation)[j]] = []
                di[re.findall(r"[\w]+", objs[i].motivation)[j]].append(objs[i].id)
                n=n+1
            else:
                flag=0
                for k in range(0,n+1):
                    if di.__contains__(re.findall(r"[\w]+", objs[i].motivation)[j]):
                        if objs[i].id not in di[re.findall(r"[\w]+", objs[i].motivation)[j]]:
                            di[re.findall(r"[\w]+", objs[i].motivation)[j]].append(objs[i].id)
                    else:
                        di[re.findall(r"[\w]+", objs[i].motivation)[j]]=[]
                        di[re.findall(r"[\w]+", objs[i].motivation)[j]].append(objs[i].id)
                        n = n + 1

    #print(resultlist[i].motivation)
    #print(resultlist[i].id)
print(di)
j = json.dumps(di)
res =requests.post(url,data=j)



