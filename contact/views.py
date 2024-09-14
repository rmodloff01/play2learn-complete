import html
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from common.utils.email import send_email
from .forms import ContactUsForm

class ContactUsView(FormView):
    template_name = 'contact/contact_us.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('contact:thanks')

    def form_valid(self, form):
        data = form.cleaned_data
        to = 'reese.modloff@gmail.com'
        subject = 'Contact Us Received!'
        content = f'''<p>Hey Play2Learn!</p>
            <p>Contact Us Received:</p>
            <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        
        content += '</ol>'

        send_email(to, subject, content)
        return super().form_valid(form)

class ContactUsThanksView(TemplateView):
    template_name = 'contact/thanks.html'