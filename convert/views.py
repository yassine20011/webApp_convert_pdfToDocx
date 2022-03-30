import contextlib
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from pdf2docx import parse
from convert.models import Snippet
import requests
from django.contrib import messages


#URL = "http://pdftodocx.online/"
URL = "http://127.0.0.1:8000"

def space(string):
    return string.replace(" ", "_")

def check404(request,context, NameOfFile):
    #file_converter = f"/home/ubuntu/yassine/media/{space(NameOfFile)}"
    file_converter = f"media/{space(NameOfFile)}"
    pdf_file = file_converter
    with contextlib.suppress(RuntimeError):
        parse(pdf_file)
    r = requests.get(f'{URL}/{context}')
    print(r.status_code)
    if r.status_code == 200:
        print("File converted successfully:", r.status_code)
        return redirect(context)
    messages.error(request, "Oops! something went wrong")
    print("File converted unsuccessfully:", r.status_code)

    return redirect("/")


def main(request):
    context = {} 
    # sourcery skip: merge-dict-assign, move-assign, remove-unnecessary-else, swap-if-else-branches, use-assigned-variable
    if request.method == 'POST':
        form = Upload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            NameOfFile = request.FILES['file'].name
            context['file_name'] = "media/" + space(NameOfFile.rsplit('.', 1)[0]) + ".docx"
            return check404(request,context['file_name'], NameOfFile)
        else: 
            messages.warning(request, "Wrong file format or size greater than 10MB. Allowed PDF")
            return HttpResponseRedirect('/')
    else:  
        form = Upload()
        return render(request,"index.html",{'form': form})

def Snippet_detail(request, slug):
    snippet = get_object_or_404(Snippet, slug=slug)
    return HttpResponse(f'This should be the detail view for the slug of {slug}')
