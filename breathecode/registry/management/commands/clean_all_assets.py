import os, requests, logging
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from ...models import Asset
from breathecode.admissions.models import Academy
from ...tasks import async_pull_from_github
from slugify import slugify
from ...actions import clean_asset_readme

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'The execution of this command release a clean function for all assets '

    def handle(self, *args, **options):
        assets = Asset.objects.all()

        for asset in assets:
            clean_asset_readme(asset)
