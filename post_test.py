#import urllib
import urllib.request

url = "http://localhost:8081/Ashx/BingoTaskHandler.ashx?action="
action = "DailyTask-GetTaskByDate"

fullUrl = url + action

req = urllib.request.Request(fullUrl)
req.add_header(
    "Content-Type", "application/x-www-form-urlencoded;charset=utf-8")

data = urllib.parse.urlencode(
    {"args": "{UserId:'bingosoft2',BelongDate:'2017-04-23'}"})
data = data.encode('utf-8')

res = urllib.request.urlopen(req, data)

fPath = "./post_output.txt"

outFile = open(fPath, "w", encoding="utf-8")

try:
    outFile.write(res.read().decode())
finally:
    outFile.close()
