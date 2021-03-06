from django.db import models

# Create your models here.

class Category(models.TextChoices):
	TECH = 'TC', 'Tecnologia'
	CR = 'CR', 'Curiosidades'
	GR = 'GR', 'Geral'

class Post(models.Model):
	title = models.CharField(max_length=200)
	sub_title = models.CharField(max_length=200)
	content = models.TextField()
	categories = models.CharField(
		max_length=2,
		choices=Category.choices,
		default=Category.GR,	
	)
	deleted = models.BooleanField(default=False)
	images = models.ImageField(upload_to='posts', null=True, blank=True)


	def __str__(self):
		return self.title

	def full_name(self):
		return self.title + self.sub_title

	def get_category_label(self):
		return self.get_categories_display()

	full_name.admin_order_field = 'title'