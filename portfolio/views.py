from django.shortcuts import render
from .models import Contact ,Service,About,Index
from django.views.generic.edit import FormView
from .forms import ContactForm
from .bot import send_message
from django.views.generic.list import ListView



class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
      name = form.cleaned_data.get('name')
      email = form.cleaned_data.get('email')
      content = form.cleaned_data.get('content')
      text = f"Name: {name}\nEmail: {email}\ntext: {content}"
      send_message(text)
      Contact.objects.create(
        name=name,
        email=email,
        content=content
    )
      return super().form_valid(form)

# def home_view(request):
#  return render(request=request,template_name='index.html')

class IndexListView(ListView):
  model = Index
  template_name = 'index.html'
  context_object_name = 'index'

class AboutListView(ListView):
  model = About
  template_name = 'about.html'
  context_object_name = 'about'

class ServiceListView(ListView):
  model = Service
  template_name = 'service.html'
  context_object_name = 'service'
