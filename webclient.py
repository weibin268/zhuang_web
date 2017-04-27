#import urllib
import urllib.request

class WebClinet:

    url=''

    def __init__(self,url):
        WebClinet.url=url
        
    def post(self,action,objData):
        
        req = urllib.request.Request(WebClinet.url+action)
        req.add_header(
            "Content-Type", "application/x-www-form-urlencoded;charset=utf-8")

        data = urllib.parse.urlencode(objData)
        data = data.encode('utf-8')

        res = urllib.request.urlopen(req, data)

        return res.read().decode()


data={"args": "{UserId:'bingosoft2',BelongDate:'2017-04-23'}"}
baseUrl='http://localhost:8081/Ashx/BingoTaskHandler.ashx?action='
action='DailyTask-GetTaskByDate'
json=WebClinet(baseUrl).post(action,data)

print(json)


