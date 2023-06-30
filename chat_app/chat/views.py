from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse

messages = []

def index(request):
    return render(request, 'chat/index.html', {'messages': messages})

def send_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        messages.append(message)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})
