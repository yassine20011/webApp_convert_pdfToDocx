from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect 
from .forms import *
from pdf2docx import parse
from convert.models import Snippet

def main(request):
    context = {} 
    # sourcery skip: merge-dict-assign, move-assign, remove-unnecessary-else, swap-if-else-branches, use-assigned-variable
    if request.method == 'POST':
        form = Upload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            NameOfFile = request.FILES['file'].name
            file_converter = "/home/ubuntu/yassine/media/" + NameOfFile
            #file_converter = "media/" + NameOfFile
            pdf_file = file_converter
            c_True = True
            while c_True:
                try:
                    parse(pdf_file)
                except RuntimeError:
                    redirect('/')
                context['file_name'] = "/media/" + NameOfFile.rsplit('.', 1)[0] + ".docx"
                c_True = False
                return redirect(context['file_name'])
            else:
                c_True = True
    else:  
        form = Upload()
        return render(request,"index.html",{'form': form})




def Snippet_detail(request, slug):
    snippet = get_object_or_404(Snippet, slug=slug)
    return HttpResponse(f'This should be the detail view for the slug of {slug}')