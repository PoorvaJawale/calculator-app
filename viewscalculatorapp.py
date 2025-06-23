from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def submitquery(request):
    q = request.GET.get('query', '')
    try:
        ans = eval(q)
        error = False
    except:
        ans = None
        error = True

    return render(request, 'index.html', {'q': q, 'ans': ans, 'error': error})
