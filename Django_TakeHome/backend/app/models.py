from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key= True)
    name= models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    id = models.AutoField(primary_key= True)
    name= models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key= True)
    name= models.CharField(max_length=150)
    description= models.TextField(blank=True)
    category= models.ForeignKey(Category, on_delete=models.PROTECT)
    tags= models.ManyToManyField(Tag)

    def __str__(self):
        return self.name



