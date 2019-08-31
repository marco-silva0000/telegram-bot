import os
import random
import math
from google_images_search import GoogleImagesSearch

from dotenv import load_dotenv
load_dotenv()

gis = GoogleImagesSearch(os.getenv('GCS_DEVELOPER_KEY'), os.getenv('GCS_CX'))

def search(search_params):
    gis.search(search_params=search_params)

    return gis.results()

bear_history = []

def bear_search(query="bear", num=10):
    print(bear_history)
    if num > 10:
        num = 10

    search_params = {
        'q':'bear',
        'num': num,
        'start': math.floor(len(bear_history)/num)
    }
    if len(bear_history) < 20:
        bear_history.extend(search(search_params))
        random.shuffle(bear_history)
    return bear_history.pop()._url





if __name__ == '__main__':
    print(bear_search())

