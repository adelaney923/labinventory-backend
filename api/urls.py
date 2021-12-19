from django.urls import path
from .views.users import SignUp, SignIn, SignOut, ChangePassword
from .views.calibrators import CalibratorsView, CalibratorView

urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    path('calibrators/', CalibratorsView.as_view(), name='calibrators'),
    path('calibrators/<int:pk>', CalibratorView.as_view(), name='calibrator')
]