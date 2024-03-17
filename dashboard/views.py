from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from item.models import Item  # Import the 'Item' model from the 'item' app

@login_required
def index(request):
    # Retrieve all items created by the currently logged-in user
    items = Item.objects.filter(created_by=request.user)

    # Render the 'index.html' template with the list of items
    return render(request, 'dashboard/index.html', {
        'items': items,
    })
