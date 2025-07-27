from requests import get
from bs4 import BeautifulSoup
from pandas import DataFrame
from math import ceil

def Serach_on (name):
    url='https://wuzzuf.net/search/jobs/?a=navbg%7Cspbg&q='+name
    return url

def number_of_Page(url):
    response=get(url)
    soup=BeautifulSoup(response.content,'lxml')

    tag=soup.find('li',class_='css-8neukt').text.split()
    num=ceil(int(tag[-1])/int(tag[3]))
    return num

def soup(num,url):
    titles_lst=[]
    refrences_lst=[]
    occupation_list=[]
    companies_lst=[]
    descriptions_lst=[]
    area_lst=[]

    for i in range(num):
        url1=f'{url}&start={i}'
        response=get(url1)
        soup=BeautifulSoup(response.content,'lxml')
        
        titles=soup.find_all('h2',class_='css-m604qf')
        for title in titles:
            titles_lst.append(title.text)
        
        for title in titles:
            refrences_lst.append(title.a['href'])
        
        occupations=soup.find_all('div',class_='css-1lh32fc')
        for o in occupations:
            occupation_list.append(o.text)
        
        descriptions=soup.find_all('div',class_='css-y4udm8')
        for d in descriptions:
            descriptions_lst.append(d.text)
        
        companies=soup.find_all('a',class_='css-17s97q8')
        for c in companies:
            companies_lst.append(c.text)
        
        areas=soup.find_all('span', class_='css-5wys0k')
        for a in areas:
            area_lst.append(a.text)

    dic={
        'Titles' : titles_lst,
        'Comapany' : companies_lst,
        'References':refrences_lst,
        'Descriptions' : descriptions_lst,
        'Occpation' :occupation_list,
        'Area' : area_lst
    }
    df=DataFrame(dic)
    return df

def Wzzuff(name):
    url=Serach_on()
    nPage=number_of_Page(url)
    df=soup(nPage,url)
    df.to_csv(f"{name.replace('%20','-')}.csv")

if __name__=='__main__':
    name=input("Search on Wzzuff : ").replace(' ','%20')
    Wzzuff(name)