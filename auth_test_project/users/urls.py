from django.urls import path
from .views import (SignUpView, LoginView)
from rest_framework_simplejwt.views import (
    TokenRefreshSlidingView
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
    path('register/', SignUpView.as_view(), name="sign_up"),
]
