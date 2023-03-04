from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'app-profile.html')

def formedit(request):
    return render(request, 'form-validation.html')

def pagelock(request):
    return render(request, 'page-lock.html')

def login(request):
    return render(request, 'page-login.html')

def logout(request):
    return render(request, 'page-logout.html')

def signup(request):
    return render(request, 'page-register.html')

def datatable(request):
    return render(request, 'table-datatable.html')

def widgets(request):
    return render(request, 'widgets.html')

def page400(request):
    return render(request, 'page-error-400.html')

def page404(request):
    return render(request, 'page-error-404.html')

def page403(request):
    return render(request, 'page-error-403.html')

def page500(request):
    return render(request, 'page-error-500.html')

def page503(request):
    return render(request, 'page-error-503.html')

