from django.core.management.base import BaseCommand
from django.db  import connection
from pathlib import Path
import os

class Command(BaseCommand):
    help = 'Populates Database.'

    def handle(self, *args, **options):
        print('Populating database...')
        cur_dir = os.path.dirname(__file__)
        file_path = os.path.join(cur_dir, 'populate_product_data.sql')
        sql_commands = Path(file_path).read_text()
        sql_command_list = sql_commands.split('\n')
        with connection.cursor() as cursor:
            for sql in sql_command_list:
                cursor.execute(sql)
                                                                                                                                        