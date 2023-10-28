from django.urls import path
from django.http import HttpResponse

def dummy_view(request):
    return HttpResponse("This is a dummy view.")

urlpatterns = [
    path('dummy/', dummy_view, name='dummy_view'),
]
