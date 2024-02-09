import ipdb
from Article import Article
# from Author import Author


class Magazine:

    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.contributors = []
    
        Magazine.all.append(self)

        # self.contributing_authors()

        # for article in Article.all:
        #     if article.magazine == self.name and article.author not in self.contributors:
        #         self.contributors.append(article)

        for article in Article.all:
            if article.magazine == self.name:
                from Author import Author
                #Find the author instance with the name matching the article's author
                author_instance = next((author for author in Author.all if author.name == article.author), None)
                if author_instance and author_instance not in self.contributors:
                    self.contributors.append(author_instance)
            
    
    @classmethod
    def find_by_name(cls, name):
        return next((magazine for magazine in cls.all if magazine.name == name), None)

    @classmethod
    def article_titles(cls,magazine_name):
        return [article.title for article in Article.all if article.magazine == magazine_name]

    def contributing_authors(self):
         return [author for author in self.contributors if len([article for article in author.articles if article.magazine == self.name]) > 2]
    
        
if __name__ == "__main__":

    # Create instances of Author
    from Author import Author
    author1 = Author("Joyce")
    author2 = Author("Kapinga")
    author3 = Author("SansPapier")

    

    #instatiating Article
    article1 = Article(author="Joyce", magazine="AmourAfrique", title="HeartBreaks")
    article2 = Article(author="Joyce", magazine="AmourAfrique", title="LoveHeals")
    article3 = Article(author="Joyce", magazine="AmourAfrique", title="LifeGoesOn")
    article4 = Article(author="Kapinga", magazine="RadioOkapi", title="Congo Nouveau")
    article5 = Article(author="SansPapier", magazine="JeuneAfrique", title="Mal du Congo")
    article5 = Article(author="Kapinga", magazine="JeuneAfrique", title="Joseph Kabila")

    #instatiating Magazine
    magazine1 =  Magazine(name="AmourAfrique", category="lifestyle")
    magazine2 = Magazine(name="RadioOkapi", category="news")
    magazine3 = Magazine(name="JeuneAfrique", category="all")
    magazine4 = Magazine(name="Equipe", category="sport")
    


    # Test the contributors method
    print("Contributors for", magazine1.name, ":", [author.name for author in magazine1.contributors])
    print("Contributors for", magazine2.name, ":", [author.name for author in magazine2.contributors])
    print("Contributors for", magazine3.name, ":", [author.name for author in magazine3.contributors])

    # Test the contributing_authors method
    print("Contributing authors for", magazine1.name, ":", [author.name for author in magazine1.contributing_authors()])
    print("Contributing authors for", magazine2.name, ":", [author.name for author in magazine2.contributing_authors()])
    print("Contributing authors for", magazine3.name, ":", [author.name for author in magazine3.contributing_authors()])



    #Returns an list strings of the titles of all articles written for that magazine
    print(Magazine.article_titles("AmourAfrique"))

    # Test the find_by_name method
    print(Magazine.find_by_name("AmourAfrique"))


    
    ipdb.set_trace()
    
