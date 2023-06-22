from django.urls import path
from . import views as v

urlpatterns = [
    #list of urls to handel file operation
    path('', v.Home.as_view(), name="home"),
    path("folder/<int:id>", v.FolderView.as_view(), name="folder"),
    path("folder/create", v.FolderCreateView.as_view(), name="folder_create"),
    path("folder/delete", v.FolderDelete.as_view(), name="folder_delete"),
    path("file/delete", v.FileDelete.as_view(), name="file_delete"),
    path("signup", v.UserCreateView.as_view(), name="signup"),
    path("logout", v.user_logout, name="logout"),
    path("login", v.Login.as_view(), name="login"),
]