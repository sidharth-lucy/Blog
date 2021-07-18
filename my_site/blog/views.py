from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from datetime import date
from .models import Post

# posts=[
#     {
#     'slug':'hike-in-the-mountains',
#     'image':'hiking.jpg',
#     'author':'Lucy',
#     'date':date(2021,7,21),
#     'title':'Mountain Hiking',
#     'excerpt':'I was realy happy to see the view ,while doing mountain hicking !!',
#     "content": """
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
#             aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
#             dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
#             deserunt mollit anim id est laborum.
#
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
#             aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
#             dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
#             deserunt mollit anim id est laborum.
#
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
#             aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
#             dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
#             deserunt mollit anim id est laborum.
#             """
#     },
#
#     {
#     'slug':'coding',
#     'image':'hiking2.jpg',
#     'author':'Lucy',
#     'date':date(2021,6,22),
#     'title':'Soul Hiking',
#     'excerpt':'I was realy happy to see the view ,while doing mountain hicking !!',
#     "content":"""
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
#             aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
#             dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
#             deserunt mollit anim id est laborum.
#
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
#             aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
#             dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
#             deserunt mollit anim id est laborum.
#
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
#             aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
#             dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
#             deserunt mollit anim id est laborum.
#             """
#     },
#
#     {
#     'slug':'devil-era',
#     'image':'hiking3.jpg',
#     'author':'Lucy',
#     'date':date(2020,1,12),
#     'title':'BreathTaking',
#     'excerpt':'I was realy happy to see the view ,while doing mountain hicking !!',
#     "content":"""
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
#             aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
#             dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
#             deserunt mollit anim id est laborum.
#
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
#             aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
#             dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
#             deserunt mollit anim id est laborum.
#
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
#             aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
#             dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
#             deserunt mollit anim id est laborum.
#             """
#     },
#     {
#     'slug':'night-mare',
#     'image':'hiking4.jpeg',
#     'author':'Lucy',
#     'date':date(2011,9,2),
#     'title':'Dreams Comes True',
#     'excerpt':'I was realy happy to see the view ,while doing mountain hicking !!',
#     "content":"""
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
#             aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
#             dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
#             deserunt mollit anim id est laborum.
#
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
#             aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
#             dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
#             deserunt mollit anim id est laborum.
#
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
#             aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
#             dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
#             deserunt mollit anim id est laborum.
#             """
#     },
#     {
#     'slug':'mountains',
#     'image':'myimg.jpg',
#     'author':'Lucy',
#     'date':date(2021,11,21),
#     'title':'Feel The Wind',
#     'excerpt':'I was realy happy to see the view ,while doing mountain hicking !!',
#     "content":"""
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
#             aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
#             dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
#             deserunt mollit anim id est laborum.
#
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
#             aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
#             dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
#             deserunt mollit anim id est laborum.
#
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
#             aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
#             dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
#             deserunt mollit anim id est laborum.
#             """
#     },
#     {
#     'slug':'dreams',
#     'image':'hiking.jpg',
#     'author':'Lucy',
#     'date':date(2019,7,21),
#     'title':'Mountain Love',
#     'excerpt':'I was realy happy to see the view ,while doing mountain hicking !!',
#     "content":"""
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
#             aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
#             dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
#             deserunt mollit anim id est laborum.
#
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
#             aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
#             dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
#             deserunt mollit anim id est laborum.
#
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
#             aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
#             dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
#             deserunt mollit anim id est laborum.
#             """
#     },
#
#     {
#     'slug':'fear-fall',
#     'image':'hiking3.jpg',
#     'author':'Lucy',
#     'date':date(2018,7,1),
#     'title':'Love The Scene',
#     'excerpt':'I was realy happy to see the view ,while doing mountain hicking !!',
#     "content":"""
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
#             aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
#             dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
#             deserunt mollit anim id est laborum.
#
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
#             aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
#             dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
#             deserunt mollit anim id est laborum.
#
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
#             et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
#             aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
#             dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
#             deserunt mollit anim id est laborum.
#             """
#     }

# ]
# 
# def get_date(post):
#     return post['date']


def about_site(request):
    latest_post=Post.objects.all().order_by('-date')[:3]
    return render(request,'blog/home.html',{
                            'post_l':latest_post
                        })


def post_list(request):
    posts=Post.objects.all().order_by('-date')
    return render(request,'blog/post_list.html',{
                                                'po_list':posts
                                                })


def post_detail(request,slug):
    identified_post= Post.objects.get(slug=slug)
    # identified_post =next(p for p in posts if p['slug']==slug )
    email=identified_post.author.email_address
    tag_content= identified_post.tags.all()
    return render(request,'blog/post_detail.html',{
                                                    'po_detail':identified_post,
                                                    'email':email,
                                                    'tag_content':tag_content
                                                    })
