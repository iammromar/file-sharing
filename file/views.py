from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import UploadFile, Comment, FileUserDetect
from .forms import UploadFileForm, CommentForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login')
def home_view(request):
	return render (request=request, template_name="home.html", context={})

@login_required(login_url="/accounts/login")
def upload_file(request):
    all_files = []
    # UploadedFile.objects.all().delete()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.creator = request.user
            if form.data['friend']:
                user_exists = User.objects.filter(Q(username=form.data['friend']) | Q(email=form.data['friend']))[0]
                if not user_exists:
                    messages.error(request, "Bu istifadəçi mövcud deyil")
                    return redirect('login')
                
                uploaded_file = form.save()
                cm_per = request.POST.get('comment_permission')
                if cm_per == 'on':
                    cm_per = True
                else:
                    cm_per = False
                file_user = FileUserDetect(user=user_exists, file=uploaded_file, permit=True, comment_permission=cm_per)
                file_user.save()            

            return redirect('/upload')
    else:
        form = UploadFileForm()
    
    creator_files = UploadFile.objects.filter(creator=request.user)
    friend_permits = FileUserDetect.objects.filter(user=request.user)

    for friend_permit in friend_permits:
        one_file = UploadFile.objects.get(id=friend_permit.file.id)
        all_files.append(one_file)

    new_all_files = list(creator_files) + list(all_files)
    return render(request, 'upload_file.html', {'form': form, 'files': new_all_files})

@login_required(login_url="/accounts/login")
def download_file(request, file_id):

    uploaded_file = UploadFile.objects.get(pk=file_id)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')

    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

@login_required(login_url="/accounts/login")
def file_detail_view(request, id = None):
    file = get_object_or_404(UploadFile, id = id)
    file_user = FileUserDetect.objects.filter(file=file)[0]

    user_comment_permission = False

    if file_user:
        user_comment_permission = file_user.comment_permission

    print('user_comment_permission', user_comment_permission)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            
            form.instance.creator = request.user
            form.instance.file = file

            form.save()
            return HttpResponseRedirect('/file/%d/'%id)
    else:
        form = CommentForm()
    comments = Comment.objects.filter(file=file)
    return render(request, 'file_detail.html', {'file': file, 'form': form, 'comments': comments, 'user_comment_permission': user_comment_permission})
