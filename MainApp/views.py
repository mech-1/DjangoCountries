from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'pagename': 'Homepage'}
    return render(request, 'pages/index.html', context)