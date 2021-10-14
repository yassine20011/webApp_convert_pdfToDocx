from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect 
from .forms import *
from pdf2docx import parse
from convert.models import Snippet
import requests


URL = "https://freeconvert.tk/"

def check404(url, NameOfFile):
    file_converter = "/home/ubuntu/yassine/media/" + NameOfFile
    #file_converter = "media/" + NameOfFile
    pdf_file = file_converter
    try:
        parse(pdf_file)
    except RuntimeError:
        redirect('/')
    r = requests.get(URL+"/"+url)
    print(r.status_code)
    if r.status_code != 200:
        return redirect("/")
    else:
        return redirect(url)


def main(request):
    context = {} 
    # sourcery skip: merge-dict-assign, move-assign, remove-unnecessary-else, swap-if-else-branches, use-assigned-variable
    if request.method == 'POST':
        form = Upload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            NameOfFile = request.FILES['file'].name
            context['file_name'] = "media/" + NameOfFile.rsplit('.', 1)[0] + ".docx"
            return check404(context['file_name'], NameOfFile)
    else:  
        form = Upload()
        return render(request,"index.html",{'form': form})

def Snippet_detail(request, slug):
    snippet = get_object_or_404(Snippet, slug=slug)
    return HttpResponse(f'This should be the detail view for the slug of {slug}')