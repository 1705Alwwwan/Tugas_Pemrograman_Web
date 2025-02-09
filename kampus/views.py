from django.shortcuts import render, redirect
from .models import Mahasiswa
from .forms import MahasiswaForm

def home (request):
    mahasiswa = Mahasiswa.objects.all()
    context = {'AllMahasiswa':mahasiswa}
    return render (request, 'kampus/index.html', context)



def crete_mahasiswa (request):
    form  = MahasiswaForm()
    if request.method == 'POST':
        form = MahasiswaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        
    context = {'CreateMahasiswaForm':form}
    return render (request, 'kampus/create-mahasiswa.html', context)

def update_mahasiswa (request, pk):
    try:
        mahasiswa = Mahasiswa.objects.get(id=pk)
    except:
        return redirect('')
    
    form = MahasiswaForm(instance=mahasiswa)
    if request.method == "POST":
        form = MahasiswaForm(request.POST, instance=mahasiswa)
        if form.is_valid():
            form.save()
            return redirect('')
        
    context = {'UpdateMahasiswaForm':form}

    return render (request, 'kampus/update-mahasiswa.html', context)

def delete_mahasiswa (request, pk):
    try:
        mahasiswa = Mahasiswa.objects.get(id=pk)
    except:
        return redirect('')
    
    if request.method == "POST":
        mahasiswa.delete()
        return redirect('')
    
    return render (request, 'kampus/delete-mahasiswa.html')


