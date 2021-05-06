from django.shortcuts import render


def hello(request):
    return render(request, 'first_blog/blog/templates/blog/index.html')
