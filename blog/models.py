from django.db import models
from django.conf import settings
from django.utils import timezone
# Models are like the special object
class Post(models.Model): #Post is the name of the model and models.Model tell the django that post is the model & it should be saved in the db.
    #setting the attribute
    #we are only setting variables here not assigning values
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
