from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

##django rest framework를 이용한 API를 위한 패키지들 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Question
from .serializers import QuestionSerializer

import datetime


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list
    }

    #return HttpResponse(template.render(context, request))
    return HttpResponse(template.render(context))
    

"""
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = { "latest_question_list": latest_question_list}

    return render(request, "polls/index.html", context)
"""





def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(requeset, question_id):
    response = "You're looking at results of quesiont %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


##REST API이용해서 react랑 연동해보기 예제 코드 
def api_get(request):
    
    message = request.GET.get('abc')
    ret_val = len(message)
    return HttpResponse(ret_val)





##django REST framework이용해서 만든 api이용해서 react랑 연동해보기 예제 코드 
@api_view(['GET', 'POST'])
def drf_api(request):
    
    ##들어온 API요청이 GET이라면
    if request.method == 'GET':
        question_id = request.GET.get('question_id')

        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            res = {
                '204_no_content': f"{question_id}에 해당하는 Question이 존재하지 않습니다."
            }
            return Response(res, status=status.HTTP_204_NO_CONTENT)
        
        serializer = QuestionSerializer(question)
        res = {
            'question_text': serializer.data['question_text'],
            'question_text_length': len(serializer.data['question_text']),
        }
        return Response(res, status=200)
    
    
    ##들어온 API요청이 POST라면
    if request.method == 'POST':
        data = request.data     #body의 원시데이터를 가져온다. 
        data['pub_date'] = datetime.datetime.now()
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid(raise_exception=True):   #유효성 검사
            serializer.save()  #DB에 저장.
            return Response(status=status.HTTP_201_CREATED)