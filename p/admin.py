from django.contrib import admin
from django.apps import apps

app = apps.get_app_config('p')

class LandedAdmin(admin.ModelAdmin):
    list_display = ('email', 'role', 'when')
    list_filter = list_display

for model_name, model in app.models.items():
    exclude = ['baseuser_groups', 'baseuser_user_permissions']
    if model_name == 'landed':
        admin.site.register(model, LandedAdmin)
    elif model_name not in exclude:
        admin.site.register(model)
