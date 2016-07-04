from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import generic
from django.contrib.auth import mixins

from content.forms import PhotoPostForm
from content.models import PhotoPost


def home_view(request):
    posts = PhotoPost.objects.all()


    return render(request, 'home.html', {"posts": posts})

def profile_view(request):
    return render(request, 'profile.html')

class UserView(mixins.LoginRequiredMixin, generic.DetailView):
    """
    Page for user
    """
    model = User
    template_name = "user.html"
    context_object_name = "author"

    def get_context_data(self, **kwargs):
        kwargs['media'] = PhotoPost.objects.filter(author=self.object)
        return super(UserView, self).get_context_data(**kwargs)


class PostView(mixins.LoginRequiredMixin, generic.DetailView):
    """
    Page for media
    """
    model = PhotoPost
    template_name = "post.html"
    context_object_name = 'post'


class CreatePostView(mixins.LoginRequiredMixin, generic.CreateView):
    """
    Simple create generic View to explain how to create new instances with Form
    """

    def get_success_url(self):
        return reverse('user', kwargs={'pk': self.request.user.id})

    model = PhotoPost
    template_name = "upload.html"
    fields = ['image', 'description']

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        return super(CreatePostView, self).form_valid(form)














