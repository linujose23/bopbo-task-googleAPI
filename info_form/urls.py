from django.urls import path
from .views import FormSubmission

urlpatterns = [
    path("", FormSubmission, name="formsub"),
    # path("thanks/", thanks, name="thanks"),
]
