import os
from app import create_app,db
from app.models import User,Alticle
from flask.ext.script import Manager,Shell
from flask.ext.migrate import Migrate,MigrateCommand
app = create_app(os.getenv('Flask_config') or 'default')
manager = Manager(app)
migrate = Migrate(app,db)
def make_shell_context():
    return dict(app=app,db=db,User=User,Alticle=Alticle)
manager.add_command('shell',Shell(make_shell_context()))
manager.add_command('db',MigrateCommand)
@manager.command
def deploy():
    """Run deployment tasks."""
    from flask.ext.migrate import upgrade
    from app.models import Alticle, User
    db.create_all()
    # migrate database to latest revision
    upgrade()




if __name__ == '__main__':
    manager.run()