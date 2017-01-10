from django import forms
from .models import Article


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(label='Your email address')
    renvoi = forms.BooleanField(help_text="Check if you want to get a copy of the mail sent.", required=False)

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        subject = cleaned_data.get('subject')
        message = cleaned_data.get('message')

        if subject and message:  # do message and subject are valid ?
            if "pizza" in subject and "pizza" in message:
                msg = forms.ValidationError('Do you talk about pizza in the subject and message ? No !')
                self.add_error("message", msg)
        return cleaned_data  # don't forget to return the data if everything is ok


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class NewContactForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()



