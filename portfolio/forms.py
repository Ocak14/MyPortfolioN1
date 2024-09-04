from django.forms import ModelForm
from .models import Contact
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name",  "email", "content"]
    
    def clean(self):
        super(ContactForm, self).clean()
        
        name = self.cleaned_data.get('name')
        content = self.cleaned_data.get('content')

        # Conditions for name length
        if name:
            if len(name) < 3:
                raise forms.ValidationError("Name must be at least 3 characters")
        else:
            self._errors['name'] = self.error_class([
                    'Name is required'])

        if not content:
            self._errors['content'] = self.error_class([
                    'Content is required'])
        
        return self.cleaned_data
