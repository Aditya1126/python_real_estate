from django.core import paginator
from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices,bedroom_choices,state_choices
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
    listing=get_object_or_404(Listing,pk=listing_id)
    context={
        'listing':listing
    }
    return render(request,'listing.html',context)

def search(request):

            

    context={
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        
        'values':request.GET
    }

    return render(request,'search.html',context)