import os
import time
import requests
import sys

def html_save():
    for year in range(2015,2024):
        for month in range(1,13):
            if(month<10):
                url='http://en.tutiempo.net/climate/0{}-{}/ws-171300.html'.format(month
                                                                          ,year)
            else:
                url='http://en.tutiempo.net/climate/{}-{}/ws-171300.html'.format(month
                                                                          ,year)
            html=requests.get(url)
            html_utf=html.text.encode('utf=8')
            
            if not os.path.exists("Data/Html_Data/{}".format(year)):
                os.makedirs("Data/Html_Data/{}".format(year))
            with open("Data/Html_Data/{}/{}.html".format(year,month),"wb") as output:
                output.write(html_utf)
            
        sys.stdout.flush()
        
if __name__=="__main__":
    start_time=time.time()
    html_save()
    stop_time=time.time()
    print("Time taken {}".format(stop_time-start_time))