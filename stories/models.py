from django.db import models
from django.contrib.auth.models import User
import datetime

class Story(models.Model):
    name = models.CharField(max_length = 50)
    last_update_date = models.DateTimeField()
    
    
    def __unicode__(self):
        return self.name
        
        
    @property
    def fulltext(self):
        frag_list = self.fragment_set.all()
        if frag_list:
            return " ".join([fragment.text for fragment in frag_list])
        else:
            return ""
    
    @property
    def brieftext(self):
        frag_list = self.fragment_set.all()
        if len(frag_list) > 5:
            return "%s..." % " ".join([fragment.text for fragment in frag_list])
        elif frag_list:
            return " ".join([fragment.text for fragment in frag_list[:4]])
        else:
            return ""
        
    def add_fragment(self, new_text, new_author, date=None):
        if not date:
            date = datetime.datetime.now()
            
        word_list = [
            word.strip()
            for word
            in new_text.strip().split(" ")
            if word.strip() != ""
        ]
        
        if len(word_list) > 3:
            raise ValueError("Fragments can only be three words long!")
            
        self.fragment_set.add(Fragment(
            text=" ".join(word_list),
            author=new_author,
            date=datetime.datetime.now(),
            story=self
        ))
        
        self.last_update_date = date
        self.save()
        
        
    class Meta:
        ordering = ("last_update_date", "name")
        verbose_name_plural = "Stories"

    
class Fragment(models.Model):
    text = models.CharField(max_length = 50)
    date = models.DateTimeField()
    author = models.ForeignKey(User)
    story = models.ForeignKey(Story)
    class Meta:
        ordering = ("date",)
