from django.contrib.sites.models import Site
from django.http import HttpResponse 
from django.shortcuts import get_object_or_404, render, redirect 
from .forms import *
from pdf2docx import parse
from convert.models import Snippet
from django.contrib.sites.requests import RequestSite



def main(request):
    context = {} 
    # sourcery skip: merge-dict-assign, move-assign, remove-unnecessary-else, swap-if-else-branches, use-assigned-variable
    if request.method == 'POST':  
        form = Upload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            NameOfFile = request.FILES['file'].name
            file_converter = "/home/ubuntu/yassine/media/" + NameOfFile
            pdf_file = file_converter
            parse(pdf_file, start=0, end=None)
            context['file_name'] = "/media/" + NameOfFile.rsplit('.', 1)[0] + ".docx"
            return redirect(context['file_name'])
        else:
            request.session['File-supported'] = "File not supported!"
            return render(request, 'index.html')
    else:  
        form = Upload()
        return render(request,"index.html",{'form': form})


def Snippet_detail(request, slug):
    snippet = get_object_or_404(Snippet, slug=slug)
    return HttpResponse(f'This should be the detail view for the slug of {slug}')