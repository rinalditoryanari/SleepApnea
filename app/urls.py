from django.urls import path
from django.shortcuts import render
from .view import dashboard, layout, blankpage, bootstrap, components, forms, google_maps, modules, auth, error, features, credits, utilities

urlpatterns = [
    path('abcdefgh', dashboard.dashboard),

    path('', dashboard.index0, name='dashboard'),
    path('dashboard-general-dashboard', dashboard.index,
         name='dashboard-general-dashboard'),


    # Layout
    path("layout-default-layout", layout.layout_default_layout,
         name="layout-default-layout"),
    path("layout-top-navigation", layout.layout_top_navigation,
         name="layout-top-navigation"),
    path("layout-transparent", layout.layout_transparent,
         name="layout-transparent"),

    # Blank Page
    path("blank-page", blankpage.blank_page, name="blank-page"),

    # Bootstrap
    path("bootstrap-alert", bootstrap.bootstrap_alert, name="bootstrap-alert"),
    path("bootstrap-badge", bootstrap.bootstrap_badge, name="bootstrap-badge"),
    path("bootstrap-breadcrumb", bootstrap.bootstrap_breadcrumb,
         name="bootstrap-breadcrumb"),
    path("bootstrap-buttons", bootstrap.bootstrap_buttons,
         name="bootstrap-buttons"),
    path("bootstrap-card", bootstrap.bootstrap_card, name="bootstrap-card"),
    path("bootstrap-carousel", bootstrap.bootstrap_carousel,
         name="bootstrap-carousel"),
    path("bootstrap-collapse", bootstrap.bootstrap_collapse,
         name="bootstrap-collapse"),
    path("bootstrap-dropdown", bootstrap.bootstrap_dropdown,
         name="bootstrap-dropdown"),
    path("bootstrap-form", bootstrap.bootstrap_form, name="bootstrap-form"),
    path("bootstrap-list-group", bootstrap.bootstrap_list_group,
         name="bootstrap-list-group"),
    path("bootstrap-media-object", bootstrap.bootstrap_media_object,
         name="bootstrap-media-object"),
    path("bootstrap-modal", bootstrap.bootstrap_modal, name="bootstrap-modal"),
    path("bootstrap-nav", bootstrap.bootstrap_nav, name="bootstrap-nav"),
    path("bootstrap-navbar", bootstrap.bootstrap_navbar, name="bootstrap-navbar"),
    path("bootstrap-pagination", bootstrap.bootstrap_pagination,
         name="bootstrap-pagination"),
    path("bootstrap-popover", bootstrap.bootstrap_popover,
         name="bootstrap-popover"),
    path("bootstrap-progress", bootstrap.bootstrap_progress,
         name="bootstrap-progress"),
    path("bootstrap-table", bootstrap.bootstrap_table, name="bootstrap-table"),
    path("bootstrap-tooltip", bootstrap.bootstrap_tooltip,
         name="bootstrap-tooltip"),
    path("bootstrap-typography", bootstrap.bootstrap_typography,
         name="bootstrap-typography"),


    # components
    path("components-article", components.components_article,
         name="components-article"),
    path("components-avatar", components.components_avatar,
         name="components-avatar"),
    path("components-chat-box", components.components_chat_box,
         name="components-chat-box"),
    path("components-empty-state", components.components_empty_state,
         name="components-empty-state"),
    path("components-gallery", components.components_gallery,
         name="components-gallery"),
    path("components-hero", components.components_hero, name="components-hero"),
    path("components-multiple-upload", components.components_multiple_upload,
         name="components-multiple-upload"),
    path("components-pricing", components.components_pricing,
         name="components-pricing"),
    path("components-statistic", components.components_statistic,
         name="components-statistic"),
    path("components-tab", components.components_tab, name="components-tab"),
    path("components-table", components.components_table, name="components-table"),
    path("components-user", components.components_user, name="components-user"),
    path("components-wizard", components.components_wizard,
         name="components-wizard"),

    # forms
    path("forms-advanced-form", forms.forms_advanced_form,
         name="forms-advanced-form"),
    path("forms-editor", forms.forms_editor, name="forms-editor"),
    path("forms-validation", forms.forms_validation, name="forms-validation"),

    # google maps
    # belum tersedia

    # modules
    path("modules-calendar", modules.modules_calendar, name="modules-calendar"),
    path("modules-chartjs", modules.modules_chartjs, name="modules-chartjs"),
    path("modules-datatables", modules.modules_datatables,
         name="modules-datatables"),
    path("modules-flag", modules.modules_flag, name="modules-flag"),
    path("modules-font-awesome", modules.modules_font_awesome,
         name="modules-font-awesome"),
    path("modules-ion-icons", modules.modules_ion_icons, name="modules-ion-icons"),
    path("modules-owl-carousel", modules.modules_owl_carousel,
         name="modules-owl-carousel"),
    path("modules-sparkline", modules.modules_sparkline, name="modules-sparkline"),
    path("modules-sweet-alert", modules.modules_sweet_alert,
         name="modules-sweet-alert"),
    path("modules-toastr", modules.modules_toastr, name="modules-toastr"),
    path("modules-vector-map", modules.modules_vector_map,
         name="modules-vector-map"),
    path("modules-weather-icon", modules.modules_weather_icon,
         name="modules-weather-icon"),

    # auth
    path("auth-forgot-password", auth.auth_forgot_password,
         name="auth-forgot-password"),
    path("auth-login", auth.auth_login, name="auth-login"),
    path("auth-login2", auth.auth_login2, name="auth-login2"),
    path("auth-register", auth.auth_register, name="auth-register"),
    path("auth-reset-password", auth.auth_reset_password,
         name="auth-reset-password"),

    # error
    path("error-403", error.error_403, name="error-403"),
    path("error-404", error.error_404, name="error-404"),
    path("error-500", error.error_500, name="error-500"),
    path("error-503", error.error_503, name="error-503"),

    # features
    path("features-activities", features.features_activities,
         name="features-activities"),
    path("features-post-create", features.features_post_create,
         name="features-post-create"),
    path("features-post", features.features_post, name="features-post"),
    path("features-profile", features.features_profile, name="features-profile"),
    path("features-settings", features.features_settings, name="features-settings"),
    path("features-setting-detail", features.features_setting_detail,
         name="features-setting-detail"),
    path("features-tickets", features.features_tickets, name="features-tickets"),

    # utilities
    path("utilities-contact", utilities.utilities_contact,
         name="utilities-contact"),
    path("utilities-invoice", utilities.utilities_invoice,
         name="utilities-invoice"),
    path("utilities-subscribe", utilities.utilities_subscribe,
         name="utilities-subscribe"),

    # credits
    path("credits", credits.credits, name="credits"),

]
