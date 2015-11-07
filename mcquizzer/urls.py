from django.conf.urls import include, url
from django.contrib import admin
from quizzer import views

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^main_page.html$', views.main_page, name='main_page'),
    url(r'^user/$', views.user_page, name='user_page'),
    
    url(r'^login/$','django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', views.logout_page, name='logout_page'),
    url(r'^register/$', views.register_page, name='register_page'),
    url(r'^registration/register_success.html', views.register_success_page, name='register_success_page'),
    url(r'^saveqz/$', views.quiz_save_page, name='quiz_save_page'),
    url(r'^saveq/(?P<quiz_id>.+?)/$', views.question_save_page, name='question_save_page'),
    url(r'^editq/(?P<qid>.+?)/$', views.question_edit, name='question_edit'),
    url(r'^quiz/(?P<quiz_id>.+?)/$', views.quiz, name='quiz'),
    url(r'^deleteq/(?P<question_id>.+?)/(?P<quiz_id>.+?)/$', views.question_delete, name='question_delete'),
    url(r'^deleteqz/(?P<quiz_id>.+?)/$', views.quiz_delete, name='quiz_delete'),
    url(r'^result/score/(?P<quiz_id>.+?)/$', views.get_score, name='get_score'),
    url(r'^score/(?P<quiz_id>.+?)/$', views.score, name='score'),
    url(r'^set_date/(?P<quiz_id>.+?)/$', views.set_date, name='set_date'),
]
