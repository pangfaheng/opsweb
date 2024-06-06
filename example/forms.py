from .models import TaskList
from django import forms


class TaskListForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = "__all__"
