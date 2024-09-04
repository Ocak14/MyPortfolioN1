from django.urls import path
from .views import IndexListView,AboutListView,ContactFormView,ServiceListView


urlpatterns = [
    path('', IndexListView.as_view(), name='index-page'),
    path('about/',AboutListView.as_view(),name='about-page'),
    path('contact/', ContactFormView.as_view(), name='contact-page'),
    path('service/',ServiceListView.as_view(),name='service-page'),
        
]