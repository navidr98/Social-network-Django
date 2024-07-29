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

    def likes_count(self):
        return self.pvotes.count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ucomments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='pcomments')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='rcomments', blank=True, null=True)
    is_reply = models.BooleanField(default=False)
    body = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.body[:30]}'


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uvotes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='pvotes')

    def __str__(self):
        return f'{self.user} liked {self.post.slug}'









