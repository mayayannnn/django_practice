from django.shortcuts import render
# from todo.models import Todo

# Create your views here.

def index(request):
    # todo = Todo(memo = "memo")
    # todo.save()
    return render(request, "index.html")