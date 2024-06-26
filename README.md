# CrawPilot

# API Documentation:
### Crawl API:
API endpoint => [{{baseUrl}}/crawl]()

* Crawl API takes list of urls in request body, upon hitting the api it returns success message saying crawling has started.
* API also returns an id, which is necessary to make other calls as well.
**Request**
```
{
    "urls": [
        "https://en.wikipedia.org/wiki/Main_Page",
        "https://www.nytimes.com/",
        "https://edition.cnn.com/",
        "https://www.bbc.com/news",
        "https://www.theguardian.com/international"
    ]
}
```

**Response**
```
{
    "message": "Scarp for the urls has been started..!!",
    "id": "add6a779dc664c898b5b6ce9a0347e56"
}
```

### Result API:
API endpoint => [{{baseUrl}}/result]()

* As soon as crawl API is hit, web scrapping starts in the background.
* We can get to know the status of scrapping using this API.
**Request**
```
{
    "id":"02ce9bfec40949d5a4974f0d3691cf5c"
}
```

**Response**

If crawling is still in progress we get this response

````
{
    "result": "Crawling is still in progress!!"
}
````
else

```
{
    "result": [
        {
            "url": "https://en.wikipedia.org/wiki/Main_Page",
            "header": "Main Page",
            "link_list": [
                "https://donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&utm_medium=sidebar&utm_campaign=C13_en.wikipedia.org&uselang=en",
                "/w/index.php?title=Special:UrlShortener&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMain_Page",
                "/w/index.php?title=Special:QrCode&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMain_Page",
                "https://www.wikidata.org/wiki/Special:EntityPage/Q5296",
                "https://commons.wikimedia.org/wiki/Main_Page",
                "https://foundation.wikimedia.org/wiki/Home",
                "https://www.mediawiki.org/wiki/MediaWiki",
                "https://meta.wikimedia.org/wiki/Main_Page",
                "https://outreach.wikimedia.org/wiki/Main_Page",
                "https://wikisource.org/wiki/Main_Page",
                "https://species.wikimedia.org/wiki/Main_Page",
                "https://en.wikibooks.org/wiki/Main_Page",
                "https://www.wikidata.org/wiki/Wikidata:Main_Page",
                "https://www.wikifunctions.org/wiki/Wikifunctions:Main_Page",
                "https://wikimania.wikimedia.org/wiki/Wikimania",
                "https://en.wikinews.org/wiki/Main_Page",
                "https://en.wikiquote.org/wiki/Main_Page",
                "https://en.wikisource.org/wiki/Main_Page",
                "https://en.wikiversity.org/wiki/Wikiversity:Main_Page",
                "https://en.wikivoyage.org/wiki/Main_Page",
                "https://en.wiktionary.org/wiki/Wiktionary:Main_Page",
                "https://lists.wikimedia.org/postorius/lists/daily-article-l.lists.wikimedia.org/",
                "https://lists.wikimedia.org/postorius/lists/daily-article-l.lists.wikimedia.org/",
                "https://wikimediafoundation.org/our-work/wikimedia-projects/",
                "https://en.wiktionary.org/wiki/",
                "https://en.wiktionary.org/wiki/",
                "https://meta.wikimedia.org/wiki/List_of_Wikipedias",
                "https://zh.wikipedia.org/wiki/",
                "https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Privacy_policy",
                "https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Universal_Code_of_Conduct",
                "https://developer.wikimedia.org",
                "https://stats.wikimedia.org/#/en.wikipedia.org",
                "https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Cookie_statement",
                "https://wikimediafoundation.org/",
                "https://www.mediawiki.org/"
            ],
            "summary": "Mars is the fourth planet from the Sun. It was formed approximately 4.5 billion years ago. It has the highest mountain in the solar system, Olympus Mons, and the largest canyon, Valles Marineris."
        }
    ]
}
```

### Report API:
API endpoint => [{{baseUrl}}/report]()

* Report API give insights about the APIs that are crawled till then.

**Response**
```
{
    "result": [
        "https://en.wikipedia.org/wiki/Main_Page",
        "https://www.nytimes.com/",
        "https://edition.cnn.com/",
        "https://www.bbc.com/news",
        "https://www.theguardian.com/international",
        "https://www.reuters.com/",
        "https://www.wsj.com/",
        "https://www.forbes.com/",
        "https://www.nationalgeographic.com/"
    ]
}
```

### Cosine API:
API endpoint => [{{baseUrl}}/cosine]()

* Report API returns cosine matrix.

**Request**
```
{
    "id":"02ce9bfec40949d5a4974f0d3691cf5c"
}
```

**Response**
```
{
    "result": "[[1.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.        ]\n [0.         1.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.07460473\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.        ]\n [0.         0.         1.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.        ]\n [0.         0.         0.         1.         0.         0.\n  0.         0.         0.         0.02981889 0.         0.\n  0.         0.01868194 0.         0.         0.         0.\n  0.         0.         0.         0.         0.03462805 0.\n  0.07206956 0.03075717 0.02763565]\n [0.         0.         0.         0.         1.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.05891554\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.        ]\n [0.         0.         0.         0.         0.         1.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.        ]\n [0.         0.         0.         0.         0.         0.\n  1.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.        ]\n [0.         0.         0.         0.         0.         0.\n  0.         1.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.03937671 0.         0.         0.         0.\n  0.         0.         0.        ]\n [0.         0.         0.         0.         0.         0.\n  0.         0.         1.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.        ]\n [0.         0.         0.         0.02981889 0.         0.\n  0.         0.         0.         1.         0.         0.03343569\n  0.         0.02467302 0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.03948741 0.         0.03649807]\n [0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         1.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.03764608 0.         0.08678747 0.         0.\n  0.         0.         0.        ]\n [0.         0.07460473 0.         0.         0.         0.\n  0.         0.         0.         0.03343569 0.         1.\n  0.         0.         0.         0.         0.         0.\n  0.         0.03103731 0.         0.         0.         0.\n  0.         0.         0.026471  ]\n [0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  1.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.        ]\n [0.         0.         0.         0.01868194 0.         0.\n  0.         0.         0.         0.02467302 0.         0.\n  0.         1.         0.         0.         0.         0.02789988\n  0.         0.         0.         0.02565015 0.         0.\n  0.0247394  0.         0.        ]\n [0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.        ]\n [0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.         1.         0.         0.\n  0.10088906 0.04960597 0.         0.         0.         0.\n  0.         0.         0.        ]\n [0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         1.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.05047484]\n [0.         0.         0.         0.         0.05891554 0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.02789988 0.         0.         0.         1.\n  0.         0.         0.         0.03954769 0.         0.\n  0.0537985  0.         0.        ]\n [0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.10088906 0.         0.\n  1.         0.         0.         0.         0.         0.\n  0.         0.         0.        ]\n [0.         0.         0.         0.         0.         0.\n  0.         0.03937671 0.         0.         0.03764608 0.03103731\n  0.         0.         0.         0.04960597 0.         0.\n  0.         1.         0.         0.         0.         0.\n  0.         0.         0.03388002]\n [0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         1.         0.         0.         0.01646578\n  0.         0.         0.        ]\n [0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.08678747 0.\n  0.         0.02565015 0.         0.         0.         0.03954769\n  0.         0.         0.         1.         0.         0.\n  0.         0.03607414 0.        ]\n [0.         0.         0.         0.03462805 0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         1.         0.\n  0.         0.         0.07983006]\n [0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.01646578 0.         0.         1.\n  0.         0.         0.        ]\n [0.         0.         0.         0.07206956 0.         0.\n  0.         0.         0.         0.03948741 0.         0.\n  0.         0.0247394  0.         0.         0.         0.0537985\n  0.         0.         0.         0.         0.         0.\n  1.         0.         0.        ]\n [0.         0.         0.         0.03075717 0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.         0.         0.\n  0.         0.         0.         0.03607414 0.         0.\n  0.         1.         0.        ]\n [0.         0.         0.         0.02763565 0.         0.\n  0.         0.         0.         0.03649807 0.         0.026471\n  0.         0.         0.         0.         0.05047484 0.\n  0.         0.03388002 0.         0.         0.07983006 0.\n  0.         0.         1.        ]]"
}
```

