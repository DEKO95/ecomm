import io

from flask import jsonify, send_file
from requests_toolbelt import MultipartEncoder

from server import app
from server.models import Item, ItemPicture

@app.route('/api/item/<int:id>')
def item_endpoint(id):

    item = Item.query.filter_by(id=id).first()
    pic = item.pictures.first()
    m = MultipartEncoder(fields={'markdown': str(item.to_dict()),
                                 'files': (pic.filename, pic.file)
                                 })

    return (m.to_string(), {'Content-Type': m.content_type})


@app.route('/api/picture/<int:id>')
def picture_endpoint(id):

    pic = ItemPicture.query.filter_by(id=id).first()
    
    return send_file(io.BytesIO(pic.file),
                     attachment_filename=pic.filename
                     )