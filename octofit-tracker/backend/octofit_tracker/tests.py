from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_user_creation(self):
        team = Team.objects.create(name='TestTeam', description='desc')
        user = User.objects.create(name='Test User', email='test@example.com', team=team.name)
        self.assertEqual(user.name, 'Test User')

    def test_team_creation(self):
        team = Team.objects.create(name='TestTeam2', description='desc2')
        self.assertEqual(team.name, 'TestTeam2')

    def test_activity_creation(self):
        team = Team.objects.create(name='TestTeam3', description='desc3')
        user = User.objects.create(name='Test User2', email='test2@example.com', team=team.name)
        activity = Activity.objects.create(user=user.name, activity_type='Run', duration=10, date='2026-03-14')
        self.assertEqual(activity.activity_type, 'Run')

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team='TestTeam', points=100)
        self.assertEqual(leaderboard.points, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='TestWorkout', description='desc', difficulty='Easy')
        self.assertEqual(workout.name, 'TestWorkout')
