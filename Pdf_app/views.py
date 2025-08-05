from django.shortcuts import render
from .forms import PDFUploadFile
from .models import PDFFile
import fitz  # PyMuPDF

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadFile(request.POST, request.FILES)
        if form.is_valid():
            pdf_instance = form.save(commit=False)
            pdf_file = request.FILES['file']

            # Extract text from PDF
            doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
            extracted_text = ""
            for page in doc:
                extracted_text += page.get_text()
            doc.close()

            # Save extracted text to model
            pdf_instance.content = extracted_text
            pdf_instance.save()

            return render(request, 'Pdf_app/result.html', {'text': extracted_text})
    else:
        form = PDFUploadFile()
    return render(request, 'Pdf_app/upload.html', {'form': form})
