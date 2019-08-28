import json
import datetime
import charactermaker


def handler(event, context):
    data = charactermaker.generateCharacter()
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}

def reprint():
    char = charactermaker.generateCharacter()
    for item in char:
        print(item + ": " + str(char[item]))

reprint()
