from .models import Articles
from django.forms import ModelForm, TextInput, DateInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            })
        }