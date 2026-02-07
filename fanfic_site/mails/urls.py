from django.urls import path
from .views import (
    ComposeMailView,
    MailboxView,
    ArchivedMailView,
    archive_mail,
    unarchive_mail,
)

app_name = "mails"

urlpatterns = [
    path("", MailboxView.as_view(), name="mailbox"),  # /mails/
    path("archive/<int:pk>/", archive_mail, name="archive"),  # /mails/archive/1/
    path(
        "unarchive/<int:pk>/", unarchive_mail, name="unarchive"
    ),  # /mails/unarchive/1/
    path("archived/", ArchivedMailView.as_view(), name="archived"),  # /mails/archived/
    path("compose/", ComposeMailView.as_view(), name="compose"),
    path(
        "compose/<str:recipient_username>/",
        ComposeMailView.as_view(),
        name="compose_with_recipient",
    ),
]
