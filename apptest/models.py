from django.db import models
from django.utils import timezone
import datetime
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
# Create your models here.


class Poll(models.Model):
    question = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question

    def pub_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=1))
    pub_recently.boolean = True
    pub_recently.short_description = 'Published recently?'


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text



class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

