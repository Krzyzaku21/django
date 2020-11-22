from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model): #obiekt Post metaklasy Django
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #models.ForeignKey odnośnik do innego modelu
    title = models.CharField(max_length=200) #models.CharField określona liczba znaków
    text = models.TextField() #models.TextField obiekt tekstowy bez ograniczeń
    created_date = models.DateTimeField(default=timezone.now) #models.DateTimeField obiekt daty
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title