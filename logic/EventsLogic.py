import requests
from bs4 import BeautifulSoup

MAIN_URL='https://www.mtgtop8.com/'

def getLastEvents():
    events=[]
    response = requests.get(MAIN_URL)
    main = BeautifulSoup(response.content,'html.parser')
    events_table= main.find('table', attrs={'style':'width:98%;margin-bottom:20px;'})
    events_tr = events_table.findAll('tr')
    print(type(events_table))
   

    def filterTds(tag):
        if(tag.attrs=={'width':'64%', 'class':'S14'}):
            return True
        elif(tag.attrs=={'width':'13%', 'align':'center'}):
            return True
        elif(tag.attrs=={'width':'9%', 'class':'S12', 'align':'right'}):
            return True
        else: return False
    
    for event_tr in events_tr:
        event_content={
            'format': event_tr.find('td', {'width': '13%'}).getText(),
            'title': event_tr.find('td', {'class' : 'S14'}).find('a').getText(),
            'location': event_tr.find('td', {'class' : 'S14'}).find('a', {'class':'und'}).getText(),
            'date': event_tr.find('td', {'class' : 'S12'}).getText(),
            'url':'www.mtgtop8.com/'+event_tr.find('td', {'class' : 'S14'}).find('a')['href']
        }
        events.append(event_content)
    
    return events
        
