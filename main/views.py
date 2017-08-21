
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from django.template import loader, Context
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
import pandas as pd
import csv
import sqlalchemy as sa
from django.contrib.auth.decorators import login_required
from main.forms import *
from django.core.validators import validate_email
from django.contrib import messages
from main.models import *
# Create your views here.
engine = sa.create_engine('mysql://root:sq8337269!@104.196.179.105:3306/voyansqldb?')

def search(request):
    form = mainForm()
    if request.method == 'POST':
        print("Hello")
        form = mainForm(request.POST)

        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            case_number = form.cleaned_data['case_number']
            county = form.cleaned_data['county']
            email = form.cleaned_data['email']
            if len(email) > 0:
                try:
                    validate_email(email)
                    validate_case_number(case_number)
                    # search_db(first_name, last_name, county, case_number)
                except Exception as e:
                    messages.error(request, e)
            if county == 'hill':
                if len(first_name) == 0 and len(last_name) >= 0 and len(case_number) == 0:
                    messages.error(request, """You must put in either both
                                                First and Last Name, or Case Number""")


                elif len(first_name) > 0 and len(last_name) == 0:
                    messages.error(request, """You must put in either both
                                                First and Last Name, or Case Number""")

                elif len(first_name) == 0 and len(last_name) == 0 and len(case_number) == 0:
                    messages.error(request, """You must put in either both
                                                First and Last Name, or Case Number""")
                elif len(first_name) == 0 and len(last_name) > 0 and len(case_number) > 0:
                    messages.error(request, """You must put in either both
                                                First and Last Name, or Case Number""")

                elif len(case_number) > 0:
                    sql_text = """SELECT DISTINCT *
                                        FROM hillsborough
                                        WHERE Case_Number
                                        regexp '%s'
                                        ;""" % case_number
                    df = pd.read_sql_query(sql_text, engine)
                    df_len = len(df)

                    empty_dict = {
                                    'Location':[],
                                    'Date':[],
                                    'Time':[],
                                    'Hearing Type':[],
                                    }
                    for x in range(0, df_len):
                        location = df.iloc[x]['Hearing Location']
                        empty_dict['Location'].append(location)
                        date_time = df.iloc[x]['Hearing Date/Time']
                        date = date_time[0:10]
                        empty_dict['Date'].append(date)
                        time = date_time[11:16]
                        empty_dict['Time'].append(time)
                        hearing_type = df.iloc[x]['Hearing Type']
                        empty_dict['Hearing Type'].append(hearing_type)

                    return render(request, 'main/results.html', {
                                                                'df_len':df_len,
                                                                'empty_dict':empty_dict,

                                                                })
                elif len(first_name) > 0 and len(last_name) > 0:
                    sql_text = """SELECT DISTINCT Hearing_Location,
                                        Hearing_DateTime,
                                        Hearing_Type
                                        FROM hillsborough
                                        WHERE first_name
                                        REGEXP '%s'
                                        AND last_name
                                        REGEXP '%s'

                                        ;""" % (first_name, last_name)
                    df = pd.read_sql_query(sql_text, engine)
                    df_len = len(df)
                    empty_dict = {
                                    'Location':[],
                                    'Date':[],
                                    'Time':[],
                                    'Hearing Type':[],
                                    }
                    for x in range(0, df_len):
                        location = df.iloc[x]['Hearing_Location']
                        empty_dict['Location'].append(location)
                        date_time = df.iloc[x]['Hearing_DateTime']
                        date = date_time[0:10]
                        empty_dict['Date'].append(date)
                        time = date_time[11:16]
                        empty_dict['Time'].append(time)
                        hearing_type = df.iloc[x]['Hearing_Type']
                        empty_dict['Hearing Type'].append(hearing_type)

                    return render(request, 'main/results.html', {
                                                                'df_len':df_len,
                                                                'empty_dict':empty_dict,

                                                                })

            elif county == 'pine':
                if len(first_name) == 0 and len(last_name) > 0:
                    messages.error(request, """You must put in either both
                                                First and Last Name, or Case Number""")

                elif len(first_name) > 0 and len(last_name) == 0:
                    messages.error(request, """You must put in either both
                                                First and Last Name, or Case Number""")

                elif len(first_name) == 0 and len(last_name) == 0:
                    messages.error(request, """You must put in either both
                                                First and Last Name, or Case Number""")
                elif len(case_number) > 0:
                    sql_text = """SELECT DISTINCT *
                                        FROM pinellas
                                        WHERE "Case Number"
                                        REGEXP '%s'


                                        ;""" % case_number
                    df = pd.read_sql_query(sql_text, engine)
                    df_len = len(df)

                    empty_dict = {
                                    'Location':[],
                                    'Date':[],
                                    'Time':[],
                                    'Hearing Type':[],
                                    }
                    for x in range(0, df_len):
                        location = df.iloc[x]['Hearing Location']
                        empty_dict['Location'].append(location)
                        date_time = df.iloc[x]['Hearing Date/Time']
                        date = date_time[0:10]
                        empty_dict['Date'].append(date)
                        time = date_time[11:16]
                        empty_dict['Time'].append(time)
                        hearing_type = df.iloc[x]['Hearing Type']
                        empty_dict['Hearing Type'].append(hearing_type)

                    return render(request, 'main/results.html', {
                                                                'df_len':df_len,
                                                                'empty_dict':empty_dict,

                                                                })

                elif len(first_name) > 0 and len(last_name) > 0:
                    sql_text = """SELECT DISTINCT *
                                        FROM pinellas
                                        WHERE first_name
                                        REGEXP '%s'
                                        AND last_name
                                        REGEXP '%s'

                                        ;""" % (first_name, last_name)
                    df = pd.read_sql_query(sql_text, engine)
                    df_len = len(df)

                    empty_dict = {
                                    'Location':[],
                                    'Date':[],
                                    'Time':[],
                                    'Hearing Type':[],
                                    }
                    for x in range(0, df_len):
                        location = df.iloc[x]['Hearing Location']
                        empty_dict['Location'].append(location)
                        date_time = df.iloc[x]['Hearing Date/Time']
                        date = date_time[0:10]
                        empty_dict['Date'].append(date)
                        time = date_time[11:16]
                        empty_dict['Time'].append(time)
                        hearing_type = df.iloc[x]['Hearing Type']
                        empty_dict['Hearing Type'].append(hearing_type)

                    return render(request, 'main/results.html', {
                                                                'df_len':df_len,
                                                                'empty_dict':empty_dict,
                                                                'form':form
                                                                })
    return render(request, 'main/search.html',  {'form': form})

def results(request):
    form = mainForm()
    if request.method == 'POST':
        form = mainForm(request.POST)
        print("Hello")
        if form.is_valid():
            email = form.cleaned_data['email']
            print(email)
            form.save()
    return render(request, 'main/results.html', {'form':form})
