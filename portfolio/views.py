
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Portfolio

def portfolio_view(request):
    users=Portfolio.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        bio = request.POST.get('bio')  # Added bio
        company = request.POST.get('company')  # Added company
        role = request.POST.get('role')  # Added role
        experience = request.POST.get('experience')
        pname = request.POST.get('pname')
        plink = request.POST.get('plink')
        experience = request.POST.get('work')
        education = request.POST.get('education')
        cname = request.POST.get('cname')
        clink = request.POST.get('clink')
        u = Portfolio(
            name=name,
            email=email,
            bio=bio,
            company=company,
            role=role,
            years_of_experience=experience,
            project_name=pname,
            project_link=plink,
            certification_name=cname,
            certification_link=clink
        )
        u.save()
    return render(request, 'portview.html',{'users':users})

def detailsview(request,user_id):
    user=Portfolio.objects.get(id=user_id)
    return render(request, 'detailsview.html', {'user': user})
def updateuser(request,user_id):
    user = Portfolio.objects.get(id=user_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')  # Added email
        bio = request.POST.get('bio')  # Added bio
        company = request.POST.get('company')  # Added company
        role = request.POST.get('role')  # Added role
        experience = request.POST.get('experience')  # Added experience
        pname = request.POST.get('pname')
        plink = request.POST.get('plink')
        cname = request.POST.get('cname')
        clink = request.POST.get('clink')

        # Update user profile
        user.name = name
        user.email = email
        user.bio = bio
        user.company = company
        user.role = role
        user.years_of_experience = experience if experience else None 
        user.project_name = pname
        user.project_link = plink
        user.certification_name = cname
        user.certification_link = clink

        # Save the changes
        user.save()
    return render(request, 'updateview.html',{'user':user})
