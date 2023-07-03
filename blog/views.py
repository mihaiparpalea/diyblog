from django.shortcuts import render
from .models import Blog, User
from django.views import generic
import operator
import datetime

def index(request):

	# Generate counts of some of the main objects
	num_blogs = Blog.objects.all().count()

	context = {
		'num_blogs': num_blogs,
	}

	# Render the HTML template index.html with the data in the context variable
	return render(request, 'index.html', context=context)

class BlogListView(generic.ListView):
	model = Blog
	ordering = ['-date']
	paginate_by = 5
	
class BlogDetailView(generic.DetailView):
	model = Blog

class BloggerDetailView(generic.DetailView):
	model = User
	users = User.objects
	blogs = sorted(users.blog_set.all, key=operator.attrgetter('date'))

	context = {
		'blogs': blogs,
	}