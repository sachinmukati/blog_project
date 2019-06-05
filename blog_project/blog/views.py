from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.models import post

def post_list_view(request):
    post_list = post.objects.all()
    paginator = Paginator(post_list,3)
    page_number=request.GET.get("page")
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=Paginator.page(1)
    except EmptyPage:
        post_list=Paginator.page(Paginator.num_pages)
    return render(request,'blog/post.html',{"post_list":post_list})

def post_detail_view(request,year,month,day,post):
    post=get_object_or_404(post,slug=post,
                           status="published",
                           publish_year=year,
                           publish_month=month,
                           publish_day=day)
    return render(request ,"blog/post_deatil.html",{ "post":post})