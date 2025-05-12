from django.contrib import admin

from .models import User, Goal, Project, Task

# Register your models here.

class UserAdmin(admin.ModelAdmin):
  pass

class GoalAdmin(admin.ModelAdmin):
  pass

# class GoalHistoryAdmin(admin.ModelAdmin):
#   pass

class ProjectAdmin(admin.ModelAdmin):
  pass

class TaskAdmin(admin.ModelAdmin):
  pass


admin.site.register(User, UserAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
