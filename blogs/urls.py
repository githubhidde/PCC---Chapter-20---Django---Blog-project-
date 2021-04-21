"""Defines URL patterns for blogs"""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
	# Home page
	path('', views.index, name='index'),
	# Page that show all blog topics
	path('blogs/', views.blogs, name='blogs'),
	# Detail page for a single blog.
	path('blogs/<int:blog_id>/', views.blog, name='blog'),
	# Page for adding a new topic
	path('new_blog', views.new_blog, name='new_blog'),
	# Page for adding a new entry
	path('new_entry/<int:blog_id>/', views.new_entry, name='new_entry'),
		# Page for editing an entry.
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]