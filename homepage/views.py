#
# This method renders the homepage/index.html template we just created.

from django.shortcuts import render

def index(request):
    return render(request, 'homepage/index.html', {})