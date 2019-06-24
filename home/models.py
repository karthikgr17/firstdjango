from django.db import models
import uuid

# Create your models here.
class Book(models.Model):
    
    name=models.CharField(max_length=100,help_text='book name',null=True)
    book_author=models.CharField(max_length=100,help_text='book author',null=True)
    def __str__(self):
        return self.name+"-"+self.book_author

class Person(models.Model):
    first_name = models.CharField(max_length=30,help_text='first_name',null=True)
    last_name = models.CharField(max_length=30,help_text='last_name',null=True)

    def __str__(self):
        return self.first_name+" "+self.last_name


#class Musician(models.Model):
    #first_name = models.CharField(max_length=50,help_text='first_name',null=True)
    #last_name = models.CharField(max_length=50,help_text='last_name',null=True)
 #   instrument = models.CharField(max_length=100,help_text='instrument',null=True)

  #  def __str__(self):
        #return self.first_name
        #return self.last_name
   #     return self.instrument

#class Album(models.Model):
 #   artist = models.ForeignKey(Musician, on_delete=models.CASCADE,max_length=40,help_text='artist',null=True)
    #name = models.CharField(max_length=100)
  #  release_date = models.DateField(max_length=20,help_text='release_date',null=True)
    #num_stars = models.IntegerField()

   # def __str__(self):
    #    return self.artist
     #   return self.release_date

