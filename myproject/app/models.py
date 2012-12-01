from django.db import models

# Create your models here.
class Shelf(models.Model):
    label = models.CharField(max_length=50)
    
class NoteBook(models.Model):

    """
         As the name specifies. A noteBook can have any number of pages.
 
    """
    title = models.CharField(max_length=50)
    shelf = models.ForeignKey('shelf')

class Chapter(models.Model):
    title = models.CharField(max_length=40)
    book = models.ForeignKey('notebook')
    date = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    

   

     
