
from django import forms
from .models import Interest,Project,Memory

# Create the form class
class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = "__all__"


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"        


class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = "__all__"        