from django.db import models

# Create your models here.


class Poll(models.Model):
    topic = models.TextField()
    option1 = models.CharField(max_length=60)
    option2 = models.CharField(max_length=60)
    option3 = models.CharField(max_length=60)
    option1_count = models.IntegerField(default=0)
    option2_count = models.IntegerField(default=0)
    option3_count = models.IntegerField(default=0)

    def total(self):
        return self.option1_count + self.option2_count + self.option3_count

    def __str__(self):
        return self.topic
