from flask import request
from app import app, db
from models import Advertisement


@app.route('/')
def home():
    return 'Hello World'


@app.route('/advertisement', methods=['POST'])
def post_advert():
    body = request.json
    advertisement = Advertisement(title=body.get("title"),
                           description=body.get("description"),
                           owner=body.get("owner"))
    db.session.add(advertisement)
    db.session.commit()
    return {'status': 201}


@app.route('/advertisement/<int:get_id>', methods=['GET'])
def get_advert(get_id):
    advertisement = Advertisement.query.filter_by(id=get_id).first_or_404()
    return {"id": advertisement.id,
            "title": advertisement.title,
            "description": advertisement.description,
            "created_at": advertisement.created_at,
            "owner": advertisement.owner
            }, {'status': 201}


@app.route('/advertisement/<int:patch_id>', methods=['PATCH'])
def patch_advert(patch_id):
    title = request.json
    Advertisement.query.filter_by(id=patch_id).update(title)
    db.session.commit()
    advert_new = Advertisement.query.filter_by(id=patch_id).first_or_404()
    return {"id": advert_new.id,
            "title": advert_new.title,
            "description": advert_new.description,
            "created_at": advert_new.created_at,
            "owner": advert_new.owner
            }, {'status': 201}


@app.route('/advertisement/<int:del_id>', methods=['DELETE'])
def delete_advert(del_id):
    advertisement = Advertisement.query.filter_by(id=del_id).first_or_404()
    db.session.delete(advertisement)
    db.session.commit()
    return {'status': 204}
