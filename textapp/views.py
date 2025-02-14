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
from .data_process import *
import datetime

# View webpage definition, may use JS to call API endpoint
# Create your views here.
def main(request):
    # Sample page for application
    content = "<html><body><h1>Welcome to TextAPP!</h1></body></html>"
    return HttpResponse(content)

def sample(request):
    return render(request, 'sample.html')

def home(request):
    home_data = {'home_data': ''}
    return render(request, 'home.html', home_data
    )

def test(request):
    return render(request, 'test.html')

# Text Task webpage
def base(request):
    return render(request, 'base.html')

def textSummarize(request):
    return render(request, 'text_summarize.html')

def textTranslate(request):
    return render(request, 'text_translate.html')

def textKeywordExtraction(request):
    return render(request, 'text_ner.html')



# API endpoint for JS script call
@csrf_exempt # Important if you're not using Django's form submission
def process_text(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get('text')

            print("Full body: ", request.META)
            # Get the client's IP address
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Use the first IP in the list
            else:
                ip = request.META.get('REMOTE_ADDR')

            print(f"Client IP Address: {ip}")  # Log the IP address

            # Perform your text processing logic here (e.g., summarization)
            processed_text = text_processing(text) # Example: Convert to uppercase

            print("Data: ", data, ' text: ', text)
            print("Processed_test: ", processed_text)

            format_data = {'originText':text, 'inferenceText':str(processed_text), 'task_type':'Normal', 'user_ip': ip}
            print("Format data: ", format_data)

            # Store inference and source to DB
            serializer = TextInferenceSerializer(data=format_data)
            if serializer.is_valid(raise_exception=True):
                print("Input data valid! Deserialized to DB")
                serializer.save()
            else:
                print("Input data serialization invalid!")

            return JsonResponse({'result': processed_text})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)



@csrf_exempt # Important if you're not using Django's form submission
def nlp_text_summarize(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get('text')

            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Use the first IP in the list
            else:
                ip = request.META.get('REMOTE_ADDR')

            # Perform your text processing logic here (e.g., summarization)
            processed_text = text_summarizing(text) # Example: Convert to uppercase

            print("Data: ", data, ' text: ', text)
            print("Processed_test: ", processed_text)

            format_data = {'originText':text, 'inferenceText':str(processed_text), 'task_type':'Summarization', 'user_ip': ip}
            print("Format data: ", format_data)

            # Store inference and source to DB
            serializer = TextInferenceSerializer(data=format_data)
            if serializer.is_valid(raise_exception=True):
                print("Input data valid! Deserialized to DB")
                serializer.save()
            else:
                print("Input data serialization invalid!")

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
        

# Text translate function
@csrf_exempt # Important if you're not using Django's form submission
def nlp_text_translate(request):
    src_lang = 'eng_Latn'
    target_lang = 'zho_Hans'
    model = 'facebook/nllb-200-distilled-600M'

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get('text')

            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Use the first IP in the list
            else:
                ip = request.META.get('REMOTE_ADDR')

            # Perform your text processing logic here (e.g., summarization)
            processed_text = text_translate(text,
                                            checkpoint=model,
                                            src_lang=src_lang, 
                                            target_lang=target_lang) # Example: Convert to uppercase

            print("Data: ", data, ' text: ', text)
            print("Processed_test: ", processed_text)

            format_data = {'originText':text, 'inferenceText':str(processed_text), 'task_type':'Translation', 'user_ip':ip}
            print("Format data: ", format_data)

            # Store inference and source to DB
            serializer = TextInferenceSerializer(data=format_data)
            if serializer.is_valid(raise_exception=True):
                print("Input data valid! Deserialized to DB")
                serializer.save()
            else:
                print("Input data serialization invalid!")

            return JsonResponse({'result': processed_text})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)