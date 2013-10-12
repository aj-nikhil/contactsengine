from django import ModelForm

from fonebuk.models import Contact

class ContactForm(ModelForm):
    class Meta:
		model=Contact
