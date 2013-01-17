from django.db import models
from django.contrib import admin	

# Create your models here.
class Shelf(models.Model):
    label = models.CharField(max_length=50)
    
    def __unicode__(self):
        return u'%s' % (self.label) 
class NoteBook(models.Model):

    """
         As the name specifies. A noteBook can have any number of pages.
 
    """
    title = models.CharField(max_length=50)
    shelf = models.ForeignKey('Shelf')
    
    def __unicode__(self):
        return u'%s    %s' % (self.title, self.shelf)
class Chapter(models.Model):
    title = models.CharField(max_length=40)
    book = models.ForeignKey('Notebook')
    date = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    text = models.TextField()   
    
    def __unicode__(self):
        return u'%s %s' % (self.title, self.book)
  

class NoteBookAdmin(admin.ModelAdmin):
    pass
class ChapterAdmin(admin.ModelAdmin):
    pass

class ShelfAdmin(admin.ModelAdmin):
    pass


admin.site.register(Shelf, ShelfAdmin) 
admin.site.register(NoteBook, NoteBookAdmin)
admin.site.register(Chapter, ChapterAdmin)

