from django.urls import include, path

from rest_framework import routers

from manifesto.views import EntryViewSet, EntryTypeViewSet

router = routers.SimpleRouter()

router.register(r'entry', EntryViewSet)
router.register(r'entry-type', EntryTypeViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
