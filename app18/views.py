from django.shortcuts import render

# Create your views here.
def ifcondition(request):
    d={'a': 200,'b':50}
    return render(request,'ifcondition.html',d)
