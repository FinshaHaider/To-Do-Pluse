from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout

from .models import Tasks,Todo,Users,Notes
from .forms import TaskForm,SignupForm,LoginForm,NoteForm
# Create your views here.
def home(request):
    user=Users.objects.all()
    return render(request, 'home.html',{'user':user})
def index(request):
    return render(request, 'index.html')
# def sin_up(request):
#     if request.POST:
#         username=Users.objects.POST['username']
#         password=Users.objects.POST['password']
#         users=Users(username=username,password=password)
#         if users.is_valid():
#             users.save()
#             return redirect('login')
#     else:
#         return render(request,'register.html')

def user_signup(request):
    if request.POST:
        form=SignupForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('login')
    else:
        form=SignupForm()   
    return render(request,'signup.html',{'form':form})

def user_login(request):
    if request.POST:
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('index')
        else:
            form=LoginForm()
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

def user_logout(request):
    logout(request)
    return render(request,'logout.html')

def user_conform(request):
    logout(request)
    return render(request,'conform.html')





def add_todo(request):
    if request.POST:
        new_task=request.POST.get('task')
        if new_task:
            Todo.objects.create(task=new_task)
        return redirect('personal')
    return render(request,'addtask.html')

def delete_todo(request,pkey):
    
    todo=Todo.objects.get(pk=pkey)
    todo.delete()
    return redirect('personal')

def personal(request):
    tasks=Todo.objects.all()
    return render(request, 'personal.html',{'tasks':tasks})

def notes(request):
    note=Notes.objects.all()
    return render(request, 'notes.html',{'note':note})

def add_note(request):
    if request.POST:
        nform=NoteForm(request.POST) 
        if nform.is_valid():
            nform.save()
            return redirect('notes')
        else:
            nform=NoteForm()
    else:
        nform=NoteForm()
    return render(request,'addnote.html',{'form':nform})

def delete_note(request,pkey):
    note=Notes.objects.get(pk=pkey)
    note.delete()
    return redirect('notes')
    

# def complete_todo(request,pk):
#     todo=Todo.objects.get(pk=pk)
#     todo.completed=True
#     todo.save()
#     return redirect('home')







def task(request):
    tas=Tasks.objects.all()
    return render(request, 'tasks.html',{'task':task} )
def addtask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task=form.cleaned_data['task']
            priority=form.cleaned_data['priority']
            deadline=form.cleaned_data['deadline']
            task_obj=Tasks(task=task,priority=priority,deadline=deadline)
            task_obj.save()

            # form.save()
            return redirect('home')
        else:
            form=TaskForm()
    else:
        form=TaskForm()
    return render(request, 'addtask.html',{'form':form})
def delete_task(request,pkey):
    # task_id=request.GET.get('task_id')
    task=Tasks.objects.get(pk=pkey)
    task.delete()
    return redirect('home')

def edit_task(request,pkey):
    pass
def task_details(request):
    return render(request,'home.html')