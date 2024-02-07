from django.shortcuts import render

# Create your views here.
# myapp/views.py
# from django.http import JsonResponse
from django.http import JsonResponse, HttpResponse

def submit_url(request):
    print("Aman")
    if request.method == 'POST':
        url = request.POST.get('url')
        # Do something with the URL (e.g., save it to a database, process it, etc.)
        print('Received URL:', url)
        # return JsonResponse({'message': 'URL received successfully'})
    elif request.method == 'OPTIONS':
        # Handle preflight OPTIONS request
        # response = JsonResponse({'message': 'OPTIONS request handled successfully'})
        # url = request.OPTIONS.get('url')
        custom_header_value = request.headers.get('Custom-Header')
        print('Custom Header Value:', custom_header_value)
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'  # Set appropriate CORS headers
        response['Access-Control-Allow-Methods'] = ['OPTIONS','POST'] # Allow only POST method
        response['Access-Control-Allow-Headers'] = ['Content-Type','X-CSRFToken','Custom-Header']  # Allow only Content-Type header
        return response
    else:
        response = JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
        response['Access-Control-Allow-Origin'] = '*'  # Set appropriate CORS headers
        return response
