from django.db import models

# Create your models here.

class Answer(models.Model):
    answer_title = models.CharField(max_length=50)
    answer_content = models.CharField(max_length=500)
    answer_id = models.CharField(primary_key=True, max_length=20)  # The composite primary key (answer_id, question_id) found, that is not supported. The first column is selected.
    answer_date = models.DateTimeField()
    question = models.ForeignKey('Question', models.DO_NOTHING)
    user_email = models.ForeignKey('User', models.DO_NOTHING, db_column='user_email')

    class Meta:
        managed = False
        db_table = 'answer'
        unique_together = (('answer_id', 'question'),)


class Question(models.Model):
    question_id = models.CharField(primary_key=True, max_length=20)   
    question_title = models.CharField(max_length=50)
    question_content = models.CharField(max_length=500)
    question_date = models.DateTimeField(auto_now_add=True)
    user_email = models.ForeignKey('User', models.DO_NOTHING, db_column='user_email')

    class Meta:
        managed = False
        db_table = 'question'


class User(models.Model):
    user_email = models.CharField(primary_key=True, max_length=30)    
    user_pwd = models.CharField(max_length=50)
    user_mobile = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'