import io

from flask import jsonify, send_file
from requests_toolbelt import MultipartEncoder

from server.api import bp
from server.models import Item, ItemPicture

@bp.route('/item/<int:id>')
def item_endpoint(id):

    item = Item.query.filter_by(id=id).first()
    pic = item.pictures.first()
    m = MultipartEncoder(fields={'markdown': str(item.to_dict()),
                                 'files': (pic.filename, pic.file)
                                 })

    return (m.to_string(), {'Content-Type': m.content_type})


@bp.route('/picture/<int:id>')
def picture_endpoint(id):

    pic = ItemPicture.query.filter_by(id=id).first()
    
    return send_file(io.BytesIO(pic.file),
                     attachment_filename=pic.filename
                     )