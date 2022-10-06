from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import func_xml
from wishlist.views import func_json
from wishlist.views import show_json_id
from wishlist.views import show_xml_id
from wishlist.views import register
from wishlist.views import login_user
from wishlist.views import logout_user
from wishlist.views import show_wishlist_ajax
from wishlist.views import add_wishlist

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', func_xml, name='func_xml'),
    path('json/', func_json, name='func_json'),
    path('json/<int:id>', show_json_id, name='show_json_id'),
    path('xml/<int:id>', show_xml_id, name='show_xml_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('ajax/', show_wishlist_ajax, name='show_wishlist_ajax'),
    path('ajax/', add_wishlist, name='add_wishlist')
]
