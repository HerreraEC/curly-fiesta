from djongo import models

# User model
class User(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=50)
    def __str__(self):
        return self.name

    class Meta:
        app_label = 'octofit_tracker'

# Team model
class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

    class Meta:
        app_label = 'octofit_tracker'

# Activity model
class Activity(models.Model):
    _id = models.ObjectIdField()
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return f"{self.user} - {self.activity_type}"

    class Meta:
        app_label = 'octofit_tracker'

# Leaderboard model
class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team} - {self.points}"

    class Meta:
        app_label = 'octofit_tracker'

# Workout model
class Workout(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=50)
    def __str__(self):
        return self.name

    class Meta:
        app_label = 'octofit_tracker'
