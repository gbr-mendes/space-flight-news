from core import models


class HelperTest:
    @staticmethod
    def create_multiples_articles(quantity):
        articles = []
        for x in range(0, quantity):
            articles.append(
                models.Article.create(
                    title=f'Article Title {x}'
                )
            )