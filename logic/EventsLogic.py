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
    
    for event_tr in events_tr:
        event_content={
            'format': event_tr.find('td', {'width': '13%'}).getText(),
            'title': event_tr.find('td', {'class' : 'S14'}).find('a').getText(),
            'location': event_tr.find('td', {'class' : 'S14'}).find('a', {'class':'und'}).getText(),
            'date': event_tr.find('td', {'class' : 'S12'}).getText(),
            'url':'www.mtgtop8.com/'+event_tr.find('td', {'class' : 'S14'}).find('a')['href']
        }
        events.append(event_content)
    
    return {'data': events, 'total': len(events)}

def getLastEventsFormat(format):
    url=''
    events=[]
    if(format=='modern'): url = MAIN_URL + 'format?f=MO'
    if(format=='standard'): url = MAIN_URL + 'format?f=ST'
    if(format=='pioneer'): url = MAIN_URL + 'format?f=PI'
    response = requests.get(url)
    main = BeautifulSoup(response.content,'html.parser')
    events_table= main.find('table', {'class' : 'Stable'})
    events_tr = events_table.findAll('tr')
    
    def checkLocation(tag):
        value = tag.find('td', {'class' : 'S14'}).find('a', {'class':'und'})
        if value : return value.getText()
        else: return 'Unknown' 


    for event_tr in events_tr:
        event_content={
            'title': event_tr.find('td', {'class' : 'S14'}).find('a').getText(),
            'location': checkLocation(event_tr),
            'date': event_tr.find('td', {'class' : 'S12'}).getText(),
            'url':'www.mtgtop8.com/'+event_tr.find('td', {'class' : 'S14'}).find('a')['href']
        }
        events.append(event_content)
   
    return {'data': events, 'total': len(events)}





        
