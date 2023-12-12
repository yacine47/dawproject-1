from django.contrib.auth.models import User
from django.db import models


class Patient(models.Model):
    idUser = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)
    levelOfAddiction = models.DecimalField(max_digits=4, decimal_places=2)
    averageHoursOfGammingPerWeek = models.DecimalField(max_digits=5, decimal_places=2)
    averageHoursOfGammingPerMounth = models.DecimalField(max_digits=5, decimal_places=2)
    insomniaScore = models.DecimalField(max_digits=4, decimal_places=2)
    excessiveSleepinessScore = models.DecimalField(max_digits=4, decimal_places=2)
    anxietyScore = models.DecimalField(max_digits=4, decimal_places=2)
    depressionScore = models.DecimalField(max_digits=4, decimal_places=2)


class Doctor(models.Model):
    idUser = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)
    scheduledTherapySessions = models.IntegerField(null=False)


class Questionnaire(models.Model):
    id_Patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=False)
    dateOfTheQuestionnaire = models.DateTimeField()


class ResponsesQuestionnaire(models.Model):
    id_Questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, null=True, blank=False)
    dateOfResponse = models.DateTimeField()
    score = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=False)


class Question(models.Model):
    questionText = models.TextField()
    questionType = models.CharField(max_length=45)


class Option(models.Model):
    id_Question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=False)
    point = models.DecimalField(max_digits=3, decimal_places=2)


class ResponsesQuestion(models.Model):
    id_Reponse_Questionnaire = models.ForeignKey(ResponsesQuestionnaire, on_delete=models.CASCADE, null=True,
                                                 blank=False)
    id_Option = models.ForeignKey(Option, on_delete=models.CASCADE, null=True, blank=False)
