from django.urls import path
from . import views

urlpatterns=[
    path('',views.stk_hld_home,name='stk_hld_home'),
    path('view_monitoring_minutes/',views.view_monitoring_minutes,name='view_monitoring_minutes'),
    path('view_statusreport_stk/',views.view_statusreport_stk,name='view_statusreport_stk'),
    path('view_dept_achievement/',views.view_dept_achievement,name='view_dept_achievement'),
    path('view_upcoming_meetings/',views.view_upcoming_meetings,name='view_upcoming_meetings'),
    path('view_past_target_stk/',views.view_past_target_stk,name='view_past_target_stk'),
    path('view_current_target_stk/',views.view_current_target_stk,name='view_current_target_stk'),
    path('feedback_form/',views.feedback_form,name='feedback_form'),
    path('feedback_form_action/',views.feedback_form_action,name='feedback_form_action'),
    path('sort_by_date_dept_achievement/',views.sort_by_date_dept_achievement,name='sort_by_date_dept_achievement'),
    path('sort_by_date_vmm',views.sort_by_date_vmm,name='sort_by_date_vmm'),
    path('sort_by_date_vum/',views.sort_by_date_vum,name='sort_by_date_vum'),
    path('sort_by_date_vsr/',views.sort_by_date_vsr,name='sort_by_date_vsr'),
    path('sh_show_ranking/',views.sh_show_ranking,name='sh_show_ranking'),
    path('view_target_analysis/',views.view_target_analysis_stk,name='view_target_analysis_stk'),
    path('view_achievement_analysis/',views.view_achievement_analysis_stk,name='view_achievement_analysis_stk'),
    # path('view_feedback_analysis/',views.view_feedback_analysis_stk,name='view_feedback_analysis_stk'),
    path('view_comparision_analysis/',views.view_comparision_analysis_stk,name='view_comparision_analysis_stk'),
    path('view_feedback_analysis/',views.view_feedback_analysis_stk,name='view_feedback_analysis_stk'),
    path('view_ap_analysis/',views.view_ap_analysis_stk,name='view_ap_analysis_stk'),
    path('download_ap_sh/',views.download_ap_sh,name='download_ap_sh'),
    path('view_dept_summary/',views.view_dept_summary,name='view_dept_summary'),

]
