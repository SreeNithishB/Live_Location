from django.shortcuts import render
from .forms import LocationModelForm

# Create your views here.

def location_views(request):

    form = LocationModelForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.latitude = form.cleaned_data.get('latitude')
        instance.longitude = form.cleaned_data.get('longitude')
        form.save()

    context = {
        'form': form
    }
    return render(request, 'location/location.html', context)
