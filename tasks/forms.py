from django import forms
from .models import Tasks

class TaskForm(forms.ModelForm):
    class Meta():
        model = Tasks
        fields = ['title', 'description', 'important']
        widgets = {
            "title": forms.TextInput(attrs={"class": "border-black border-2 border-solid rounded-sm my-2 p-3"}),
            "description": forms.Textarea(attrs={"class": "border-black border-2 border-solid rounded-sm my-2 p-3"}),
            "important": forms.CheckboxInput(attrs={"class": "ml-1 inline-block"})
        }