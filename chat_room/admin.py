from django.contrib import admin
from chat_room.models import Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_creator', 'invited_users_admin', 'created_date']
    ordering = ['room_creator']

    def invited_users_admin(self, obj):
        return '\n'.join([user.username for user in obj.invited_users.all()])

    class Meta:
        model = Room

admin.site.register(Room, RoomAdmin)
