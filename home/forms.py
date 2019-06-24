
from django import forms
from home.models import Book,Person
class Bookforms(forms.Form):
    name=models.CharField(label='Book Name',
                                widget=forms.TextInput(attrs={'maxlength':'30','placeholder':'Book Name',
                                'class':'form-control'}))
    Person=forms.ModelChoicefield(
                    queryset=Author.objects.all(),
                    empty_label='Author',widget=forms.Select(attrs={'name':'author','id':'author',
                    'class':'custom-select'}))
    summary=forms.CharField(label='Summary',
                                widget=forms.Textarea(attrs={'placeholder':'Summary','name':'summary',
                                'id':'summary','class':'form-control'}))
    isbn=forms.CharField(label='ISBN Number',
                                widget=forms.TextInput(attrs={'placeholder':'ISBN Number',
                                'class':'form-control','name':'isbn','id':'isbn'}))
    genre=forms.ModelMultipleChoicefield(queryset=Genre.objects.all(),
                               widget=forms.CheckboxSelectMultiple)
    class Meta
        model=Book
        fields='__all__'              
   