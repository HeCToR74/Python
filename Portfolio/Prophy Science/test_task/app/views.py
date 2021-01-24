import requests
import pandas as pd
from sqlalchemy import create_engine
from django.shortcuts import render
from .forms import TextForm
from .models import Text, Keyphrase
from rake_nltk import Rake

API_ENDPOINT = "https://www.wikidata.org/w/api.php"

# SQLAlchemy connectable
cnx = create_engine('sqlite:///prophy_science.sqlite3').connect()
df = pd.read_sql_table('app_keyphrase', cnx)
df = df.groupby('phrase')['id'].nunique()
df = pd.DataFrame({"phrase": df.index, 'count': df.to_list()})
df = df.sort_values(by='count')

def index(request):
    textform = TextForm()
    if request.method == 'POST':
        text = request.POST.get("text")
        text_object = Text.objects.create(text=text)
        r = Rake()
        r.extract_keywords_from_text(text)
        list_phrases = r.get_ranked_phrases()
        for phrase in list_phrases:
            params = {
                'action': 'wbsearchentities',
                'format': 'json',
                'language': 'en',
                'search': phrase
            }
            r = requests.get(API_ENDPOINT, params=params)
            result = r.json()['search']
            if result == []:
                exist = False
                disambiguation = False
            else:
                exist = True
                if len(result) > 1:
                    disambiguation = True
                else:
                    disambiguation = False
            text_object.keyphrase_set.create(phrase=phrase, exist=exist, disambiguation=disambiguation)

        return render(request, "index.html", {"form": textform})

    return render(request, "index.html", {"form": textform, "top_keyphrase": df['phrase'].to_list()[::-1][:10]})
