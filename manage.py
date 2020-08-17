from mysite import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app('develop')
manage = Manager(app)

Migrate(app, db)
manage.add_command('migrate', MigrateCommand)

if __name__ == '__main__':
    manage.run()
