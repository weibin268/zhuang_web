from webclient import WebClinet

import json

args=json.dumps({'UserId':'bingosoft2','Index':-2})
data={"args": args}
baseUrl='http://localhost:8081/Ashx/BingoTaskHandler.ashx?action='
action='Date-GetWeekFirstAndLastDates'
wc=WebClinet(baseUrl)
result=wc.post(action,data)


with open('./post_output.txt','w',encoding='utf-8') as file:
    file.write(result)

print(result)
