from django.shortcuts import render

from .models import Comment
from .forms import CommentForm


def index(request):
    comments = Comment.objects.order_by("-date_added")

    # Keys of the context will be the variable names
    # accesible in the template, its values, the contents
    context = {"comments": comments}

    return render(request, "guestbook/index.html", context)


def sign(request):
    form = CommentForm()
    context = {"form": form}
    return render(request, "guestbook/sign.html", context)
