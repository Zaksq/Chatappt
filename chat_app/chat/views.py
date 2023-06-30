from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

messages = []

def index(request):
    return render(request, 'chat/index.html', {'messages': messages})

def send_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        messages.append(message)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

@csrf_exempt
def change_background(request):
    if request.method == 'POST':
        # Получаем текущий режим фона из сессии или устанавливаем значение по умолчанию
        background_mode = request.session.get('background_mode', 'light')

        # Изменяем режим фона
        if background_mode == 'light':
            background_mode = 'dark'
        else:
            background_mode = 'light'

        # Сохраняем новый режим фона в сессии
        request.session['background_mode'] = background_mode

        # Возвращаем JSON-ответ для обновления фона на клиентской стороне
        return JsonResponse({'background_mode': background_mode})

    # Если запрос не POST, возвращаем ошибку или перенаправляем на другую страницу
    return JsonResponse({'error': 'Invalid request'})