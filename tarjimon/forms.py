from django import forms

from tarjimon.models import Dictio


class DictioForm(forms.ModelForm):
    class Meta:
        model = Dictio
        fields = '__all__'
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 15, 'class': 'form-control'}),
        }