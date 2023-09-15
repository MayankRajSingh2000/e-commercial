from django.urls import path
from .import views #from shop import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("shop/", views.shop, name="shop"),
    path("search/", views.search, name="search"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("shop/<int:id>/", views.detail, name="detail"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("orders/", views.order, name="orders"),
    #path("tracker/", views.tracker, name="TrackingStatus"),
    #path("products/<int:myid>", views.productView, name="ProductView"),
    #path("handlerequest/", views.handlerequest, name="HandleRequest"),
]