from books.models import Review
from django import forms

class ReviewForm(forms.Form):
    review=forms.CharField(widget=forms.Textarea(attrs={'name':'review','class':'border rounded p-2 w-full','cols':'30','rows':'5','placeholder':'Write your Review'}))
    image=forms.ImageField(required=False)


class ReviewModelForm(forms.ModelForm):
    image=forms.ImageField(required=False)
    class Meta:
        model = Review
        fields=['body','image']
        widgets={'body':forms.Textarea(attrs={'name':'review','class':'border rounded p-2 w-full','cols':'30','rows':'5','placeholder':'Write your Review'})}