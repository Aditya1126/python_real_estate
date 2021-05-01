from django.shortcuts import render

# Create your views here.
def listings(request):
    render(request,'listings.html')

def listing(request):
    render(request,'listing.html')

def search(request):
    render(request,'search.html')