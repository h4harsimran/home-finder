import requests
from IPython.display import display
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#%%%
st_var=np.linspace(1,99,100,dtype=int)
arr=np.zeros((19000,4),dtype='str')
df=pd.DataFrame(data=None,columns=['Title','Price','kms','link'])
#%%
for k in st_var:
    start=str(k)
    URL= "https://www.kijiji.ca/b-for-rent/mississauga-peel-region/page-{}/c30349001l1700276?radius=9.0&address=2585+Meadowpine+Boulevard%2C+Mississauga%2C+ON&ll=43.602075,-79.779412".format(start)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    ad_elems = soup.find_all(class_='search-item regular-ad')

    
    
    for i in range(len(ad_elems)):
        ad_price=ad_elems[i].find('div', class_='price')
        #ad_mil=ad_elems[i].find('div', class_='kms')
        ad_mil=ad_elems[i].find('div', class_='distance')
        ad_tit=ad_elems[i].find('a', class_='title')
        ad_link=str('https://www.kijiji.ca'+ ad_elems[i].find('a', href=True)['href'])
        at=str(ad_tit.text)[29:].split('\n')[0]
        am=str(ad_mil.text).split('\n')[4][34:-3]
        ap=str(ad_price.text)[187:].split('\n')[0]
        al=ad_link
        df.loc[df.shape[0]]=[at,ap,am,al]
    
    
df.to_excel('homesnov.xlsx', index=False)
