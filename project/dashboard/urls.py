from .views.counts import DashboardCounts
from django.urls import path

urlpatterns = [
    path("counts/<str:business_sn>", DashboardCounts.as_view(), name="dashboard-count")
]

