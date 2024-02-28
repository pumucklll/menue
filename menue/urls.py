from django.urls import path
from . import views, admin

urlpatterns = [
    # Other URL patterns
    path('', views.menue_alkoholfrei.as_view(), name="alkoholfrei"),
    path("kaffee", views.menue_kaffee.as_view(), name="kaffee"),
    path("bier/", views.menue_bier.as_view(), name="bier"),
    path("wein/", views.menue_wein.as_view(), name="wein"),
    path("speisen/", views.menue_speisen.as_view(), name="speisen"),
    path('export-csv/', views.export_csv, name='export_csv'),
    path('export-query-to-csv/', views.export_query_to_csv, name='export_query_to_csv'),
    path('export-html-to-csv/', views.export_html_to_csv, name='export_html_to_csv'),
    path('import-csv/', views.import_csv, name='import_csv'),
    path('home/', views.home, name='home'),
]
