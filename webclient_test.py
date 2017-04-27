from webclient import WebClinet

data={"args": "{UserId:'bingosoft2',BelongDate:'2017-04-23'}"}
baseUrl='http://localhost:8081/Ashx/BingoTaskHandler.ashx?action='
action='DailyTask-GetTaskByDate'
wc=WebClinet(baseUrl)
json=wc.post(action,data)


with open('./post_output.txt','w',encoding='utf-8') as file:
    file.write(json)

print(json)

