from django.shortcuts import render,HttpResponse


def home(request):
    query = request.GET.get('search')
    context = {'query': query}
    a = [request, 'abc.html', context]
    return render(*a)


