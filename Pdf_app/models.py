from django.db import models

class PDFFile(models.Model):
    file = models.FileField(upload_to='pdfs/')
    extracted_text = models.TextField(default ="")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

