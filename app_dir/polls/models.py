from django.db import models
from django.utils.translation import ugettext_lazy as _
from simple_history.models import HistoricalRecords

# Create your models here.
class Choice(models.Model):
    question = models.TextField(max_length=500)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    history = HistoricalRecords()

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = _('Choice')
