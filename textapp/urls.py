from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'textapp'

# Map url address to each view function

urlpatterns = [
    path('main/', views.main), # Argument: path address, view function (here is home function)
    path('base/', views.base),
    path('textSummarize/', views.textSummarize),
    path('textTranslate/', views.textTranslate),
    path('textKeywordExtract/', views.textKeywordExtraction),
    path('sample/', views.sample),
    path('processText/', views.process_text),
    path('processTextSummarize/', views.nlp_text_summarize),
    path('processTextTranslate/', views.nlp_text_translate),
    path('test/', views.test),
]


