from django.shortcuts import render
import requests



# Create your views here.
def artii(request):
    font_list = requests.get('http://artii.herokuapp.com/fonts_list').text.split("\n")
    context = {
        'fonts': font_list
    }

    return render(request, 'artii/arti.html', context)

def artii_result(request):

    base_url="http://artii.herokuapp.com/make?text="
    text = request.POST.get('text')

    url = base_url + text

    response = requests.get(url).text

    context = {
        'art_txt': response
    }

    return render(request, 'artii/artii_result.html', context)
