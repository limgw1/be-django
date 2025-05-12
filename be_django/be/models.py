from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class User(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  email = models.EmailField(max_length=255)
  # password_hash = models.pass
  created_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.first_name} {self.last_name} - {self.email}"

class Goal(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class GoalHistory(models.Model):
  goal_id = models.ForeignKey(Goal, on_delete=models.CASCADE)
  goal_name = models.CharField(max_length=140)
  goal_description = models.CharField(max_length=2000)
  priority = models.IntegerField(
    validators=[MinValueValidator(1), MaxValueValidator(10)]
  )
  due_date = models.DateTimeField()
  created_at = models.DateTimeField(auto_now=True)

class Project(models.Model):
  project_name = models.CharField(max_length=140)
  project_description = models.CharField(max_length=2000)
  parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Task(models.Model):
  TASK_TYPE_CHOICES = {
    "1off" : "one-off completable task",
    "recc" : "recurring task",
    "note" : "note task (non completable)"
  }
  task_name = models.CharField(max_length=140)
  task_type = models.CharField(max_length=5, choices=TASK_TYPE_CHOICES)
  task_description = models.CharField(max_length=2000)
  parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
  project_id = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  due_date = models.DateTimeField()
  created_at = models.DateTimeField(auto_now=True)
  priority = models.IntegerField(
    validators=[MinValueValidator(1), MaxValueValidator(10)]
  )
  is_completed = models.BooleanField()
  recurrence_interval = models.DurationField()

  
