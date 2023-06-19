from django.shortcuts import render,redirect
from .models import Task
from .forms import Totdoform

# Create your views here.
def add(requset):
    task = Task.objects.all()
    if requset.method=='POST':
        name1 = requset.POST.get('task','')
        priority1 = requset.POST.get('priority','')
        date1 = requset.POST.get('date','')
        obj = Task(name=name1,priority=priority1,date=date1)
        obj.save()


    return render(requset,'index.html' ,{'task':task})

def Delete(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    
    return render(request,'delete.html')

def Update(request,taskid):
    task1 = Task.objects.get(id=taskid)
    form = Totdoform(request.POST or None,instance=task1)
    if form.is_valid():
        form.save()
        redirect('/')

    return render(request,'edit.html',{'task1':task1,'form':form})