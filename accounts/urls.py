from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


# app_name = 'accounts'

urlpatterns = [
    #     # login, logout, dashboard ========================================================================================================
    #     path("login/", auth_views.LoginView.as_view(), name='login'),
    #     path("logout/", auth_views.LogoutView.as_view(template_name='registration/logout.html'), name="logout"),
    #     # password change urls ========================================================================================================
    #     path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy("password_change_done")),
    #          name='password_change'),
    #     path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(),
    #          name='password_change_done'),
    #     # password reset urls ========================================================================================================
    #     path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy("password_reset_done"), ),
    #          name="password_reset"),
    #     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
    #          name="password_reset_done"),
    #     path("password_reset/<uidb64>/<token>/",
    #          auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy("password_reset_complete")), name='password_reset_confirm'),
    #     path("password_reset/complete/", auth_views.PasswordResetCompleteView.as_view(),
    #          name='password_reset_complete')
    #
    path('profile/', views.dashboard, name='dashboard'),
    path('profile/edit/', views.edit, name='edit_profile'),
    path('user/', include('django.contrib.auth.urls')),
    path('register/', views.register_user, name="register"),
]
