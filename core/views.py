from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from .models import Resume, CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
     
        if CustomUser.objects.filter(email=email).exists():
           messages.error(request, "Email already exists")
           return render(request, 'signUp.html')
        
        user = CustomUser.objects.create_user(username=email, email=email, password=password)
        login(request, user)
        return redirect('dashboard')
    
    return render(request, 'signUp.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Find user by email first
        try:
            user_obj = CustomUser.objects.get(email=email)
            username = user_obj.username
        except CustomUser.DoesNotExist:
            username = None
            
        # Authenticate with username
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return render(request, 'signIn.html', {'error': 'Invalid credentials'})
            
    return render(request, 'signIn.html')

def logout_view(request):
    logout(request)
    return redirect('signin')

@login_required(login_url='/user/signIn')
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='/user/signIn')
def submit_resume(request):
    if request.method == 'POST':
        user = request.user
        
        # Extract basic fields
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        linkedin = data.get('linkedin')
        address = data.get('address')
        website = data.get('website')
        briefintro = data.get('briefintro')
        
        # Helper to parse arrays
        def parse_list(key_suffix, keys):
            # keys is a list of field names e.g. ['degree', 'start', 'end', 'uni']
            # request.POST.getlist(key + '[]')
            # Assuming data comes as degree[], start[], etc.
            result = []
            # Get length of first array
            first_list = request.POST.getlist(keys[0] + '[]')
            for i in range(len(first_list)):
                item = {}
                for key in keys:
                    val_list = request.POST.getlist(key + '[]')
                    # handle index out of bound just in case
                    item[key] = val_list[i] if i < len(val_list) else ''
                result.append(item)
            return result

        education = parse_list('', ['degree', 'start', 'end', 'uni'])
        
        # Languages: lanname[], lanper[]
        languages = []
        lannames = request.POST.getlist('lanname[]')
        lanpers = request.POST.getlist('lanper[]')
        for i in range(len(lannames)):
            languages.append({
                'lanname': lannames[i],
                'lanper': lanpers[i] if i < len(lanpers) else ''
            })

        # Experience: ex-start[], ex-end[], cname[], job-role[], job-des[]
        # Mapping to keys expected by original logic/template?
        # distinct keys: companyName, expStart, expEnd, jobRole, jobDes
        # POST keys: cname[], ex-start[] ...
        experiences = []
        cnames = request.POST.getlist('cname[]')
        ex_starts = request.POST.getlist('ex-start[]')
        ex_ends = request.POST.getlist('ex-end[]')
        job_roles = request.POST.getlist('job-role[]')
        job_des = request.POST.getlist('job-des[]')
        
        for i in range(len(cnames)):
            experiences.append({
                'companyName': cnames[i],
                'expStart': ex_starts[i] if i < len(ex_starts) else '',
                'expEnd': ex_ends[i] if i < len(ex_ends) else '',
                'jobRole': job_roles[i] if i < len(job_roles) else '',
                'jobDes': job_des[i] if i < len(job_des) else ''
            })
            
        # Skills: skill-name[], skill-per[]
        skills = []
        skill_names = request.POST.getlist('skill-name[]')
        skill_pers = request.POST.getlist('skill-per[]')
        for i in range(len(skill_names)):
            skills.append({
                'skillName': skill_names[i],
                'skillPer': skill_pers[i] if i < len(skill_pers) else ''
            })
            
        # Expert: expert[]
        experts = request.POST.getlist('expert[]')
        interests = ["Reading", "Writing"] # Hardcoded in original controller? 
        # Lines 127 in formController.js: interests: ["Reading", "writing"],
        
        # Versioning logic
        # Find active valid resume and archive it
        Resume.objects.filter(user=user, active=True, archive=False).update(archive=True)
        
        # Determine version
        last_resume = Resume.objects.filter(user=user).order_by('-version').first()
        version = last_resume.version + 1 if last_resume else 1
        
        resume = Resume.objects.create(
            user=user,
            name=name,
            email=email,
            contact=phone,
            linkedin=linkedin,
            address=address,
            website=website,
            briefIntro=briefintro,
            education=education,
            languages=languages,
            experience=experiences,
            skills=skills,
            expert=experts, # Storing simple list of strings
            interests=interests,
            version=version,
            active=True,
            archive=False
        )
        
        return redirect('dashboard')
        
    return render(request, 'form/index.html')

@login_required(login_url='/user/signIn')
def resume_form(request):
    return render(request, 'form/index.html')

@login_required(login_url='/user/signIn')
def view_resume(request, template_name):
    user = request.user
    resume = Resume.objects.filter(user=user, archive=False).first()
    
    if not resume:
        return render(request, 'form/index.html', {'message': "You need to fill the form first"})
    
    # Context to match what EJS expects.
    # original sends 'userFormData' as root object properties?
    # res.render(..., userFormData) -> variables are top level
    # But later it says res.render(..., { portfolioData: userFormData })
    # template code uses `portfolioData.name` ? or `name`?
    # I saw app.js line 65: res.render("template2/pages/about", { portfolioData: userFormData });
    # line 171: res.render(`./${templateName}/index`, userFormData);
    # This implies template1 uses direct keys, template2 might use portfolioData?
    # I'll provide both.
    
    context = {
        'portfolioData': resume,
        # Flatten resume fields for direct access if needed
        'name': resume.name,
        'email': resume.email,
        'contact': resume.contact,
        'address': resume.address,
        'linkedin': resume.linkedin,
        'website': resume.website,
        'briefIntro': resume.briefIntro,
        'expert': resume.expert,
        'education': resume.education,
        'languages': resume.languages,
        'experience': resume.experience,
        'skills': resume.skills,
        'interests': resume.interests,
    }
    
    return render(request, f'{template_name}/index.html', context)
    
@login_required(login_url='/user/signIn')
def template_page(request, template_name, page):
    # e.g. /template2/pages/about
    user = request.user
    resume = Resume.objects.filter(user=user, archive=False).first()
    if not resume:
        return render(request, 'form/index.html', {'message': "You need to fill the form first"})
    
    context = {'portfolioData': resume}
    return render(request, f'{template_name}/pages/{page}.html', context)

def admin_dashboard(request):
    if not request.user.is_superuser:
         return redirect('signin')
    
    total_count = Resume.objects.count() # simplistic, maybe verify logic
    user_count = CustomUser.objects.count()
    return render(request, 'adminDashboard.html', {
        'totalCount': total_count,
        'userCount': user_count
    })

def admin_signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user_obj = CustomUser.objects.get(email=email)
            username = user_obj.username
        except CustomUser.DoesNotExist:
            username = None

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                messages.error(request, "Access denied. Admin only.")
                return render(request, 'adminSignIn.html', {'error': 'Access denied'})
        else:
             messages.error(request, "Invalid credentials")
             return render(request, 'adminSignIn.html', {'error': 'Invalid credentials'})
             
    return render(request, 'adminSignIn.html')
