from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.html import format_html
from .models import User

# Register your models here.

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'is_staff','is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Cambio de Contraseña', {'fields': ('password_link',)}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'profile_picture')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    readonly_fields = ['password', 'password_link']

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)
    

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['password', 'password_link']
        return []
    

    def password_link(self, obj):
        url = reverse('admin:auth_user_password_change', args=[obj.pk])
        return format_html('<p>Por razones de seguridad, el cambio de contraseña esta disponible desde este formulario: <a href="{}">Cambiar contraseña</a></p>', url)

    password_link.short_description = 'Contraseña'


    def change_view(self, request, object_id, form_url='', extra_context=None):
        # self.fieldsets = self.get_fieldsets(request, None)
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        return super().change_view(request, object_id, form_url, extra_context)


    def response_change(self, request, obj):
        if "_password" in request.POST:
            return redirect('admin:dashboard_user_change',obj.pk)
        return super().response_change(request, obj)

admin.site.register(User, CustomUserAdmin)
