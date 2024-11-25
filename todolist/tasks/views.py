from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Tag
from .forms import TaskForm, TagForm


def home(request):
    tasks = Task.objects.all().order_by("is_done", "-created_at")
    return render(request, "tasks/home.html", {"tasks": tasks})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm()
    return render(request, "tasks/add_task.html", {"form": form})


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "tasks/tag_list.html", {"tags": tags})


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm()
    return render(request, "tasks/create_task.html", {"form": form})


def create_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tag_list")
    else:
        form = TagForm()
    return render(request, "tasks/create_tag.html", {"form": form})


def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/create_task.html", {"form": form})


def add_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tag_list")
    else:
        form = TagForm()
    return render(request, "tasks/add_tag.html", {"form": form})


def delete_task(task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect("home")


def toggle_task_status(task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_done = not task.is_done
    task.save()
    return redirect("home")
