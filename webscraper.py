from bs4 import BeautifulSoup
import requests

r = []

def bsoup(keyword, keyword1):
   #Britannica.com
   url="https://www.britannica.com/search?query="+ keyword1
   # Make a GET request to fetch the raw HTML content
   html_content = requests.get(url).text

   # Parse the html content
   soup = BeautifulSoup(html_content, "lxml")
   result = soup.find("div",{"class":"mt-5 font-weight-normal"})
   result1 = result.get_text()
   r.append(result1)


   print("\n")

   
   #Wikipedia.com
   url="https://en.wikipedia.org/wiki/"+keyword

   html_content = requests.get(url).text

   # Parse the html content
   soup = BeautifulSoup(html_content, "lxml")
   results = soup.find("p",{}).findNext("p").get_text()
   r.append(results)

keyword = input("Enter the keyword: ")
keyword1 = keyword.replace(" ","+")
bsoup(keyword,keyword1)

for i in range(len(r)):
  print(i+1,". ",r[i],"\n")
