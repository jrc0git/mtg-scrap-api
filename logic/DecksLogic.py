import requests
from bs4 import BeautifulSoup


URL_MODERN = 'https://www.mtgtop8.com/format?f=MO'
URL_STANDARD = 'https://www.mtgtop8.com/format?f=ST'
URL_PIONEER = 'https://www.mtgtop8.com/format?f=PI'

def getDecksByMeta(meta):
    if(meta=='modern'): meta=URL_MODERN
    if(meta=='standard'): meta=URL_STANDARD
    if(meta=='pioneer'): meta=URL_PIONEER
    result=[]
    response = requests.get(meta)
    soup = BeautifulSoup(response.content, 'html.parser')
    meta_table = soup.find('td')
    meta_decks = meta_table.find_all('div', class_='meta_arch')



    def getDecks (tag):
        breakCond=True
        currentTag=tag
        metaResults=[]
        metaDic=[]
        while (breakCond):
            currentTag = currentTag.find_next_sibling()
            if currentTag != None:
                if currentTag['class'][0] == 'hover_tr':
                    metaResults.append([currentTag.find('a'), currentTag.find('img')])
                else: breakCond=False
            else: break
        for deck in metaResults:
            metaDic.append({'name':deck[0].getText(), 'url':'www.mtgtop8.com/'+deck[0]['href'], 'img':'www.mtgtop8.com/'+deck[1]['src']})

        return metaDic


    for i in range(len(meta_decks)):
        result.append(
            {
                'type': meta_decks[i].getText().split(' ')[0],
                'decks': getDecks(meta_decks[i])
            }
        )
    
    return {'data':result}


    

