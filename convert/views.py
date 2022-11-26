import contextlib
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *
from pdf2docx import parse
import os, glob
from django.contrib import messages





def space(string):
    return string.replace(" ", "_")

def check404(request, path, FileName):
    #file_converter = f"/app/media/{space(FileName)}"
    file_converter = f"media/{space(FileName)}"
    
    pdf_file = file_converter
    with contextlib.suppress(RuntimeError):
        parse(pdf_file)

    os.chdir(r"C:\Users\AMJAD\Desktop\webApp_convert_pdfToDocx\media")
    #os.chdir(r"/app/media")

    for file in glob.glob("*.docx"):
        if file ==  space(FileName.rsplit('.', 1)[0]) + ".docx":
            return redirect(path)
    messages.error(request, "Oops! something went wrong")
    return HttpResponseRedirect('/')




def main(request):
    
    if request.method == 'POST':
        form = Upload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            FileName = request.FILES['file'].name
            path = "media/" + space(FileName.rsplit('.', 1)[0]) + ".docx"
            return check404(request, path, FileName)
        else: 
                messages.warning(request, "Wrong file format or size greater than 10MB. Allowed PDF")
                return HttpResponseRedirect('/')


    else:  
        form = Upload()
        return render(request, "index.html", {'form': form})


