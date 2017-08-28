## Wikipedia Disambiguation Extractor

I have build a simple script to crawl Wikipedia and extract all the titles of the articles that are in the Disambiguation Category, for any language. The titles are kept in a list and then saved as a pickle file.

Simply run the disambiguation.py script. 
Then paste the URL of the Category:Disambiguation pages ([this is the English version](https://en.wikipedia.org/wiki/Category:Disambiguation_pages)) of the language of your choice. 
Then enter the label of the "next page" button, again in the language of your choice(Hint -- go to the previous URL and scroll down to the bottom, find the button for "next page" and paste the translation of the label in the above language. I.e: "nächste Seite" in DE, "page suivante" in FR, "pagina successiva" in IT, etc.) 

If you want the list of the English articles, leave the prompt empty.

The script requires: Python 3, BeautifulSoup 4, urllib and pickle.

There is also a disambiguation_gr.py script which is written for the Greek Wikipedia version.

Afterwards if you want to load the articles as a list, you could use the pickle library or the joblib library.

## What is Disambiguation in Wikipedia

Disambiguation in Wikipedia simply put, is when an article redirects to other articles. This disambiguation article's only purpose is to redirect you.  For more on disambiguation in Wikipedia visit the [Wiki article](https://en.wikipedia.org/wiki/Wikipedia:Disambiguation).
