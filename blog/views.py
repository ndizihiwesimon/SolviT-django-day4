from django.shortcuts import redirect, render
from blog.forms import BlogForm
from blog.models import Blog
# Create your views here.
def  blog(request):
    blogs=Blog.objects.all()
    context={"blogs":blogs}
    return render(request, 'blog.html', context)

def add_blog(request):
    form=BlogForm()
    context={"form":form}
    if request.method == 'POST':
        blog_form=BlogForm(request.POST)
        if blog_form.is_valid():
            blog_form.save()
            return redirect("blogs")
        else:
            context={'form': blog_form}
            return render(request,'add_form.html',context)
    return redirect(request,'add_form.html',context)