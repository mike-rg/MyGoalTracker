from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def principal(request):
    return render(request, 'principal.html')
