from django.shortcuts import render, redirect

# Create your views here.
def resume_pdf(request):
    return redirect('https://webscrape-bucket.s3.amazonaws.com/Cloud-DevOps-Engineer-Resume.pdf')

