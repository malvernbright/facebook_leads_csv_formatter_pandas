from django.urls import path
from .views import CSVFilesList, CSVFileDetail

app_name = "sanitize"
urlpatterns = [
    path('', CSVFilesList.as_view(), 'index'),
    path('sanitize/<pk:uid>/', CSVFileDetail.as_view(), 'detail'),
]
