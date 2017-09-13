## Wikipedia Disambiguation Extractor

I have build a simple script to crawl Wikipedia and extract all the titles of the articles that are in the Disambiguation Category, for any language. The titles are kept in a list and then saved as a pickle file.

Simply run the disambiguation.py script. 
Then paste the URL of the Category:Disambiguation pages ([this is the English version](https://en.wikipedia.org/wiki/Category:Disambiguation_pages)) of the language of your choice. 
Then enter the label of the "next page" button, again in the language of your choice.

Hint -- go to the previous URL and scroll down to the bottom, find the button for "next page" and paste the translation of the label in the above language. I.e: "nächste Seite" in [DE](https://de.wikipedia.org/wiki/Kategorie:Begriffskl%C3%A4rung), "page suivante" in [FR](https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Homonymie), "pagina successiva" in [IT](https://it.wikipedia.org/wiki/Categoria:Pagine_di_disambiguazione), etc. This is done in order to crawl through all the pages containing articles.

If you want the list of the English articles, just press enter, leaving the prompt empty.

The script requires: Python 3, BeautifulSoup 4, urllib and pickle.

There is also a disambiguation_gr.py script which is written for the Greek Wikipedia version.

Afterwards if you want to load the articles as a list, you could use the pickle library or the joblib library.

## What is Disambiguation in Wikipedia

A disambiguation  article in Wikipedia simply put, is when an article is put together to redirect to other articles ([example](https://en.wikipedia.org/wiki/Mercury)). For more on disambiguation in Wikipedia visit the [official article](https://en.wikipedia.org/wiki/Wikipedia:Disambiguation).
