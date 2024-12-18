from .forms import TCCForm
from django.contrib.auth.decorators import login_required
from .models import TCC
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required 
def criar_tcc(request):
    if request.method == 'POST':
        form = TCCForm(request.POST, request.FILES)
        
        if form.is_valid():
            print(form.cleaned_data)
            tcc = form.save(commit=False)
            tcc.orientador = request.user.orientador 
            tcc.save()
            return redirect('dashboard')  
        else:
            print(form.errors)
    else:
        form = TCCForm()
        
    return render(request, 'app_forms/criar_tcc.html', {'form': form})

@login_required
def dashboard(request):
    if hasattr(request.user, 'orientador'):  
        tccs = TCC.objects.filter(orientador=request.user.orientador)
        print(tccs.query)
    else:
        tccs = TCC.objects.filter(autores__user=request.user)
    return render(request, 'orientador/pag_mentor.html', {'tccs': tccs})

def tcc_details(request, tcc_id):
    tcc = get_object_or_404(TCC, id=tcc_id)
    tasks = tcc.tasks.all()  # Pegando as tasks associadas ao TCC
    return render(request, 'app_forms/tcc_details.html', {'tcc': tcc, 'tasks': tasks})

@login_required
def add_task(request, tcc_id):
    # Pega o TCC com base no ID, como no exemplo da view de TCC
    tcc = get_object_or_404(TCC, id=tcc_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # Aqui associamos a task ao tcc
            task = form.save(commit=False)
            task.tcc = tcc  # Associa o TCC ao criar a task
            task.save()
            return redirect('tcc_view', tcc_id=tcc.id)  # Redireciona para a página de detalhes do TCC
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form, 'tcc': tcc})


def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Para suportar AJAX
        return JsonResponse({'status': 'success'})
    return redirect('tcc_details', tcc_id=request.GET.get('tcc_id'))

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Para suportar AJAX
        return JsonResponse({'status': 'success'})
    return redirect('tcc_details', tcc_id=request.GET.get('tcc_id'))
