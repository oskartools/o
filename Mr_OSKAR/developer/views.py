from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import JobApplicationForm
from .models import DeveloperApplication
from django.contrib.auth.decorators import login_required

def apply_for_job(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            # حفظ البيانات في قاعدة البيانات
            DeveloperApplication.objects.create(
                full_name=form.cleaned_data['full_name'],
                gender=form.cleaned_data['gender'],
                country=form.cleaned_data['country'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                portfolio=form.cleaned_data['portfolio'],
                experience=form.cleaned_data['experience'],
                education=form.cleaned_data['education'],
                skills=form.cleaned_data['skills'],
            )
            return render(request, 'success.html', {'name': form.cleaned_data['full_name']})
    else:
        form = JobApplicationForm()
    return render(request, 'apply.html', {'form': form})

@login_required
def view_applications(request):
    applications = DeveloperApplication.objects.all()
    return render(request, 'applications.html', {'applications': applications})