from rest_framework.routers import DefaultRouter
from .views import APPReviewView


router = DefaultRouter()
router.register('applications-reviews', APPReviewView)

urlpatterns = router.urls