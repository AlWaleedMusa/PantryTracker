from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.home, name="home"),
    path("add_item/<int:pk>/", views.add_item, name="add_item"),
    path("remove_item/<int:pk>/", views.remove_item, name="remove_item"),
    path("add_new_item/", views.add_new_item, name="add_new_item"),
    path("edit_item/<int:pk>/", views.edit_item, name="edit_item"),
    path("delete_item/<int:pk>/", views.delete_item, name="delete_item"),

]
