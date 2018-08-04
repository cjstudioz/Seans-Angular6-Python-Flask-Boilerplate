from app import app
from flask import jsonify, abort, request
from datetime import datetime, timedelta

cats = [
    {
        'id': 1,
        'name': u'Cosmo',
        'genus': u'felis',
        'isHungry': True,
        'lastFedDate': datetime.today() - timedelta(1)  #yesterday
    },
    {
        'id': 2,
        'name': u'Emmy',
        'genus': u'felis',
        'isHungry': True,
        'lastFedDate': datetime.today() - timedelta(1)  #yesterday
    }
]

@app.route('/cats', methods=['GET'])
def get_cats():
    return jsonify({'cats': cats})


@app.route('/cats/<int:id>', methods=['GET'])
def get_cat(id):
    cat = [cat for cat in cats if cat['id'] == id]
    if len(cat) == 0:
        abort(404)
    return jsonify({'cat': cat[0]})


@app.route('/cats', methods=['POST'])
def create_cat():
    if request.get_json():
        data = request.get_json(force=True)
        if data['cat']:
            if type(data['cat']['name']) == unicode and type(data['cat']['genus']) == unicode and type(data['cat']['isHungry']) == bool:
                if len(data['cat']['name']) >= 3 and len(data['cat']['name']) <= 20:
                    cat = {
                        'id': cats[-1]['id'] + 1,
                        'name': data['cat']['name'],
                        'genus': data['cat']['genus'],
                        'isHungry': bool(data['cat']['isHungry']),
                        'lastFedDate': data['cat']['lastFedDate']
                        or datetime.now()
                    }
                    cats.append(cat)
                    return jsonify({'cat': cat}), 201
                else:
                    abort(400)
            else:
                abort(400)
        else:
            abort(400)
    else:
        abort(400)


@app.route('/cats/<int:id>', methods=['PUT'])
def update_cat(id):
    cat = [cat for cat in cats if cat['id'] == id]
    if len(cat) == 0:
        abort(404)
    if request.get_json():
        data = request.get_json(force=True)
        if data['cat']:
            if type(data['cat']['name']) == unicode and type(data['cat']['genus']) == unicode and type(data['cat']['isHungry']) == bool:
                cat[0]['name'] = data['cat']['name']
                cat[0]['genus'] = data['cat']['genus']
                cat[0]['isHungry'] = data['cat']['isHungry']
                cat[0]['lastFedDate'] = data['cat']['lastFedDate'] or datetime.now()
                return jsonify({'cat': cat[0]})
            else:
                abort(400)
        else:
            abort(400)
    else:
        abort(400)


@app.route('/cats/<int:id>', methods=['DELETE'])
def delete_cat(id):
    cat = [cat for cat in cats if cat['id'] == id]
    if len(cat) == 0:
        abort(404)
    cats.remove(cat[0])
    return jsonify({'result': True})
