from django.shortcuts import render

from django.http import HttpResponse
# post k import kore dilamam
from .models import Post  

# data gulo list akare dekhabe
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Post k class er maddhome atkano
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#content =[
    #{
       # 'title' : 'Blog Post 1',
       # 'author' : 'Author',
       # 'date' : '25 December 2020',
       # 'text' : 'The first blog in our project'
    #},
    #{
       # 'title' : 'Blog Post 2',
        #'author' : 'Author',
        #'date' : '27 December 2020',
        #'text' : 'The second blog in our project'
   # }
#]

# Create your views here.
def home(request):
    context = ws.scrap()
    #context = {
        #'posts' : content
        #'posts' : Post.objects.all()
        
    #}
    
    return render(request, 'blog/home.html', context)
                        
def about(request):
    '''return HttpResponse('<h1>Hello From About</h1>')'''
    return render(request, 'blog/about.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date'] # assending order sorting date, desending order ['-date']
    
class PostDetailView(DetailView):
    model = Post

# CREATE Post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title' , 'text']
    
    #auto userinfo nibe post korle
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
# Update Post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'text']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
    
    # Onno ta jeno update na kori
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False
        
# Delete Post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'      # delete korar pore kothay jabe shei jonno
    
    # Onno ta jeno Delete na kori
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False
    
    
#<app>/<model>_<view>.html