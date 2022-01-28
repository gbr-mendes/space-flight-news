import requests
import json

from core import models
from core.utils import is_valid_uuid


def request_articles():
    try:
        quant_url = 'https://api.spaceflightnewsapi.net/v3/articles/count'
        quant_articles = int(requests.get(quant_url).content)
        len_articles_db = models.Article.objects.all().count()
        if len_articles_db < quant_articles:
            articles_url = f'https://api.spaceflightnewsapi.net/v3/articles?_limit={quant_articles-len_articles_db}'
            articles = json.loads(requests.get(articles_url).content)
            
            for article in articles:
            
                launches = article.pop('launches', None)
                events = article.pop('events', None)
                
                if not is_valid_uuid(str(article['id'])):
                    article.pop('id')
                new_article = models.Article.objects.create(**article)
                
                
                if launches:
                    new_launches_list = []
                    for launch in launches:
                        exists = models.Launch.objects.filter(id=launch['id']).exists()
                        if not exists:
                            launch.pop('id')
                            new_launches_list.append(models.Launch.objects.create(
                                **launch
                            ))
                    new_article.launches.set(new_launches_list)
                    new_article.save()
                
                if events:
                    new_events_list = []
                    for event in events:
                        exists = models.Event.objects.filter(id=event['id']).exists()
                        if not exists:
                            event.pop('id')
                            new_events_list.append(models.Event.objects.create(
                                **launch
                            ))
                    new_article.events.set(new_events_list)
                    new_article.save()
    except Exception as e:
        print(e)
    