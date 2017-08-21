from django.db import models

# Create your models here.
import pandas as pd
from pandas import DataFrame
import sqlalchemy as sa
from django.db.models.aggregates import Count
from random import randint
from main.form_choices import COUNTY_CHOICES

class searchCourtdate(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    case_number = models.CharField(max_length=100)
    county = models.CharField(max_length=50, choices=COUNTY_CHOICES)
    email = models.CharField(max_length=100)

def search_db(first_name, last_name, county, case_number):
    if case_number:
        print(case_number)
    elif last_name:
        print(first_name, last_name)

class emailForm(models.Model):

    email = models.CharField(max_length=100)
