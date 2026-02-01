from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),

    # Notes
    path('notes', views.notes, name="notes"),
    path('shareNote/<int:primaryKey>', views.shareNote, name="shareNote"),
    path('delete_note/<int:primaryKey>', views.delete_note, name="delete_note"),
    path('notes_detail/<int:pk>/', views.NotesDetailView.as_view(), name='notes_detail'),

    # Homework
    path('homework/', views.homework, name='homework'),
    path('update_homework/<int:primaryKey>', views.update_homework, name="update_homework"),
    path('delete_homework/<int:primaryKey>', views.delete_homework, name="delete_homework"),

    # Tools
    path('youtube', views.youtube, name="youtube"),
    path('todo', views.todo, name="todo"),
    path('update_todo/<int:primaryKey>', views.update_todo, name="update_todo"),
    path('delete_todo/<int:primaryKey>', views.delete_todo, name="delete_todo"),
    path('books', views.books, name="books"),
    path('dictionary', views.dictionary, name="dictionary"),
    path('wiki', views.wiki, name="wiki"),
    path('conversion', views.conversion, name="conversion"),
    path('focus-timer/', views.focus_timer, name='focus-timer'),

    # Auth
    path('register', views.register, name="register"),

    # --- PASSWORD RESET FLOW ---
    
    # 1. Submit Email (The Modal points here)
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='dashboard/password_reset.html', # Keep this for direct access
             success_url='/password-reset/done/' # Forces redirect after modal submit
         ), 
         name='password_reset'),
    
    # 2. Success Message
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='dashboard/password_reset_done.html'
         ), 
         name='password_reset_done'),
    
    # 3. Link from Email
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='dashboard/password_reset_confirm.html'
         ), 
         name='password_reset_confirm'),
    
    # 4. Complete Message
    path('password-reset-complete/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='dashboard/password_reset_complete.html'
         ), 
         name='password_reset_complete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)