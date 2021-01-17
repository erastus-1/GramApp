from django.http  import HttpResponse,Http404
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def search(request):
    profiles = User.objects.all()

    if 'username' in request.GET and request.GET['username']:
        search_term = request.GET.get('username')
        results = User.objects.filter(username__icontains=search_term)
        print(searchs)

        return render(request,'search.html',locals())

    return redirect(home)
