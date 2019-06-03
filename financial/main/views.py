from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd


def main(request):
    url = 'https://jdata.yuanta.com.tw/z/zc/zcq/zcq_2885.djhtm'
    df = pd.read_html(url)
    return HttpResponse(df)
# Create your views here.
