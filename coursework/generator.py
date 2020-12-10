from bs4 import BeautifulSoup
import requests
import json
from collections import namedtuple
from pprint import pprint

class Entity():
    def __init__(self,title = "", year = 0, country = "", genre = ""):
        self.id = id
        self.title = title
        self.year = year
        self.country = country
        self.genre = genre

def load_data(min, max):
    list = []
    k = 0
    if max-min > 698 or max > 698:
        return list
    else:
        while min <= max:
            req = requests.get('https://rezka.ag/films/page/' + str(min) + '/')
            bs = BeautifulSoup(req.text, 'html.parser')
            a = bs.select('div.b-content__inline_item-link > a')
            div = bs.select('div.b-content__inline_item-link > div')
            for titles_ in a:
                for title in titles_:
                    entity = Entity()
                    entity.title = title
                    list.append(entity)
            for info in div:
                for j in info:
                    x = j.split(',')
                    if len(x) < 3:
                        list[k].year = 0
                        list[k].country = ""
                        list[k].genre = ""
                        continue
                    for s in x[0].split():
                        if s.isdigit():
                            year = int(s)
                    list[k].year = year
                    list[k].country = x[1]
                    list[k].genre = x[2]
                    k = k + 1
            min = min + 1
        return list

def to_json(list):
    with open("data_file.json", mode="w") as entity_file:
                i = 0
                entity_list = []
                while i < len(list):
                    entity_dict = {
                        "title": list[i].title,
                        "year": list[i].year,
                        "country": list[i].country,
                        "genre": list[i].genre
                    }
                    entity_list.append(entity_dict)
                    i = i + 1
                json.dump(entity_list, entity_file, indent=4, sort_keys=True, ensure_ascii=False)
    entity_file.close()


