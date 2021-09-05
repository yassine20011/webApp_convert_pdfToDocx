from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from pdf2docx import parse

# Create your views here.
def base(request):
    return render(request, 'base.html')

def media(request):
    return render(request, 'index.html')



def main(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['POST-file']
        file_system = FileSystemStorage()
        media = r"/media/"
        name = file_system.save(uploaded_file.name,  uploaded_file)
        file_converter = media + name
        pdf_file = file_converter
        parse(pdf_file, start=0, end=None)
        context['file_name'] = media + name.rsplit('.', 1)[0] + ".docx"
    return render(request, 'index.html', context)