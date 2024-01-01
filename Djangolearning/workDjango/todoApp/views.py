from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from django.views.decorators.http import require_http_methods


#@csrf_exempt
# @require_http_methods(["POST"])  # This decorator is used to exempt CSRF protection for simplicity. Use a more secure approach in production.
#@require_POST
def todo(request):
    return render(request, 'index.html')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def js(request):
    if request.method == 'POST':
        try:
            # Load JSON data from the request body
            data = json.loads(request.body.decode('utf-8'))
            task_text = data.get('taskText', '')

            # Perform any additional processing with task_text
            # ...
            print("task data :", task_text)

            # Return a JsonResponse if needed
            return JsonResponse({'message in js func': task_text})
        except json.JSONDecodeError as e:
            return JsonResponse({'error kya ye js karne pe aa raha hai': 'Invalid JSON data'}, status=400)
