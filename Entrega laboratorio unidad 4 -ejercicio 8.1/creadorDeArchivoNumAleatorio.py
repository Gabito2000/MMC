import requests
import json

url = 'https://api.random.org/json-rpc/1/invoke'

apiKey = "1bb6d993-0b39-4f4d-afe4-493ff7b6d145" 

data = {'jsonrpc':'2.0','method':'generateIntegers','params': {'apiKey':apiKey,'n':10000,'min':0,'max':100000,'replacement':'true','base':10},'id':24565}

params = json.dumps(data)

response = requests.post(url,params)

print(response.text)

open('random2.txt', 'w').write(response.text)

# open the file and read the content to a json
with open('random2.txt', 'r') as filehandle:
    json_data = json.load(filehandle)

print (json_data['result']['random']['data'])

data = json_data['result']['random']['data']

# create a random3 file where the data is stored in a list with 5 columns
i = 0
with open('random3.txt', 'a') as filehandle:
    for listitem in data:
        filehandle.write('%s ' % listitem)
        if i == 4:
            filehandle.write('\n')
        i = (i + 1) % 5