from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django import forms
from .models import Mail


class ComposeMailView(LoginRequiredMixin, CreateView):
    """
    View for writing and sending direct messages to other users
    """
    model = Mail
    success_url = reverse_lazy('mails:mailbox')

    class ComposeForm(forms.ModelForm):
        recipient_username = forms.CharField(label="Recipient's username")

        class Meta:
            model = Mail
            fields = ['recipient_username', 'subject', 'body']

        def clean_recipient_username(self):
            username = self.cleaned_data['recipient_username']
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                raise forms.ValidationError("User does not exist")
            return user

    form_class = ComposeForm

    def get_initial(self):
        initial = super().get_initial()
        # Pre-fill recipient if provided in URL
        recipient_username = self.kwargs.get('recipient_username') or self.request.GET.get('to')
        if recipient_username:
            initial['recipient_username'] = recipient_username
        
        # Pre-fill subject if a story title is provided
        story_title = self.request.GET.get('story')
        if story_title:
            initial['subject'] = story_title
        
        return initial

    def form_valid(self, form):
        mail = form.save(commit=False)
        mail.sender = self.request.user
        mail.recipient = form.cleaned_data['recipient_username']
        mail.save()
        return super().form_valid(form)



class MailboxView(LoginRequiredMixin, ListView):
    """
    Private list of all the non-archived mails a user has received
    """
    model = Mail
    template_name = 'mails/mailbox.html'
    context_object_name = 'mails'

    def get_queryset(self):
        return Mail.objects.filter(recipient=self.request.user, is_archived=False).order_by('-timestamp')


def archive_mail(request, pk):
    """
    Function for the 'Archive' button on a mail
    """
    mail = get_object_or_404(Mail, pk=pk)
    if mail.recipient != request.user:
        return HttpResponseForbidden("You don't have permission to archive this mail.")
    mail.is_archived = True
    mail.save()
    return redirect('mails:mailbox')

def unarchive_mail(request, pk):
    """
    Function to remove a mail from the archive
    """
    mail = get_object_or_404(Mail, pk=pk)
    if mail.recipient != request.user:
        return HttpResponseForbidden("You don't have permission to unarchive this mail.")
    mail.is_archived = False
    mail.save()
    return redirect('mails:archived')


class ArchivedMailView(LoginRequiredMixin, ListView):
    """
    Private list showing all the received mails that a user has archived
    """
    model = Mail
    template_name = 'mails/archived.html'
    context_object_name = 'mails'

    def get_queryset(self):
        return Mail.objects.filter(recipient=self.request.user, is_archived=True).order_by('-timestamp')
