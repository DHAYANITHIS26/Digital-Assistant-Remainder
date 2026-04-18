from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Group
from accounts.models import User

@login_required
def group_list(request):
    groups = Group.objects.filter(members=request.user)
    return render(request, 'groups/group_list.html', {'groups': groups})

@login_required
def create_group(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        group = Group.objects.create(name=name, description=description, created_by=request.user)
        group.members.add(request.user)
        
        # Add members by email if provided
        member_emails = request.POST.get('member_emails', '').split(',')
        for email in member_emails:
            email = email.strip()
            if email:
                user = User.objects.filter(email=email).first()
                if user:
                    group.members.add(user)
                    
        return redirect('groups:list')
    return render(request, 'groups/group_list.html') # Reusing same template for simplicity or build a modal
