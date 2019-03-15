from app import app
from flask import jsonify, abort, request
from datetime import datetime, timedelta

cats = [ #QUESTOIN: why is cats a list instead of a dict? can you explain the lookup by ID performance cost (O(m) notation) of a dict lookup vs a list lookup?
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
# QUESTOIN: why 4 nested if statements if all the <else> conditions do the same abort(400)?

@app.route('/cats/<int:id>', methods=['PUT'])
def update_cat(id):
    cat = [cat for cat in cats if cat['id'] == id] #QUESTOIN: this 3 line pattern seems to repeat quite a bit, what does htat suggest to you? what is hte O(n) cost of this lookup if cats were a ver ylong list of a million elements e.g.
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
# QUESTOIN: again: why 3 nested if statements if all the <else> conditions do the same abort(400)?

@app.route('/cats/<int:id>', methods=['DELETE'])
def delete_cat(id):
    cat = [cat for cat in cats if cat['id'] == id]
    if len(cat) == 0:
        abort(404)
    cats.remove(cat[0]) #Question: what happens if there are 2 cats with the same id but different properties? if cats were a database table what built in primitives could we use to protect against these?
    return jsonify({'result': True})
