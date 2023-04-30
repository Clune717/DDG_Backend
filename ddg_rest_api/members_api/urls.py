from django.urls import path
from . import views

urlpatterns = [
    path('api/members', views.MemberList.as_view(), name='member_list'), # api/members will be routed to the ContactList view for handling
    path('api/members/<int:pk>', views.MemberDetail.as_view(), name='member_detail'),
]