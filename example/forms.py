from .models import TaskList,TerraformProject
from django import forms


class TaskListForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = "__all__"


class TerraformProjectForm(forms.ModelForm):
    class Meta:
        model = TerraformProject
        fields = "__all__"