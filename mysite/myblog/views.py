from django.shortcuts import render, redirect, reverse
from django.views import generic
from .models import Post, Comment
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.views.generic.edit import FormMixin
from .forms import CommentForm


# Create your views here.
class PostListView(generic.ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = "posts"
    paginate_by = 3


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = 'post'
    form_class = CommentForm

    def get_success_url(self):
        return reverse("post", kwargs={"pk": self.object.pk})

    # standartinis post metodo perrašymas, naudojant FormMixin, galite kopijuoti tiesiai į savo projektą.
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.post = self.object
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


def search(request):
    query = request.GET.get("query")
    posts = Post.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query) | Q(author__username__icontains=query))
    context = {
        "posts": posts,
        "query": query,
    }
    return render(request, template_name="search.html", context=context)


class MyPostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = "myposts.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class MyCommentListView(LoginRequiredMixin, generic.ListView):
    model = Comment
    template_name = "mycomments.html"
    context_object_name = "comments"

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'registration/register.html')
