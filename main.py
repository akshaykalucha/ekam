import xmltodict

import json


INPUT_FILE = "tickets.xml"
OUTPUT_FILE = "output.json"

dataDict = {}

with open(INPUT_FILE, encoding='utf-16') as f:
    dataDict = xmltodict.parse(f.read())

records = dataDict['Records']

finalRecordStr = "{\"Records\": {\n"

for key, value in records.items():

    if key == "Record":
        recordStr = f"\"{key}\":[\n"

        for recordItem in value:
            recordStr += json.dumps(recordItem) + ",\n"
        
        recordStr = recordStr[:-2] + "\n]"

        finalRecordStr += recordStr + ",\n"

    else:
        restStr = json.dumps(value)

        restStr = f"\"{key}\":{restStr}"

        finalRecordStr += restStr + ",\n"
        print()
    
    print()

finalRecordStr = finalRecordStr[:-2] + "\n}}"

with open(OUTPUT_FILE, 'w') as f:
    f.write(finalRecordStr)


print(dataDict)
