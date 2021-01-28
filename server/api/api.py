import io

from flask import jsonify, send_file
from requests_toolbelt import MultipartEncoder

from server.api import bp
from server.models import Item, ItemPicture

@bp.route('/item/<int:id>')
def item_endpoint(id):

    item = Item.query.filter_by(id=id).first()
    
    return item.to_dict()


@bp.route('/picture/<int:id>')
def picture_endpoint(id):

    pic = ItemPicture.query.filter_by(id=id).first()
    
    return send_file(io.BytesIO(pic.file),
                     attachment_filename=pic.filename
                     )