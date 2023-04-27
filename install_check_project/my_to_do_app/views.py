from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

def index(request):
    todos = Todo.objects.all()
    content = {'todos': todos}
    return render(request, 'my_to_do_app/index.html', content)

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content=user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse("create Todo를 할거야! =>" + user_input_str)

# Todo delete
def deleteTodo(request):
    todo_id = request.POST['todoNum']
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))



    