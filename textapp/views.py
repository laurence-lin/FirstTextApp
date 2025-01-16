from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError, Http404, JsonResponse
from django.shortcuts import reverse, render
from django.template import loader
from rest_framework.response import Response 
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, throttle_classes
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
import json
from django.views.decorators.csrf import csrf_exempt
from .models import TextInference
from .serializers import TextInferenceSerializer

# Create your views here.
def main(request):
    # Sample page for application
    content = "<html><body><h1>Welcome to TextAPP!</h1></body></html>"
    return HttpResponse(content)

def home(request):
    home_data = {'home_data': ''}
    return render(request, 'home.html', home_data
    )

def base(request):
    return render(request, 'base.html')

def sample(request):
    return render(request, 'sample.html')

@csrf_exempt # Important if you're not using Django's form submission
def process_text(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get('text')
            # Perform your text processing logic here (e.g., summarization)
            processed_text = f"{text.upper()}" # Example: Convert to uppercase

            # Store inference and source to DB
            serializer = TextInferenceSerializer()

            return JsonResponse({'result': processed_text})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


class TextInferenceView(generics.ListCreateAPIView):

    queryset = TextInference.objects.all()
    serializer_class = TextInferenceSerializer # Store inference and source to DB

    def post(self, request):
        try:
            data = json.loads(request.body)
            text = data.get('text')
            # Perform your text processing logic here (e.g., summarization)
            processed_text = f"{text.upper()}" # Example: Convert to uppercase

            

            return JsonResponse({'result': processed_text})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)