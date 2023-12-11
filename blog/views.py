from django.shortcuts import render
from datetime import date

all_posts = [
    {
        'slug': 'learning-django',
        'title': 'django course',
        'author': 'mohammad ordokhani',
        'image': 'django.png',
        'date': date(2021, 4, 5),
        'short_description': 'this is django course in toplearn from zero to hero',
        'content': """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit.
            Animi cum debitis, enim excepturi exercitationem ipsa
            molestiae nobis praesentium quod temporibus!
            Aliquid asperiores corporis deserunt dignissimos,
            doloribus inventore ipsam labore nostrum obcaecati
            quas suscipit vitae. Dignissimos fugit odio possimus sint voluptatem.
        """
    },
    {
        'slug': 'learning-python',
        'title': 'python course',
        'author': 'mohammad ordokhani',
        'image': 'Python.png',
        'date': date(2021, 6, 3),
        'short_description': 'this is django course in toplearn from zero to hero',
        'content': """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit.
            Animi cum debitis, enim excepturi exercitationem ipsa
            molestiae nobis praesentium quod temporibus!
            Aliquid asperiores corporis deserunt dignissimos,
            doloribus inventore ipsam labore nostrum obcaecati
            quas suscipit vitae. Dignissimos fugit odio possimus sint voluptatem.
        """
    },
    {
        'slug': 'learning-machine laerning',
        'title': 'ML course',
        'author': 'mohammad ordokhani',
        'image': 'ml.jpg',
        'date': date(2021, 3, 1),
        'short_description': 'this is django course in toplearn from zero to hero',
        'content': """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit.
            Animi cum debitis, enim excepturi exercitationem ipsa
            molestiae nobis praesentium quod temporibus!
            Aliquid asperiores corporis deserunt dignissimos,
            doloribus inventore ipsam labore nostrum obcaecati
            quas suscipit vitae. Dignissimos fugit odio possimus sint voluptatem.
        """
    },

]


# Create your views here.

def get_date(post):
    return post['date']


def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-2:]
    return render(request, 'blog/index.html', {
        'latest_posts': latest_posts
    })


def posts(request):
    context = {
        'all_posts': all_posts
    }
    return render(request, 'blog/all-posts.html', context)


def single_post(request, slug):
    return render(request, 'blog/post-detail.html')
