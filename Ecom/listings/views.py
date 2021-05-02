from django.core import paginator
from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def listings(request):

    listings=Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator=Paginator(listings,3)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
    context={
        'listings':listings
    }

    return render(request,'listings.html',context)

def listing(request,listing_id):
    return render(request,'listing.html')

def search(request):
    return render(request,'search.html')