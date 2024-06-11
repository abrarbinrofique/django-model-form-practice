from django.shortcuts import render
from ourappmodelform.forms import Example

# Create your views here.
def ppmodelform(request):
    if request.method=="POST":
        form=Example(request.Post)
        if form.is_valid():
            form.save()

    else:
          form=Example()


    

    return render(request,'ourappmodelform.html',{'form':form})