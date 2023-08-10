from django.conf import settings
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    def __str__(self) -> str:
        return self.title


class Question(models.Model):
    PUBLISHED = 'published'
    DRIFT = 'draft'
    STATUS_CHOICES = (
        (PUBLISHED, 'Published'),
        (DRIFT, 'Draft')
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='questions')
    text = models.CharField(max_length=255)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    comment = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default=DRIFT)

    def __str__(self) -> str:
        return self.text[:50]


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='choices')
    label = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.label


class Respondant(models.Model):
    STUDENT = 'STU'
    EMPLOYEE = 'EMP'
    FARMER = 'FAM'
    MERCHANT = 'MER'
    UNEMPLOY = 'UNE'
    OCCUPATION_STATUS_CHOICES = [
        (STUDENT, 'Student'),
        (EMPLOYEE, 'Employee'),
        (FARMER, 'Farmer'),
        (MERCHANT, 'Business person'),
        (UNEMPLOY, 'Unemploy')
    ]
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, primary_key=True)
    birth_date = models.DateField()
    occupation = models.CharField(
        max_length=3, choices=OCCUPATION_STATUS_CHOICES, default=STUDENT)

    def __str__(self) -> str:
        return self.user.username


class Address(models.Model):
    respondant = models.OneToOneField(
        Respondant, on_delete=models.CASCADE, primary_key=True)
    country = models.CharField(max_length=200)
    county = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    community = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Response(models.Model):
    respondant = models.ForeignKey(
        Respondant, on_delete=models.PROTECT, related_name='responses')
    question = models.ForeignKey(
        Question, on_delete=models.PROTECT, related_name='responses')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['question', 'respondant']]
        
    def __str__(self) -> str:
        return self.date.strftime('%a %d %b %Y, %I:%M%p')


class SelectedChoice(models.Model):
    response = models.ForeignKey(
        Response, on_delete=models.PROTECT, related_name='selectedchoices')
    choice = models.ForeignKey(Choice, on_delete=models.PROTECT)
