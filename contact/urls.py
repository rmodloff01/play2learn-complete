from django.urls import path

from .views import ContactUsView, ContactUsThanksView

app_name = 'contact'
urlpatterns = [
    path('contact-us/', ContactUsView.as_view(), name='app'),
    path('contact-us/thanks/', ContactUsThanksView.as_view(), name='thanks'),
]