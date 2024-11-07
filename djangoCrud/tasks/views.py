from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# In-memory list to store tasks
task_list = []

def view_tasks(request):
    """View all tasks"""
    return JsonResponse({"tasks": task_list})

@csrf_exempt
def add_task(request):
    """Add a new task"""
    if request.method == 'POST':
        data = json.loads(request.body)
        task_description = data.get("description")
        if task_description:
            task_list.append(task_description)
            return JsonResponse({"message": "Task added", "tasks": task_list})
        else:
            return JsonResponse({"error": "No task description provided"}, status=400)

@csrf_exempt
def delete_task(request, task_id):
    """Delete a task by index"""
    try:
        task_id = int(task_id)
        task_list.pop(task_id)
        return JsonResponse({"message": "Task deleted", "tasks": task_list})
    except (IndexError, ValueError):
        return JsonResponse({"error": "Invalid task index"}, status=400)
