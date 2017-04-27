#import urllib
import urllib.request

class WebClinet:
    
    url=''

    def __init__(self,url):
        WebClinet.url=url
        
    def post(self,url_suffix,obj_data):
        
        req = urllib.request.Request(WebClinet.url+url_suffix)
        req.add_header(
            "Content-Type", "application/x-www-form-urlencoded;charset=utf-8")

        form_data = urllib.parse.urlencode(obj_data)
        form_data = form_data.encode('utf-8')

        res = urllib.request.urlopen(req, form_data)

        return res.read().decode()


data={"args": "{UserId:'bingosoft2',BelongDate:'2017-04-23'}"}
baseUrl='http://localhost:8081/Ashx/BingoTaskHandler.ashx?action='
action='DailyTask-GetTaskByDate'
json=WebClinet(baseUrl).post(action,data)

with open('./post_output.txt','w',encoding='utf-8') as file:
    file.write(json)

print(json)


