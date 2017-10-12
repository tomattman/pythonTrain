from django.db import models

class Topic(models.Model):
    """User's topic"""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.text

class Entry(models.Model):
    """Info by topic"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + ("..." if len(self.text) > 50 else "")
