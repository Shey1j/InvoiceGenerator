from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'index.html')

def faqView(request):
    return render(request, 'faq.html')

def contactView(request):
    return render(request, 'contact.html')


def userStatisticsView(request):
    return render(request, 'user-statistics.html')


def pricingView(request):
    return render(request, 'pricing.html')


def invoiceGuideView(request):
    return render(request, 'guide.html')


def dashboardView(request):
    return render(request, 'dashboard.html')


def aboutView(request):
    return render(request, 'about.html')

