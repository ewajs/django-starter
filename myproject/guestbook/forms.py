from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"}),
    )
    # For a form we'll use CharField but with a widget property
    comment = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Comment"})
    )
