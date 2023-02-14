from django.urls import path
from django.shortcuts import render
from app import views

urlpatterns = [
    path('abcdefgh', views.dashboard),

    path('', views.index0, name='dashboard'),
    path('dashboard-general-dashboard', views.index,
         name='dashboard-general-dashboard'),


    # Layout
    path("layout-default-layout", views.layout_default_layout,
         name="layout-default-layout"),

    # Blank Page
    path("blank-page", views.blank_page, name="blank-page"),

    # Bootstrap
    path("bootstrap-alert", views.bootstrap_alert, name="bootstrap-alert"),
    path("bootstrap-badge", views.bootstrap_badge, name="bootstrap-badge"),
    path("bootstrap-breadcrumb", views.bootstrap_breadcrumb,
         name="bootstrap-breadcrumb"),
    path("bootstrap-buttons", views.bootstrap_buttons, name="bootstrap-buttons"),
    path("bootstrap-card", views.bootstrap_card, name="bootstrap-card"),
    path("bootstrap-carousel", views.bootstrap_carousel, name="bootstrap-carousel"),
    path("bootstrap-collapse", views.bootstrap_collapse, name="bootstrap-collapse"),
    path("bootstrap-dropdown", views.bootstrap_dropdown, name="bootstrap-dropdown"),
    path("bootstrap-form", views.bootstrap_form, name="bootstrap-form"),
    path("bootstrap-list-group", views.bootstrap_list_group,
         name="bootstrap-list-group"),
    path("bootstrap-media-object", views.bootstrap_media_object,
         name="bootstrap-media-object"),
    path("bootstrap-modal", views.bootstrap_modal, name="bootstrap-modal"),
    path("bootstrap-nav", views.bootstrap_nav, name="bootstrap-nav"),
    path("bootstrap-navbar", views.bootstrap_navbar, name="bootstrap-navbar"),
    path("bootstrap-pagination", views.bootstrap_pagination,
         name="bootstrap-pagination"),
    path("bootstrap-popover", views.bootstrap_popover, name="bootstrap-popover"),
    path("bootstrap-progress", views.bootstrap_progress, name="bootstrap-progress"),
    path("bootstrap-table", views.bootstrap_table, name="bootstrap-table"),
    path("bootstrap-tooltip", views.bootstrap_tooltip, name="bootstrap-tooltip"),
    path("bootstrap-typography", views.bootstrap_typography,
         name="bootstrap-typography"),


    # components
    path("components-article", views.components_article, name="components-article"),
    path("components-avatar", views.components_avatar, name="components-avatar"),
    path("components-chat-box", views.components_chat_box,
         name="components-chat-box"),
    path("components-empty-state", views.components_empty_state,
         name="components-empty-state"),
    path("components-gallery", views.components_gallery, name="components-gallery"),
    path("components-hero", views.components_hero, name="components-hero"),
    path("components-multiple-upload", views.components_multiple_upload,
         name="components-multiple-upload"),
    path("components-pricing", views.components_pricing, name="components-pricing"),
    path("components-statistic", views.components_statistic,
         name="components-statistic"),
    path("components-tab", views.components_tab, name="components-tab"),
    path("components-table", views.components_table, name="components-table"),
    path("components-user", views.components_user, name="components-user"),
    path("components-wizard", views.components_wizard, name="components-wizard"),

    # forms
    path("forms-advanced-form", views.forms_advanced_form,
         name="forms-advanced-form"),
    path("forms-editor", views.forms_editor, name="forms-editor"),
    path("forms-validation", views.forms_validation, name="forms-validation"),

    # google maps
    # belum tersedia

    # modules
    path("modules-calendar", views.modules_calendar, name="modules-calendar"),
    path("modules-chartjs", views.modules_chartjs, name="modules-chartjs"),
    path("modules-datatables", views.modules_datatables, name="modules-datatables"),
    path("modules-flag", views.modules_flag, name="modules-flag"),
    path("modules-font-awesome", views.modules_font_awesome,
         name="modules-font-awesome"),
    path("modules-ion-icons", views.modules_ion_icons, name="modules-ion-icons"),
    path("modules-owl-carousel", views.modules_owl_carousel,
         name="modules-owl-carousel"),
    path("modules-sparkline", views.modules_sparkline, name="modules-sparkline"),
    path("modules-sweet-alert", views.modules_sweet_alert,
         name="modules-sweet-alert"),
    path("modules-toastr", views.modules_toastr, name="modules-toastr"),
    path("modules-vector-map", views.modules_vector_map, name="modules-vector-map"),
    path("modules-weather-icon", views.modules_weather_icon,
         name="modules-weather-icon"),

    # auth
    path("auth-forgot-password", views.auth_forgot_password,
         name="auth-forgot-password"),
    path("auth-login", views.auth_login, name="auth-login"),
    path("auth-login2", views.auth_login2, name="auth-login2"),
    path("auth-register", views.auth_register, name="auth-register"),
    path("auth-reset-password", views.auth_reset_password,
         name="auth-reset-password"),

    # error
    path("error-403", views.error_403, name="error-403"),
    path("error-404", views.error_404, name="error-404"),
    path("error-500", views.error_500, name="error-500"),
    path("error-503", views.error_503, name="error-503"),

    # features
    path("features-activities", views.features_activities,
         name="features-activities"),
    path("features-post-create", views.features_post_create,
         name="features-post-create"),
    path("features-post", views.features_post, name="features-post"),
    path("features-profile", views.features_profile, name="features-profile"),
    path("features-settings", views.features_settings, name="features-settings"),
    path("features-setting-detail", views.features_setting_detail,
         name="features-setting-detail"),
    path("features-tickets", views.features_tickets, name="features-tickets"),

    # utilities
    path("utilities-contact", views.utilities_contact, name="utilities-contact"),
    path("utilities-invoice", views.utilities_invoice, name="utilities-invoice"),
    path("utilities-subscribe", views.utilities_subscribe,
         name="utilities-subscribe"),

    # credits
    path("credits", views.credits, name="credits"),

]
