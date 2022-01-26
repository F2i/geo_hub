from django.core.management.base import BaseCommand
from django.db  import connection
from pathlib import Path
import os

class Command(BaseCommand):
    help = 'Populates Database.'

    def handle(self, *args, **options):
        print('Populating database...')
        cur_dir = os.path.dirname(__file__)
        file_path = os.path.join(cur_dir, 'products.sql')
        sql = Path(file_path).read_text()

        with connection.cursor() as cursor:
            cursor.execute(sql)
                                                                                                                                        