from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from app_forms.models import TCC
from app_tcc_workspace.models import Message
from .forms import TCForm
from django.views.decorators.csrf import csrf_exempt
from app_tcc_workspace.models import Task
import json


@csrf_exempt
def update_task_status(request, tcc_id):  
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        task_id = data.get('task_id')
        completed = data.get('completed')

        
        task = get_object_or_404(Task, id=task_id)

        
        task.completed = completed
        task.save()

        
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required
def tcc_edit(request, tcc_id):
    
    
    tcc = get_object_or_404(TCC, id=tcc_id)
    if request.user != tcc.orientador.user:
        return redirect('tcc', tcc_id=tcc.id)
    
    if request.method == 'POST':
        form = TCForm(request.POST, request.FILES, instance=tcc)
        if form.is_valid():
            form.save()
            return redirect('tcc', tcc_id=tcc.id)
    else:
        form = TCForm(instance=tcc)

    return render(request, 'tcc_edit.html', {'form': form, 'tcc': tcc})


@login_required
def tcc_view(request, tcc_id):
    tcc = get_object_or_404(TCC, id=tcc_id)

    # Verifica se o método da requisição é POST (para mensagens)
    if request.method == "POST":
        # Verifica se é uma mensagem ou uma tarefa
        data = json.loads(request.body)
        
        if 'content' in data:  # Isso é para as mensagens de chat
            content = data.get('content', '')
            if content:
                # Cria a mensagem no banco de dados
                message = Message.objects.create(
                    user=request.user,
                    content=content,
                    tcc=tcc
                )

                # Retorna a resposta JSON com as informações da mensagem criada
                return JsonResponse({
                    'user': message.user.username,
                    'message': message.content,
                    'timestamp': message.timestamp.strftime('%H:%M')
                })
        
        elif 'title' in data:  # Isso é para a criação de tarefas
            title = data.get('title', '')
            description = data.get('description', '')
            due_date = data.get('due_date', None)

            # Cria a nova tarefa
            task = Task.objects.create(
                tcc=tcc,
                title=title,
                description=description,
                due_date=due_date
            )

            # Retorna a resposta JSON com as informações da tarefa criada
            return JsonResponse({
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'due_date': task.due_date,
                'completed': task.completed
            })

    # Caso a requisição não seja POST, apenas renderiza a página
    messages = Message.objects.filter(tcc=tcc).order_by('timestamp')
    tasks = Task.objects.filter(tcc=tcc).order_by('-created_at')  # Obtém as tarefas associadas ao TCC

    return render(request, 'tcc.html', {'tcc': tcc, 'messages': messages, 'tasks': tasks})

def create_task(request, tcc_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        description = data.get('description', '')
        due_date = data.get('due_date')

        # Criação da tarefa
        tcc = TCC.objects.get(id=tcc_id)
        task = Task.objects.create(
            tcc=tcc,
            title=title,
            description=description,
            due_date=due_date
        )

        return JsonResponse({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'due_date': task.due_date,
        })

    return JsonResponse({'error': 'Método não permitido'}, status=405)