import datetime

from django.db import models
from django.utils import timezone




# Create your models here.



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) #datetime.timedelta(days=1)는 오늘로부터 하루 뒤 날짜를 계산하는데 이용된다. 
"""
    def __str__(self):
        return self.question_text 
""" 
    




class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
##ForeignKey(to, **options) // 이때 to는 어떤 table을 참조할지 즉 어떤 table(혹은 model)의 pk(primary key)를 가질지를 결정해 준다. 
##ForeingKey included in Choice class DJango each Choice is related to a single Question 
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

##def __str__(self)는 python 자체 클래스 내장 모듈이다. 
##해당 모듈은 객체 자체를 출력할때 문자열을 리턴하도록 한다.
##공홈 :  객체의 표현이 Django의 자동 생성된 관리자 전체에서 사용되기 때문에 모델에 __str__() 메서드를 추가하는 것이 중요합니다.
##라고 공홈에서 설명하는데 사실 왜 중요한지 모르겠음 ;;; 