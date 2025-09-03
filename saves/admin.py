from django import forms
from django.contrib import admin
from .models import Saves
from posts.models import Post

class SavesAdminForm(forms.ModelForm):
    class Meta:
        model = Saves
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SavesAdminForm, self).__init__(*args, **kwargs)

        # Only filter posts if a user has been selected
        if 'user' in self.data:
            try:
                user_id = int(self.data.get('user'))
                self.fields['post'].queryset = Post.objects.filter(owner__id=user_id)
            except (ValueError, TypeError):
                pass  # fallback to default
        elif self.instance.pk:
            # If editing an instance, filter by the current user of the save
            self.fields['post'].queryset = Post.objects.filter(owner=self.instance.user)
        else:
            self.fields['post'].queryset = Post.objects.none()
    
class SavesAdmin(admin.ModelAdmin):
    form = SavesAdminForm
    list_display = ['user', 'post', 'saved_at']
    search_fields = ['user__username', 'post__title']

admin.site.register(Saves, SavesAdmin)