#import urllib
import urllib.request

class WebClinet:

    def __init__(self,url):
        self.url=url
        
    def post(self,url_suffix,obj_data):
        
        req = urllib.request.Request(self.url+url_suffix)
        req.add_header(
            "Content-Type", "application/x-www-form-urlencoded;charset=utf-8")

        form_data = urllib.parse.urlencode(obj_data)
        form_data = form_data.encode('utf-8')

        res = urllib.request.urlopen(req, form_data)

        return res.read().decode()
