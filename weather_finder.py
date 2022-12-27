from requests_html import HTMLSession
import pandas as pd
class Weather_Info:
    def __init__(self,city):
        self.city = city
    def getWeather(self):
        try:
            s = HTMLSession()
            if s:
                url = f'https://www.google.com/search?q={self.city}+weather'
                r = s.get(url)
                title = r.html.find('title', first = True).text
                place = r.html.find('#wob_loc',first = True).text
                temp = r.html.find('span#wob_tm', first = True).text
                prec = r.html.find('span#wob_pp', first = True).text
                humidity = r.html.find('span#wob_hm', first = True).text
                wind_speed = r.html.find('span#wob_ws', first = True).text
                dts = r.html.find('#wob_dts',first = True).text
                data = {'title' : title,
                        'place' : place,
                         'temp' : temp,
                        'precipiation' : prec,
                       'humidity' : humidity,
                       'wind_speed' : wind_speed,
                       'time' : dts}
                sr = pd.Series(data)
                return sr
        except Exception as e:
            return(str(e))
        
place = str(input('enter::'))
obj = Weather_Info(place)
series = obj.getWeather()
df = pd.DataFrame(data=series)
print(series)
