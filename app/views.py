from django.shortcuts import render

# Create your views here.
def hi(request):
    return render(request,'hi.html')
def bye(request):
    return render(request,'bye.html')