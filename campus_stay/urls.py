
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from reviews.api.views import PropertyReviewViewSet
from users.api.views import UserViewSet
from favourites.api.views import FavouritesViewSet
from users.api.views import CustomTokenObtainPairView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from properties.api.views import PropertiesViewSet
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)
from universities.api.views import UniversitiesViewSet
from universities.api.views import CampusViewSet
from user_messages.urls import urlpatterns as user_messages_urls

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'properties', PropertiesViewSet)
router.register(r'universities', UniversitiesViewSet)
router.register(r'campuses', CampusViewSet)
router.register(r'reviews',PropertyReviewViewSet,basename='propertyreview')
router.register(r'favourites', FavouritesViewSet, basename='favourites')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('', include(user_messages_urls)),
    path('api/v1/auth/token/',CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/auth/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('admin/', admin.site.urls),
    
    ### API documentation
     path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
