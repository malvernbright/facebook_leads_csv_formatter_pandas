from django.shortcuts import render
from django.views import generic
from .models import FbFile


class CSVFilesList(generic.ListView):
    model = FbFile
    template_name = "sanitize/index.html"
    context_object_name = "files"


class CSVFileDetail(generic.DetailView):
    model = FbFile
    template_name = "sanitize/detail.html"
    context_object_name = "file"
