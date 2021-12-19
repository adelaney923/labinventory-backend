from django.urls import path
from .views.users import SignUp, SignIn, SignOut, ChangePassword
from .views.calibrators import CalibratorsView, CalibratorView
from .views.consumables import ConsumablesView, ConsumableView
from .views.controls import ControlsView, ControlView
from .views.reagents import ReagentsView, ReagentView

urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    path('calibrators/', CalibratorsView.as_view(), name='calibrators'),
    path('calibrators/<int:pk>', CalibratorView.as_view(), name='calibrator'),
    path('consumables/', ConsumablesView.as_view(), name='consumables'),
    path('consumables/<int:pk>', ConsumableView.as_view(), name='consumable'),
    path('controls/', ControlsView.as_view(), name='controls'),
    path('controls/<int:pk>', ControlView.as_view(), name='control'),
    path('reagents/', ReagentsView.as_view(), name='reagents'),
    path('reagents/<int:pk>', ReagentView.as_view(), name='reagent')
]