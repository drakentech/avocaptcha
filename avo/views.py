from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
import threading

import json

API_KEY = "your-key-here"

@csrf_exempt
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def contacts(request):
    openai.api_key = API_KEY
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "give me 4 objects in one line!"}
        ]
    )

    txt_response = res.choices[0].message["content"]
    request.session['img_desc'] = txt_response
    print(txt_response+'\n')
    img_response = openai.Image.create(
            prompt=txt_response+" blend",
            n=1,
            size="256x256"
    )
    url = img_response['data'][0]['url']
    print(url)
    resp = False
    return render(request, 'contacts.html', {'url': url})

@csrf_exempt
def pricing(request):
    return render(request, 'pricing.html')

@csrf_exempt
def features(request):
    return render(request, 'features.html')

@csrf_exempt
def integrations(request):
    return render(request, 'integrations.html')
    
@csrf_exempt
def ajax(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        text = request.POST.get('text')
        print(text)
        openai.api_key = API_KEY
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Please tell me the difference between these two strings, please consider synonims and spelling errors. Please return the similarity in a 0-100% value in JSON format. Please return only this similarity value, and no other. {text} {request.session['img_desc']}"}
            ]
        )
        txt_response = res.choices[0].message["content"]
        txt_response = txt_response.split('}')[0]+"}"
        chat = Chat.objects.create(
            text = text,
            gpt = txt_response
        )
        
        json_dict = json.loads(txt_response)
        print("similarity: " + str(json_dict['similarity']))
        if int(json_dict['similarity']) >= 50:
            return JsonResponse({'data': True })
        else:
            return JsonResponse({'data': False })
    return JsonResponse({})
