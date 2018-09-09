from django import forms

class CommentForm(forms.Form):
    new_comment = forms.CharField(label='New comment', max_length=400)

    def clean_new_comment(self):
        data = self.cleaned_data['new_comment']
        return data
