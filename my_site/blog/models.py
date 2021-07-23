from django.db import models

from django.core.validators import MinLengthValidator
# Create your models here.

class Tag(models.Model):
    caption=models.CharField(max_length=100)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email_address=models.EmailField()

    def __str__(self):
        full_name='{} {}'.format(self.first_name,self.last_name)
        return full_name


class Post(models.Model):
    title= models.CharField(max_length=300)
    excerpt=models.CharField(max_length=400)
    # image_name=models.CharField(max_length=100)
    image_name=models.ImageField(upload_to='image')
    date= models.DateField(auto_now=True)
    slug=models.SlugField(unique=True,db_index=True)
    content=models.TextField(validators=[MinLengthValidator(10)])

    tags=models.ManyToManyField(Tag)
    author= models.ForeignKey(Author,on_delete=models.SET_NULL,null=True,related_name='posts')
