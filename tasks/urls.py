from django.urls import path
from tasks import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("", views.TaskListView.as_view(), name="task-list"),
    path("<int:pk>", views.TaskDetailView.as_view(), name="task-detail" ),
    path("task-create/", views.TaskCreateView.as_view(), name="task-create"),
    path("comment-update/<int:pk>", views.CommentUpdateView.as_view(), name="comment-update"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
]