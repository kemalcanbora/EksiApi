from newspaper import Article


def extractor(url):
    article = Article(url, language='tr')
    article.download()
    article.parse()
    return article.text