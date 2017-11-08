from bs4 import BeautifulSoup
import pickle
from datetime import datetime
try:
    import urllib
except AttributeError:
    import urllib.requests

startTime = datetime.now()

# for other languages change starting_url

starting_url = urllib.request.urlopen('https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CF%84%CE%B7%CE%B3%CE%BF%CF%81%CE%AF%CE%B1:%CE%91%CF%80%CE%BF%CF%83%CE%B1%CF%86%CE%AE%CE%BD%CE%B9%CF%83%CE%B7')

# initialize

soup = BeautifulSoup(starting_url, "lxml")

## disambiguation articles
dis_art = [] 

counter = 1

# crawling loop

while counter != 0:
    
    print("Page", counter)
    
    #get the disambiguation articles from the current page
    
    divs = soup.find_all("div", attrs={'class':"mw-category-group"})

    for div in divs:
        lis = div.find_all("li")
        for li in lis:
            dis_art.append(li.text)

    # getting next pages link
    
    links = soup.find_all('a' , text = 'επόμενη σελίδα') # for other languages change the "next page" title/text
    
    if links:
        
        next_link = 'https://el.wikipedia.org' + links[0]['href']
        
        next_url = urllib.request.urlopen(next_link)
        soup = BeautifulSoup(next_url, "lxml")
        
        counter += 1
        
    else:
        # halting the process if there are no further pages of articles
        break

# print info and save to file

print()
print("Process terminated after",datetime.now() - startTime)
print("Finished gathering", len(dis_art), "articles, from", counter, "pages")
print("Last url visited was:", next_link)
print()


print("Please enter a filename for the list")

filename = input("> ")
filename = filename + '.txt'
pickle.dump(dis_art, open(filename, 'wb'))

print("Articles saved as:", filename)
print()
print("If you want to load the articles as a list you could use the pickle library or the joblib library")
print("i.e:")
print(" > with open('"+filename+"', 'rb') as pickle_file:")
print(" >     articles = pickle.load(pickle_file)")
print(" or")
print(" > articles = joblib.load('" + filename + "')")
