from django.urls import path
from . import views

urlpatterns=[
    path('',views.dept_home,name='dept_home'),
	path('view_upcoming_montitoring_meetings_action/',views.view_upcoming_monitoring_meetings_action_dept,name='view_upcoming_monitoring_meetings_action_dept'),
    path('view_upcoming_individual_meetings_action/',views.view_upcoming_individual_meetings_action_dept,name='view_upcoming_individual_meetings_action_dept'),
    path('view_prev_monitoring_meeting/',views.view_prev_monitoring_meeting,name='view_prev_monitoring_meeting'),
    path('view_prev_individual_meeting/',views.view_prev_individual_meeting,name='view_prev_individual_meeting'),
    path('view_status_report/',views.view_status_report_dept,name='view_status_report_dept'),
    path('notify/',views.notify_dept,name='notify_dept'),
    path('notify_action/',views.notify_action_dept,name='notify_action_dept'),
    path('view_notification/',views.view_notification_dept,name='view_notification_dept'),
    path('view_past_target_dept/',views.view_past_target_dept,name='view_past_target_dept'),
    path('view_current_target/',views.view_current_target_dept,name='view_current_target_dept'),
    path('update_status_current_target/<str:tid>',views.update_status_current_target,name='update_status_current_target'),
    path('update_report_current_target/<str:tid>',views.update_report_current_target,name='update_report_current_target'),
    path('show_ranking_d/',views.show_ranking_d,name='show_ranking_d'),
    path('view_target_analysis/',views.view_target_analysis_dept,name='view_target_analysis_dept'),
    path('view_achievement_analysis/',views.view_achievement_analysis_dept,name='view_achievement_analysis_dept'),
    path('view_comparision_analysis/',views.view_comparision_analysis_dept,name='view_comparision_analysis_dept'),
    path('view_feedback_analysis/',views.view_feedback_analysis_dept,name='view_feedback_analysis_dept'),
    path('view_ap_analysis/',views.view_ap_analysis_dept,name='view_ap_analysis_dept'),
    path('chart/',views.chart,name='chart'),
    path('download_ap/',views.download_ap,name='download_ap'),

]

# Url kept similar to dipp app
# Added '_dept' to most of the urls
