from django.db import models

# Create your models here.
class SearchResult(models.Model):
  link = models.URLField(help_text="Link to the website")
  title = models.CharField(max_length=500, help_text="A title for this result.")
  short_description = models.CharField(max_length=500, help_text="A short summary of this.")
  keyword1 = models.CharField(max_length=500, help_text="Keywords which someone would search and it would show your result. NO SPACES! E.g./ Cakerecipes")
  keyword2 = models.CharField(blank=True,max_length=500, help_text="Keywords which someone would search and it would show your result. NO SPACES! E.g./ Cakerecipes")
  keyword3 = models.CharField(blank=True,max_length=500, help_text="Keywords which someone would search and it would show your result. NO SPACES! E.g./ Cakerecipes")
  keyword4 = models.CharField(blank=True, max_length=500, help_text="Keywords which someone would search and it would show your result. NO SPACES! E.g./ Cakerecipes")
  keyword5 = models.CharField(blank=True,max_length=500, help_text="Keywords which someone would search and it would show your result. NO SPACES! E.g./ Cakerecipes")
  keyword6 = models.CharField(blank=True,max_length=500, help_text="Keywords which someone would search and it would show your result. NO SPACES! E.g./ Cakerecipes")
  keyword7 = models.CharField(blank=True,max_length=500, help_text="Keywords which someone would search and it would show your result. NO SPACES! E.g./ Cakerecipes")
  keyword8 = models.CharField(blank=True,max_length=500, help_text="Keywords which someone would search and it would show your result. NO SPACES! E.g./ Cakerecipes")
  keyword9 = models.CharField(blank=True,max_length=500, help_text="Keywords which someone would search and it would show your result. NO SPACES! E.g./ Cakerecipes")