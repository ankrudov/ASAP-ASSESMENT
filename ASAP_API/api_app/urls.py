from django.urls import path
from .views import MemberView

urlpatterns = [
    path('members/', MemberView.as_view()),
    path('members/<int:id>',MemberView.as_view()),
    
]
