from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'yash vendra',
        'title' : 'First Blog Post',
        'content' : 'This is the first post content',
        'date_posted' : 'August 2, 2021'
    },
    {
        'author': 'Anusha vendra',
        'title' : 'Second Blog Post',
        'content' : 'This is the Second post content',
        'date_posted' : 'August 20, 2021'
    },
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title' : 'About' })