from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import Post, Category


class PostCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        label='Категория',
        widget=forms.Select(attrs={'class': 'form-select'}),
        queryset=Category.objects.all()
    )
    title = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # text = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control'}))
    text = forms.CharField(label='Текст', widget=CKEditorUploadingWidget(attrs={'class': 'form-control'}))
    textic = RichTextUploadingField()

    class Meta:
        model = Post
        exclude = ('author',)
