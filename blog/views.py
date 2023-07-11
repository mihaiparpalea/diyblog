from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Blog, Author, Comment
from django.views import generic
from django.contrib.auth.models import Permission
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from blog.forms import AddComment
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

	def get_context_data(self, **kwargs):
		text = 'You must be logged in to comment.'
		if self.request.user.is_authenticated:
			text = 'Add comment.'
		context = super().get_context_data(**kwargs)                     
		context["text"] = text
		return context
	
class BloggerDetailView(generic.DetailView):
	model = Author

class AuthorListView(generic.ListView):
	model = Author
	def get_queryset(self):
		perm = Permission.objects.get(codename='add_blog')
		return Author.objects.filter(Q(groups__permissions=perm) | Q(user_permissions=perm)).distinct()

@login_required
def create_comment(request, pk):
	blog = get_object_or_404(Blog, pk=pk)
	new_comment = Comment()
	new_comment.blog = blog
	new_comment.date = datetime.date.today()
	new_comment.author = request.user

	if request.method == 'POST':
		form = AddComment(request.POST)
		if form.is_valid():
			new_comment.content = form.cleaned_data['content']
			new_comment.save()
			return HttpResponseRedirect(reverse('blog-detail', kwargs={'pk': blog.id}))
	else:
		form = AddComment(request.POST)

	context = {
		'form': form,
		'blog': blog,
	}

	return render(request, 'blog/comment_form.html', context)