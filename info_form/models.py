from django.db import models


class Contact(models.Model):
    Name = models.CharField(default="", max_length=100, null=True)
    Email = models.EmailField(default="", max_length=254)
    Mobile = models.CharField(default="", max_length=12)
    Message = models.TextField(default="", max_length=400)
    # files = models.FileField(upload_to='files/')
    files = models.FileField(verbose_name='files_to_upload', null=True)

    # uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
