from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, Group
from datetime import date

class Author(User):

	class Meta:
		proxy = True

	def get_absolute_url(self):
		return reverse('blogger-detail', args=(self.pk,))
	
	def save(self, *args, **kwargs):
		creating = not self.pk
		super().save(*args, **kwargs)
		if creating:
			self.groups.add(Group.objects.get(name='blogger'))
	
class Biography(models.Model):
	content = models.TextField(max_length=1000, blank=True)
	blogger = models.OneToOneField(Author, on_delete=models.CASCADE)

	def __str__(self):
		return self.content

class Blog(models.Model):
	name = models.CharField(max_length=200, help_text='Enter name')
	author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
	content = models.TextField(help_text='Enter content')
	date = models.DateField(null=True, blank=True)

	class Meta:
		ordering = ['date']

	def get_absolute_url(self):
		return reverse('blog-detail', args=[str(self.id)])

	def __str__(self):
		return self.name

class Comment(models.Model):
	content = models.TextField(blank=False)
	date = models.DateField(null=True, blank=True)
	blog = models.ForeignKey('Blog', on_delete=models.DO_NOTHING, null=False)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

	class Meta:
		ordering = ['date']

	def get_absolute_url(self):
		return reverse('comment-detail', args=[str(self.id)])

	def __str__(self):
		return self.content