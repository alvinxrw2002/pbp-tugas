from django import forms

class TaskForm(forms.Form):
    judul = forms.CharField(max_length=255)
    deskripsi = forms.CharField(widget=forms.Textarea)