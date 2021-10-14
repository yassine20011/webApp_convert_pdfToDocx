"""from django.shortcuts import render
import requests

URL = "http://127.0.0.1:8000"

def check404(url):
    r = requests.get(URL+"/"+url)
    if r.status_code == 200:
        return render()
    print(r.status_code)

check404("home")"""
