from django.urls import path 
from . import views
app_name='shop'

urlpatterns = [
    # path('',views.ptest,name='ptest'),
    path('',views.allprdtcat,name='allprdtcat'),
    path('<slug:c_slug>/',views.allprdtcat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.productdetail,name='prodCatdeatil'),
    
]