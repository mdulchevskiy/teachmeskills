from django.shortcuts import render, redirect
from todo_list.forms import TodoForm
from todo_list.models import TodoList


def home_page(request):
    activities = TodoList.objects.filter().order_by('order')
    return render(request, 'home_page.html', {'activities': activities})


def filter_activity(request):
    activities = TodoList.objects.filter().order_by('order')
    filter_parameter = int(request.POST.get('choice'))
    if filter_parameter:
        filtered_activities = TodoList.objects.filter(priority=filter_parameter)
        return render(request, 'home_page.html', {'activities': activities, 'filtered_activities': filtered_activities})
    return redirect('home_page')


def add_activity(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            TodoList.objects.create(**data)
            activity = TodoList.objects.filter(activity=data['activity']).first()
            TodoList.objects.filter(activity=data['activity']).update(order=activity.id)
            return redirect('home_page')
        else:
            error_list = form.errors
            form = form_with_initial(request)
            return render(request, 'add_activity.html', {'form': form, 'errors': error_list})
    return render(request, 'add_activity.html', {'form': TodoForm()})


def delete_activity(request, activity_id):
    TodoList.objects.filter(id=activity_id).delete()
    return redirect('home_page')


def edit_activity(request, activity_id):
    activity = TodoList.objects.get(id=activity_id)
    data_dict = {
        'activity': activity.activity,
        'priority': activity.priority,
    }
    form = TodoForm(initial=data_dict)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            TodoList.objects.filter(id=activity_id).update(**data)
            return redirect('home_page')
        else:
            error_list = form.errors
            form = form_with_initial(request)
            return render(request, 'edit_activity.html', {'form': form, 'errors': error_list, 'activity_id': activity_id})
    return render(request, 'edit_activity.html', {'form': form, 'activity_id': activity_id})


def edit_status(request, activity_id):
    status = request.POST.get('status')
    if status:
        status = int(status)
    else:
        status = 0
    TodoList.objects.filter(id=activity_id).update(status=status)
    return redirect('home_page')


def up_activity(request, activity_id):
    activities = TodoList.objects.filter()
    order_list = []
    for activity in activities:
        order_list.append(activity.order)
    order_list.sort()
    activity = TodoList.objects.get(id=activity_id)
    activity_order = activity.order
    activity_index = order_list.index(activity_order)
    if activity_index - 1 >= 0:
        other_activity_order = order_list[activity_index - 1]
        other_activity = TodoList.objects.get(order=other_activity_order)
        TodoList.objects.filter(id=activity.id).update(order=other_activity_order)
        TodoList.objects.filter(id=other_activity.id).update(order=activity_order)
        return redirect('home_page')
    return redirect('home_page')


def down_activity(request, activity_id):
    activities = TodoList.objects.filter()
    order_list = []
    for activity in activities:
        order_list.append(activity.order)
    order_list.sort()
    activity = TodoList.objects.get(id=activity_id)
    activity_order = activity.order
    activity_index = order_list.index(activity_order)
    if activity_index + 1 < len(order_list):
        other_activity_order = order_list[activity_index + 1]
        other_activity = TodoList.objects.get(order=other_activity_order)
        TodoList.objects.filter(id=activity.id).update(order=other_activity_order)
        TodoList.objects.filter(id=other_activity.id).update(order=activity_order)
        return redirect('home_page')
    return redirect('home_page')


def form_with_initial(request):
    data_dict = {
        'activity': request.POST.get('activity'),
        'priority': request.POST.get('priority'),
    }
    form = TodoForm(initial=data_dict)
    return form
