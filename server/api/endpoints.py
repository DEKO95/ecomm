import io

from flask import jsonify, send_file, request, Response
from flask_restful import Resource, abort, reqparse
from requests_toolbelt import MultipartEncoder
from werkzeug.utils import secure_filename

from server import auth, db
from server.api import bp
from server.models import Item, ItemPicture


IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in IMAGE_EXTENSIONS


def load_item_images_from_multipart(id):
    for files in request.files.listvalues():
        for file in files:
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                pic = ItemPicture(item_id=id,
                                    filename=filename,
                                    file=file.read()
                                    )
                db.session.add(pic)


item_parser = reqparse.RequestParser()
item_parser.add_argument('price', type=float, store_missing=False)
item_parser.add_argument('title', store_missing=False)
item_parser.add_argument('description', store_missing=False)
item_parser.add_argument('is_available', type=bool, store_missing=False)
item_parser.add_argument('category_id', type=int, store_missing=False)


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
        return None, 204  # 204 - NO CONTENT
    
    @auth.login_required(role=['moderator','admin'])
    def put(self, id):
        '''
        Takes request with `multipart/form-data` Content-Type
        where the parts have name of Item field and contains corresponding value
        (see models.Item)
        
        All remaining parts can contain a picture in allowed extension
        
        If successful returns json of modified object and status code 200
        '''
        item = Item.query.filter_by(id=id)
        if not item:
            abort(404)

        item.update(item_parser.parse_args())
        
        item = item.first()
        load_item_images_from_multipart(item.id)
        
        db.session.commit()
        
        return item.to_dict()


class AllItemsResource(Resource):
    
    @auth.login_required(role=['admin'])
    def post(self):
        '''
        Takes request with `multipart/form-data` Content-Type
        where the parts have name of Item field and contains corresponding value
        (see models.Item)
        
        All remaining parts can contain a picture in allowed extension
        
        If successful returns json of new object and status code 201
        '''
        item = Item(**item_parser.parse_args())
        db.session.add(item)
        db.session.commit()  # for some reason item.id is None before commit
        
        load_item_images_from_multipart(item.id)
        db.session.commit()
        
        return item.to_dict(), 201  # 201 - CREATED
    
    def get(self):
        # pagination
        page = request.args.get('page', 1, type=int)
        per_page = min(request.args.get('per_page', 12, type=int), 100)
        data = Item.to_collection_dict(Item.query, page, per_page, 'api.allitemsresource')
        return data


class PictureResource(Resource):
    
    def get(self, id):
        pic = ItemPicture.query.get_or_404(id)
        return send_file(io.BytesIO(pic.file),
                        attachment_filename=pic.filename
                        )

    @auth.login_required(role=['admin'])
    def delete(self, id):
        pic = ItemPicture.query.get_or_404(id)
        db.session.delete(pic)
        db.session.commit()
        return None, 204  # 204 - NO CONTENT
