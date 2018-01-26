import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "tango_with_django_project.settings")

import django
django.setup()
from rango.models import Category, Page


def populate():

    ##list of dictionaries of pages to be added
    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "https://docs.python.org/2/tutorial/"},
        {"title": "How To Think LIke A Computer Scientist",
         "url": "http://www.greeteapress.com/thinkpython/"},
        {"title":"Learn Python in 10 Minutes",
         "url":"http://www.korokithakis.net/tutorials/python/"},
        ]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com"},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/"},
        ]

    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/"},
        {"title": "Flask",
         "url": "http://flask.pocoo.org"},
        ]

    cats = {"Python": {"pages": python_pages},
            "Django": {"pages": django_pages},
            "Other_frameworks": {"pages": other_pages},
            }

    
    







            
