import urllib
import urllib.request

url = "http://localhost:8081/Ashx/BingoTaskHandler.ashx?action="+"DailyTask-GetTaskByDate"

req = urllib.request.Request(url)
req.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")

data = urllib.parse.urlencode({"args":"{UserId:'bingosoft2',BelongDate:'2017-04-23'}"})
data = data.encode('utf-8')

res =urllib.request.urlopen(req,data)

print (res.read())
