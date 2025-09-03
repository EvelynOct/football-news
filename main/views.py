from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406365282',
        'name': 'Evelyne Octaviana Benedicta Aritonang',
        'class': 'KKI'
    }

    return render(request, "main.html", context)
