
from django.shortcuts import render, redirect, get_object_or_404
from tasks.forms import ListForm
from tasks.models import List

# CREATE and LIST
def task_list(request):
    # Retrieves all List objects from the database
    tasks = List.objects.all()
    # Creates an empty form for a new task
    form = ListForm()
    # If the request is a POST, it means a form submission occurred. The view:
    if request.method == "POST":
        # Retrieves the data submitted in ListForm(request.POST)
        form = ListForm(request.POST)
        # Validates and saves the form data if valid
        if form.is_valid():
            form.save()
            # Redirects to 'task_list' to reload the updated list
            return redirect('task_list')
    # Renders the task list and form in the 'task_list.html' template
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})

# CREATE (on a separate page)
def create_task(request):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = ListForm()
    return render(request, 'tasks/task_form.html', {'form': form})

# UPDATE
def task_update(request, pk):
    # Fetches the specific task (List object) to update
    task = get_object_or_404(List, pk=pk)
    if request.method == "POST":
        form = ListForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = ListForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

# DELETE
def task_delete(request, pk):
    # Fetches the specific task (List object) to delete
    task = get_object_or_404(List, pk=pk)
    task.delete()
    return redirect('task_list')
