from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from ourapp.forms import ExampleForm

# Create your views here.
def ourapp(request):
    if request.method=="POST":
        form=ExampleForm(request.Post)
        if form.is_valid():
            form.save()

    else:
          form=ExampleForm()

        
  

    return render(request,'ourapp.html',{'form':form})