from django.shortcuts import render
from .models import Student

def app(request):
    return render(request,"index.html")

def show(request):
    val=request.GET['val']
    # if val=='':
    #     val=[]
    # else:
    #     val=int(val)
    #     val=[i for i in range(1,val+1)]
    if val=='':
        val=[]
    else:
        val=Student.objects.get(id=val)
        if val is None:                            # line 18,19 ko comment kia to bhi kam chal jayega
            val="No Student found"
    return render(request,'StudentDisplay.html',{'val':val})