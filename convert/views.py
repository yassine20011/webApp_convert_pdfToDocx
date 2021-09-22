from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
from pdf2docx import parse
def main(request):
    context = {} 
    # sourcery skip: merge-dict-assign, move-assign, remove-unnecessary-else, swap-if-else-branches, use-assigned-variable
    if request.method == 'POST':  
        form = Upload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            NameOfFile = request.FILES['file'].name
            file_converter = "media/" + NameOfFile
            pdf_file = file_converter
            parse(pdf_file, start=0, end=None)
            context['file_name'] = "/media/" + NameOfFile.rsplit('.', 1)[0] + ".docx"
            return redirect(context['file_name'])
        else:
            return HttpResponse("File not supported!")
    else:  
        form = Upload()
        return render(request,"index.html",{'form': form})

