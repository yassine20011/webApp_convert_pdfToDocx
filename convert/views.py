from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect 
from .forms import *
from pdf2docx import parse
from convert.models import Snippet
import requests
from django.contrib import messages


URL = "http://pdftodocx.online/"
#URL = "http://127.0.0.1:8000"

def check404(request,url, NameOfFile):
    file_converter = "/home/ubuntu/yassine/media/" + NameOfFile
    #file_converter = "media/" + NameOfFile
    pdf_file = file_converter
    try:
        parse(pdf_file)
    except RuntimeError:
        pass
    r = requests.get(URL+"/"+url)
    print(r.status_code)
    if r.status_code != 200:
        messages.error(request, "Oops! something went wrong")
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
            return check404(request,context['file_name'], NameOfFile)
        else:
            messages.warning(request, "Wrong file format. Allowed PDF")
            return HttpResponseRedirect('/')
    else:  
        form = Upload()
        return render(request,"index.html",{'form': form})

def Snippet_detail(request, slug):
    snippet = get_object_or_404(Snippet, slug=slug)
    return HttpResponse(f'This should be the detail view for the slug of {slug}')