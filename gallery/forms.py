from django import forms

class ReviewForm(forms.Form):
    raiting = forms.IntegerField(max_value=4, min_value=0)
    content = forms.CharField(widget=forms.Textarea)