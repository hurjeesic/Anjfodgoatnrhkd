from django.db import models
from django.utils import timezone

# Create your models here.
class Example(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    sentence = models.CharField(max_length=100)
    boolean_answer = models.PositiveIntegerField(default=0)
    boolean_num = models.PositiveIntegerField(default=0)
    boolean_ratio = models.FloatField(default=0)
    short_answer = models.PositiveIntegerField(default=0)
    short_num = models.PositiveIntegerField(default=0)
    short_ratio = models.FloatField(default=0)
    published_date = models.DateTimeField(default=timezone.now)

    def edit_problem(self):
        self.boolean_answer = 0
        self.boolean_num = 0
        self.short_answer = 0
        self.short_num = 0
        self.published_date = timezone.now()
        self.save()

    def right_problem(self, type, answer):
        if type == 'boolean':
            if answer: self.boolean_answer += 1
            self.boolean_num += 1
        elif type == 'short':
            if answer: self.short_answer += 1
            self.short_num += 1

        right_ratio(type)
        self.save()

    def right_ratio(self, type):
        if type == 'boolean':
            boolean_ratio = self.boolean_answer / self.boolean_num
        elif type == 'short':
            short_ratio = self.short_answer / self.short_num

    def __str__(self):
        return self.sentence

class Dialect(models.Model):
    standard = models.CharField(max_length=255)
    jeju = models.CharField(max_length=255)

    def regist_word(self, standard, jeju):
        self.standard = standard
        self.jeju = jeju
        self.save()
