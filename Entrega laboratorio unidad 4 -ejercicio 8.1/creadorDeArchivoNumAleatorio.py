import requests
import json

# url = 'https://api.random.org/json-rpc/1/invoke'

# data = {'jsonrpc':'2.0','method':'generateIntegers','params': {'apiKey':'8c57eec1-5c5c-45ae-ba76-58bb522867ee','n':10000,'min':0,'max':100000,'replacement':'true','base':10},'id':24565}

# params = json.dumps(data)

# response = requests.post(url,params)

# print(response.text)

# open('random2.txt', 'w').write(response.text)

# open the file and read the content to a json
with open('random2.txt', 'r') as filehandle:
    json_data = json.load(filehandle)

print (json_data['result']['random']['data'])

data = json_data['result']['random']['data']

# create a random3 file where the data is stored in a list with 5 columns
i = 0
with open('random3.txt', 'w') as filehandle:
    for listitem in data:
        filehandle.write('%s ' % listitem)
        if i == 4:
            filehandle.write('\n')
        i = (i + 1) % 5

# 32557,97916,94301,2622,80324,76834,83438,95380,53903,88078