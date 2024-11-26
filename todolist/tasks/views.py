from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Tag
from .forms import TaskForm, TagForm
from django.urls import reverse_lazy
from django.views import generic


def home(request):
    task_list = Task.objects.all()
    return render(request, "tasks/home.html", {"task_list": task_list})


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "tasks/task_list.html"
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.order_by("is_done", "-created_at")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "tasks/tag_list.html"
    paginate_by = 3

    def get_queryset(self):
        return Tag.objects.all()


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag_list")
    template_name = "tasks/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag_list")
    template_name = "tasks/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag_list")
    template_name = "tasks/tag_confirm_delete.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/create_task.html"
    success_url = reverse_lazy("task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/create_task.html"
    success_url = reverse_lazy("tasks:task_list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("tasks:task_list")


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()

    return render(request, "tasks/create_task.html", {"form": form})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm()
    return render(request, "tasks/add_task.html", {"form": form})


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect('tasks:home')


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "tasks/tag_list.html", {"tags": tags})


def add_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tag-list")
    else:
        form = TagForm()
    return render(request, "tasks/add_tag.html", {"form": form})


def create_tag(request):
    if request.method == "POST":
        tag_name = request.POST.get("name")
        Tag.objects.create(name=tag_name)
        return redirect("tag-list")
    return render(request, "tasks/create_tag.html")


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.name = request.POST.get("name", task.name)
        task.description = request.POST.get("description", task.description)
        task.save()
        return redirect("task-list")

    return render(request, "tasks/update_task.html", {"task": task})


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return render(request, "tasks/task-list.html")
