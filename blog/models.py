from django.db import models

# Create your models here.
from django.db import models



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Author(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

    class Meta:
         verbose_name_plural = "Categories"



class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey('Author', on_delete= models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.body
