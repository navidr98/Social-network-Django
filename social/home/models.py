from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# related_name for backward move in models
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #ordering models in views by crerated time and slug
    class Meta:
        ordering = ('created', 'slug' )

    #show models by slug and updated time
    def __str__(self):
        return f'{self.slug} - {self.updated}'

    #set html url for cleaning code
    def get_absolute_url(self):
        return reverse(('home:post_detail'), args=(self.pk,self.slug))

