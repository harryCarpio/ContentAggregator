from django.core.management.base import BaseCommand, CommandError
from aggregator.models import Website
from aggregator.utils import aggregate_news


class Command(BaseCommand):
    def handle(self, *args, **options):
        # for poll_id in options['poll_ids']:
        print("Running django command for content aggregation...")
        websites = Website.objects.all()
        for website in websites:
            aggregate_news(website)
