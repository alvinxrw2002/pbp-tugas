from django import forms

class TaskForm(forms.Form):
    judul = forms.CharField(max_length=255)
    deskripsi = forms.CharField(max_length=1000000)