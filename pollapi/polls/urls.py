from django.urls import path
from .apiviews import  ChoiceList, CreateVote, PollViewSet, UserCreate, LoginView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choices_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create")
]

urlpatterns += router.urls
