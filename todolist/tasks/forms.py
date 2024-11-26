from django import forms
from .models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]

    content = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Enter task details..."}))
    deadline = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={"type": "datetime-local"}))

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
