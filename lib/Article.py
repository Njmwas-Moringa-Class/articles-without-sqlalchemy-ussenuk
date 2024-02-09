import ipdb

class Article:

    all = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title

        
        Article.all.append(self)


    def get_author(self):
        return self._author
    def get_magazine(self):
        return self._magazine
    def get_title(self):
        return self._title
    
 
    author = property(get_author)
    magazine = property(get_magazine)
    title = property(get_title)

if __name__ == "__main__":
    
    first_article = Article(author="Joyce", magazine="AmourAfrique", title="HeartBreaks")
    second_article = Article(author="Kapinga", magazine="RadioOkapi", title="Congo Nouveau")
    third_article = Article(author="SansPapier", magazine="JeuneAfrique", title="Mal du Congo")
    fourth_article = Article(author="Joyce", magazine="AmourAfrique", title="Sexual Parteners")

    # Article.get_article_by()

    ipdb.set_trace()