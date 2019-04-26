from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from textEmails.models import *


# Create your views here.
class InboxView(TemplateView):
    template_name = 'textEmails/mailbox.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mail = Email.objects.all()
        priorities = ["Medicine", "Education", "Travel", "Job", "Government", "Fashion", "Sports", "Economy", "Marriage", "Family"]
        context['mails'] = mail
        context['pri_list'] = priorities
        return context


class ContactUsView(TemplateView):
    template_name = 'textEmails/contactus.html'
