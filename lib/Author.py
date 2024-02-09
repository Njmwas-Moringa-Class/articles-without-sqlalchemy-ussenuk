import ipdb

from Magazine import Magazine
from Article import Article

class Author:
    all = []  # Class variable to keep track of all instances

    def __init__(self, name):
        self._name = name
        self.articles = []
        self.magazines = []

        Author.all.append(self)  # Append the new instance to the 'all' class variable

        for article in Article.all:
            if article.author == self.name:
                self.articles.append(article)
        for magazine in Magazine.all:
            for article in self.articles:
                if magazine.name == article.magazine and magazine not in self.magazines:
                    self.magazines.append(magazine)

    def get_name(self):
        return self._name
    
    def articles(self):
        return self.articles

    def magazines(self):
        return self.magazines
    
    def add_article(self,magazine, title):
        new_article = Article(self._name, magazine.name, title)
        self.articles.append(new_article)

        if magazine not in self.magazines:
            self.magazines.append(magazine)

    def topic_areas(self):
        return list(set([magazine.category for magazine in self.magazines]))
    
    name = property(get_name)


if __name__ == "__main__":

    #instatiating Article

    first_article = Article(author="Joyce", magazine="AmourAfrique", title="HeartBreaks")
    second_article = Article(author="Kapinga", magazine="RadioOkapi", title="Congo Nouveau")
    third_article = Article(author="SansPapier", magazine="JeuneAfrique", title="Mal du Congo")
    fourth_article = Article(author="Kapinga", magazine="AmourAfrique", title="Sexual Parteners")

    #instatiating Magazine

    first_magazine = Magazine(name="AmourAfrique", category="lifestyle")
    second_magazine = Magazine(name="RadioOkapi", category="news")
    third_magazine = Magazine(name="JeuneAfrique", category="all")
    fourth_magazine = Magazine(name="Equipe", category="sport")
    
    first_author = Author("Kapinga")

    # Returns an list of Articles instances the author has written
    first_author.articles # should return 2 Articles instances of Kapinga

    # Returns a unique list of Magazine instances for which the author has contributed to
    first_author.magazines # should return 2 Magazine instances for Kapinga

    # Given a  magazine(as Magazine instance) and a title (as a string), creates a new Article instance and associates it with that author and that magazine
    author = Author("Joyce")
    magazine = Magazine(name="Euronews", category="lifestyle")
        
    author.add_article(magazine, "Le regles")   
        # Check if the new article was added
    print("Here is the new added article instance to the author\n")
    print(author.articles)   # This should print a list of instances containing the new article
    print("Here all articles within the Article class including the lastly added\n")
    for articles in Article.all: print(articles.title)   
        # Check if the magazine was added to the author's magazines
    print("Here is the new added magazine instance\n")
    print(author.magazines)  # This should print a list of instances containing the magazine
    print("Here all magazine within the Magazine class inclding the lastly added\n")
    for magazine in Magazine.all: print(magazine.name)

    # Returns a unique list of strings with the categories of the magazines the author has contributed to
    print("Here is the unique list of magazine categories the author has contributed to\n")
    print(first_author.topic_areas())
    


    
    ipdb.set_trace()
