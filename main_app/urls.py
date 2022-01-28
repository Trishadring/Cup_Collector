from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
		path('cups/', views.cup_index, name="index"),
		path('cups/<int:cup_id>/', views.cup_detail, name='detail'),
		path('cups/create/', views.CupCreate.as_view(), name='cups_create'),
		path('cups/<int:pk>/update/', views.CupUpdate.as_view(), name='cups_update'),
		path('cups/<int:pk>/delete/', views.CupDelete.as_view(), name='cups_delete'),
		path('cups/<int:cup_id>/add_use/', views.add_use, name='add_use'),
		path('cups/<int:cup_id>/assoc_sticker/<int:sticker_id>/', views.assoc_sticker, name='assoc_sticker'),
		path('stickers/', views.StickerList.as_view(), name='stickers_index'),
		path('stickers/<int:pk>/', views.StickerDetail.as_view(), name='stickers_detail'),
		path('stickers/create/', views.StickerCreate.as_view(), name='stickers_create'),
		path('stickers/<int:pk>/update/', views.StickerUpdate.as_view(), name='stickers_update'),
		path('stickers/<int:pk>/delete/', views.StickerDelete.as_view(), name='stickers_delete'),
]