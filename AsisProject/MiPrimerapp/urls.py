3. from django.urls import path
4.
5. from MiPrimerapp import views
6.
7. urlpatterns = [
8. path('',views.index, name='index')
9. ]