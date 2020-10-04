from django.shortcuts import render, redirect

from .models import Comment
from .forms import CommentForm


def index(request):
    comments = Comment.objects.order_by("-date_added")

    # Keys of the context will be the variable names
    # accesible in the template, its values, the contents
    context = {"comments": comments}

    return render(request, "guestbook/index.html", context)


def sign(request):
    if request.method == "POST":
        # Instantiate the form with the data received
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = Comment(
                name=request.POST["name"], comment=request.POST["comment"]
            )
            new_comment.save()
            return redirect("index")
    else:
        form = CommentForm()

    # The final steps are equal for both methods.
    context = {"form": form}
    return render(request, "guestbook/sign.html", context)
