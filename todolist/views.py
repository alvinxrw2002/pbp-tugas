import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from todolist.models import Task
from todolist.forms import TaskForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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