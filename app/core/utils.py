from core import models
from uuid import UUID


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


def is_valid_uuid(uuid_to_test, version=4):    
    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test
