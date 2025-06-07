from django.shortcuts import render

# Create your views here.

def calculator_view(request):
    template_name = 'app1/show.html'
    context={}
    return render(request,template_name,context)
