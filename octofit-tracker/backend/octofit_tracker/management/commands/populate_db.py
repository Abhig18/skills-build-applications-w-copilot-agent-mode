from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email='john.doe@example.com', name='John Doe', password='password123')
        user2 = User.objects.create(email='jane.smith@example.com', name='Jane Smith', password='password123')

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1, user2)

        # Create test activities
        Activity.objects.create(user=user1, type='Running', duration=30, date='2025-05-01')
        Activity.objects.create(user=user2, type='Cycling', duration=45, date='2025-05-02')

        # Create test leaderboard
        Leaderboard.objects.create(team=team1, points=100)

        # Create test workouts
        Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session to start the day.')
        Workout.objects.create(name='HIIT', description='High-Intensity Interval Training for advanced users.')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
