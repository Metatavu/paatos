from django.core.management.base import BaseCommand

from decisions.importer.paatos_scraper import PaatosScraperImporter


class Command(BaseCommand):
    help = 'Imports Espoo Dynasty data'

    def add_arguments(self, parser):
        parser.add_argument('zipfile', type=str)
        parser.add_argument('--flush', action='store_true', dest='flush', default=False,
                            help='Delete all existing objects first')

    def handle(self, *args, **options):
        defaults = dict(
            name='Espoo Dynasty'
        )
        importer = PaatosScraperImporter('espoo_dynasty', defaults, options)
        importer.import_data()
