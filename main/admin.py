from django.contrib import admin
from .models import History
from .models import Report_tags
from .models import Values_tags
from .models import Services_sp
from .models import Roles_sp
from .models import Infrastructure_sp
from .models import Trcking_tags
from .models import Priority_tags


# Register your models here.
admin.site.register(History)
admin.site.register(Report_tags)
admin.site.register(Values_tags)
admin.site.register(Services_sp)
admin.site.register(Roles_sp)
admin.site.register(Infrastructure_sp)
admin.site.register(Trcking_tags)
admin.site.register(Priority_tags)