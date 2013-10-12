from django.db import models
from django.forms import ModelForm

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    phone_number = models.IntegerField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    is_starred = models.BooleanField(default = False)
    image = models.ImageField(upload_to='fonebuk/photos/', null=True, blank=True)
	
    def __unicode__(self):  
        return self.name

		
class ContactForm(ModelForm):
    class Meta:
		model = Contact		