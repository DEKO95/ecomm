from werkzeug.security import generate_password_hash, check_password_hash

from server import auth
from server.models import User, Moderator
from server.api import bp


@auth.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return user.id

@auth.get_user_roles
def get_user_roles(user_id):
    m = Moderator.query.filter_by(user_id=user_id).first()
    if not m: # TODO rewrite
        return 'user'
    if m.is_admin:
        return 'admin'
    return 'moderator'

@bp.route('/')
@auth.login_required(role=['admin'])
def login():
    return "Hello, {}!".format(auth.current_user())