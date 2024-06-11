from django import forms
from .models import Homework


# class HomeworkForm(forms.ModelForm):
#     description = forms.CharField(widget=forms.Textarea)
#     homework_file = forms.FileField(widget=forms.Textarea)


class HomeworkForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    homework_file = forms.FileField()

    class Meta:
        model = Homework
        fields = ['description', 'homework_file']
