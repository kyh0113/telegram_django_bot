from django.db import models

# 실제 DB에 어떤 테이블을 만들고 관리할 것인지
# Create your models here.

class DATA_WORKER(models.Model):
    WORKER_ID = models.CharField(max_length=50, primary_key=True)
    WORKER_NAME = models.CharField(max_length=50, null=True)

class DATA_IMAGE(models.Model):
    IMAGE_ID = models.AutoField(primary_key=True)
    IMAGE = models.CharField(max_length=200)
    DATE_WORK = models.DateField(auto_now=True)
    WORKER_ID = models.ForeignKey(DATA_WORKER, on_delete=models.SET_NULL, null=True)
    STATUS = models.CharField(max_length=1, null=True)


class QUESTION(models.Model):
    QUESTION_ID = models.AutoField(primary_key=True)
    QUESTION = models.CharField(max_length=1000)
    QUESTION_CNT = models.IntegerField()
    IMAGE_ID = models.ForeignKey(DATA_IMAGE, on_delete=models.PROTECT)
    STATUS = models.CharField(max_length=1, null=True)

class ANSWER(models.Model):
    ANSWER_ID = models.AutoField(primary_key=True)
    ANSWER = models.CharField(max_length=1000)
    QUESTION_ID = models.ForeignKey(QUESTION, on_delete=models.PROTECT)
    STATUS = models.CharField(max_length=1, null=True)


