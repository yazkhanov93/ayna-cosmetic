from django.urls import path, include
from api.order.views import *
from api.media_app.views import *
from api.products.views import *

urlpatterns = [
    path("home/", HomeListView.as_view(), name="home"),
    path("categories/", CategoryListView.as_view(), name="categories"),
    path("products/", ProductListView.as_view(), name="products"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product-id"),
    path("order/", OrderCreateView.as_view(), name="order"),
    path("media/", PostListView.as_view(), name="media"),
    path("media/<int:pk>/", PostDetailView.as_view(), name="media-Id"),
]