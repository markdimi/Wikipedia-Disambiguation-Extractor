from bs4 import BeautifulSoup
import pickle
from datetime import datetime
try:
    import urllib
except AttributeError:
    import urllib.requests

startTime = datetime.now()

# user input
print()
print("Please enter the Wikipedia URL containing the disambiguation articles")
print("Leave empty if the target language of the Wikipedia articles is English.")
user_url = input("> ")

if user_url:
    print()
    print("Please enter the 'next page' label in the target language of the articles")
    print("Hint -- go to the bottom of the given URL and enter the label for the 'next page' button")
    next_page_label = input("> ")
else:
    user_url = "https://en.wikipedia.org/wiki/Category:Disambiguation_pages"
    next_page_label = "next page"

# initialize

starting_url = urllib.request.urlopen(user_url)

soup = BeautifulSoup(starting_url, "lxml")

## disambiguation articles
dis_art = [] 

counter = 1

# crawling loop

while counter != 0:
    
    print("Page:", counter)
    
    # Let's get the disambiguation articles from the current page
    
    ## at the bottom of the page there is a div with id = mw-pages which contains divs with class = mw-category-group.
    ## Each mw-category-group div contain an alphabetical category of disambiguation articles.
    
    divs = soup.find_all("div", attrs={'class':"mw-category-group"})
    
    ## The article titles are <li> items.

    for div in divs:
        lis = div.find_all("li")
        for li in lis:
            dis_art.append(li.text)

    # getting next pages link
    
    links = soup.find_all('a' , text = next_page_label) 
    
    if links:
        
        # constructing the link for the next page
        
        next_link = user_url.split("org")[0] + "org" + links[0]['href']
        
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
