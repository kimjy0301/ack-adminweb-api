from rest_framework.routers import DefaultRouter
from . import views

app_name = "emrif"

router = DefaultRouter()
router.register("pc", views.EmrifPcViewSet)
router.register("equip", views.EmrifEquipViewSet)
router.register("error", views.EmrifErrorViewSet)
router.register("lab", views.EmrifLabViewSet)
router.register("dept", views.EmrifDeptViewSet)
router.register("emrifaib", views.EmrifAibViewSet)

urlpatterns = router.urls
