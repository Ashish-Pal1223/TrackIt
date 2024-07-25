from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class animeForm(forms.Form):
    anime_name = forms.CharField(max_length=100, 
                                 label="",
                                 widget=forms.TextInput({"class": "form-items", "placeholder": "Anime Name"}))
    rating = forms.IntegerField(label="",
                                min_value=1,
                                max_value=5,
                                widget=forms.TextInput({"class": "form-items", 
                                                        "placeholder": "Rating",
                                                        "min": 1,"max": 5,
                                                        "size" : 15}))
    genre = forms.ChoiceField(label='',
                              choices=[
                                ('action', 'Action'),
                                ('romance', 'Romance'),
                                ('psychology', 'Psychology')],
                              widget=forms.Select(
                                attrs={
                                    'class': 'form-items'}))