from django.contrib import admin
from e_public_app.models import CustomUser,AdminMD,Department,Peoples,Complaints
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(AdminMD)
admin.site.register(Department)
admin.site.register(Peoples)
admin.site.register(Complaints)
