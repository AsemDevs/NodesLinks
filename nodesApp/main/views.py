from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
import logging
import pymysql as sql

# HTML_STRING = """
# <h1>NodesApp</h1>
# """

def home(response):
    return render(response, "main/home.html",{})
