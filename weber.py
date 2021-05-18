from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.flipkart.com/search?q=mi+laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_9_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_9_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=mi+laptop%7CLaptops&requestId=3fb515fa-1f75-4a64-b60e-64677dc136eb&as-searchtext=mi%20laptops'

myClients = uReq(my_url)
page_html = myClients.read()
myClients.close()

page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("div",{"class":"_2kHMtA"})
filename = "weber.csv"
f  = open(filename,"w")
headers = ("title_fresh, clear_price, rating_fresh \n")
f.write(headers)

for mishra_containers in containers: 
    title = mishra_containers.findAll("div", {"class": "_4rR01T"})
    title_fresh = title[0].text
    price= mishra_containers.findAll("div", {"class":"_30jeq3 _1_WHN1"})
    clear_price = price[0].text
    rating = mishra_containers.findAll("div", {"class":"_3LWZlK"})
    rating_fresh = rating[0].text


    print("title: "+title_fresh)
    print("prices: " +clear_price)
    print("rating: " +rating_fresh)

    f.write(title_fresh +"," +clear_price.replace(",","-")+ "," +rating_fresh+"\n")
f.close()    
