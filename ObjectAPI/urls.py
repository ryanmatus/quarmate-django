from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'persons', views.PersonViewSet)
router.register(r'guests', views.GuestViewSet)
router.register(r'housemates', views.HousemateViewSet)
router.register(r'residence', views.ResidenceViewSet)
router.register(r'room', views.RoomViewSet)
router.register(r'visit', views.VisitViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
