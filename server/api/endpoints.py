import io

from flask import jsonify, send_file, abort, request
from flask_restful import Resource
from requests_toolbelt import MultipartEncoder
from werkzeug.utils import secure_filename

from server import auth, db
from server.api import bp
from server.models import Item, ItemPicture



IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in IMAGE_EXTENSIONS


class ItemResource(Resource):
 
    def get(self, id):

        item = Item.query.get_or_404(id)
        
        return item.to_dict()
    
    
    @auth.login_required(role=['admin'])
    def delete(self, id):
        item = Item.query.get_or_404(id)
        for pic in item.pictures:
            db.session.delete(pic)
        db.session.delete(item)
        db.session.commit()
        return None, 204
    
    
    @auth.login_required(role=['moderator'])
    def put(self, id):
        pass


@bp.route('/items', methods=['POST'])
@auth.login_required(role=['admin'])
def add_item():

    pass


@bp.route('/picture/<int:id>')
def picture_endpoint(id):

    pic = ItemPicture.query.filter_by(id=id).first()
    
    return send_file(io.BytesIO(pic.file),
                     attachment_filename=pic.filename
                     )