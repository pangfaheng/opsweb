from .models import single_task_task
from django import forms


class single_task_form(forms.ModelForm):
    class Meta:
        model = single_task_task
        fields = "__all__"
