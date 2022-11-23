import datetime
from django.core import serializers
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from todolist.models import Task
from todolist.forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Wajibkan login karena task yang ditampilkan akan disesuaikan berdasarkan usernya
@login_required(login_url='/todolist/login')
def show_todolist(request):
    # Tampilkan task berdasarkan user yang sedang login
    logged_in_user = request.user
    tasks = Task.objects.filter(user = logged_in_user)
    context = {
        'todolist' : tasks,
        'user' : logged_in_user
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.user:
        logout_user(request)

    if request.method == 'POST':
        # Autentikasikan username dan password
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')

    context = {}
    return render(request, 'login.html', context)

# Tentu saja perlu login terlebih dahulu untuk menjlankan mekanisme logout
@login_required(login_url='/todolist/login')
def logout_user(request):
    # Redirect ke halaman login dan hapus cookie
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

# Syaratkan login untuk membuat task baru, karena instance Task memerlukan parameter user
@login_required(login_url='/todolist/login')
def create_task(request):
    # Jika request-nya berbentuk POST, proses data form-nya
    if request.method == 'POST':
        
        # Membuat instance form dan sesuaikan dengan data request
        form = TaskForm(request.POST)

        # Jika valid, ambil entrynya, kemudian masukan ke variable yang sesuai
        if form.is_valid():
            current_user = request.user
            task_title = form.cleaned_data['judul']
            task_description = form.cleaned_data['deskripsi']

            # Membuat instance task berdasarkan entry pada form, kemudian simpan ke database 
            new_task = Task(user = current_user, title = task_title, description = task_description)
            new_task.save()

            # Kembali ke halaman todolist jika berhasil menambahkan task
            return redirect('todolist:show_todolist')

    # jika method-nya GET atau yang lainnya, buat form kosong
    else:
        form = TaskForm()

    # Tampilkan form baru
    return render(request, 'taskform.html', {'form': form})

@login_required(login_url='/todolist/login')
def delete_task(request, task_id):
    task = Task.objects.get(pk = task_id)
    task.delete()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login')
def update_task_status(request, task_id):
    task = Task.objects.get(pk = task_id)
    present_status = task.is_finished
    updated = not present_status
    task.is_finished = updated
    task.save()
    return redirect('todolist:show_todolist')

def show_todolist_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def login_ajax(request):
    if request.user:
        logout_user(request)

    if request.method == 'POST':
        # Autentikasikan username dan password
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist_ajax")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')

    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='/todolist/login-ajax')
def show_todolist_ajax(request):
    # Tampilkan task berdasarkan user yang sedang login
    logged_in_user = request.user
    tasks = Task.objects.filter(user = logged_in_user)
    context = {
        'todolist' : tasks,
        'user' : logged_in_user
    }
    return render(request, "todolist_ajax.html", context)

@login_required(login_url='/todolist/login-ajax')
@csrf_exempt
def add(request):
    if request.method == 'POST':
        current_user = request.user
        task_title = request.POST["judul"]
        task_description = request.POST["deskripsi"]

        new_task = Task(user = current_user, title = task_title, description = task_description)
        new_task.save()
        return HttpResponse("success")

@login_required(login_url='/todolist/login-ajax')
def update(request, task_id):
    task = Task.objects.get(pk = task_id)
    task.is_finished = not task.is_finished
    task.save()
    return HttpResponse("success")

@login_required(login_url='/todolist/login-ajax')
def delete(request, task_id):
    task = Task.objects.get(pk = task_id)
    task.delete()
    return HttpResponse("success")
