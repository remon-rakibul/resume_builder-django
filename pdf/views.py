from django.shortcuts import redirect, render
from .models import Profile
from django.http import HttpResponse
from django.template import loader
import pdfkit

# Create your views here.
def accept(request):
    if request.method == 'POST':
        profile = Profile(
            name = request.POST.get('name'),
            phone = request.POST.get('phone'),
            email = request.POST.get('email'),
            school = request.POST.get('school'),
            degree = request.POST.get('degree'),
            university = request.POST.get('university'),
            skills = request.POST.get('skills'),
            about = request.POST.get('about'),
            experience = request.POST.get('experience'),
            publications = request.POST.get('publications'),
            awards = request.POST.get('awards'),
            certifications = request.POST.get('certifications')
        )
        profile.save()
        return redirect('accept')
    else:
        return render(request, 'pdf/accept.html')

def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile': user_profile})
    pdf = pdfkit.from_string(html, False, {'page-size': 'Letter', 'encoding': 'UTF-8'})
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachments'
    return response

def list(request):
    profiles = Profile.objects.all()
    return render(request, 'pdf/list.html', {'profiles': profiles})