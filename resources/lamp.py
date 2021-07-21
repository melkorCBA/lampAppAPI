
from flask import Blueprint, Response, request
from data.models import Lamp
from werkzeug.datastructures import ImmutableMultiDict
from pusherHook.hook import initlizePusherClinet

lamps = Blueprint('lamps', __name__)
pusher_client = initlizePusherClinet()
# GET lamps


@lamps.route('/lamps')
def get_lamps():
    lamps = Lamp.objects().to_json()
    return Response(lamps, mimetype="application/json", status=200)

# GET lamp


@lamps.route('/lamps/<id>')
def get_lamp(id):
    lamp = Lamp.objects.get(id=id).to_json()
    return Response(lamp, mimetype="application/json", status=200)


# POST lamp
@lamps.route('/lamps', methods=['POST'])
def add_lamp():
    newLamp = request.get_json()
    try:
        value = newLamp['priority']
    except KeyError:
        lampsCount = Lamp.objects().count()
        newLamp['priority'] = lampsCount + 1
        pass

    lamp = Lamp(**newLamp).save()
    id = lamp.id
    pusher_client.trigger('lamps', 'update', {
                          'type': '1', 'desc': 'new Lamp added'})
    return Response({'id': str(id)}, mimetype="application/json", status=200)


# PUT lamp
@lamps.route('/lamps/<id>', methods=['PUT'])
def update_lamp(id):
    EditingLamp = request.get_json()
    Lamp.objects.get(id=id).update(**EditingLamp)
    UpdatedLamp = Lamp.objects.get(id=id).to_json()
    pusher_client.trigger('lamps', 'update', {
                          'type': '2', 'desc': 'Lamp data updated'})
    return Response(UpdatedLamp, mimetype="application/json", status=200)


# DELETE lamp
@lamps.route('/lamps/<id>', methods=['DELETE'])
def delete_lamp(id):
    deletedLamp = Lamp.objects.get(id=id).delete()
    return Response(deletedLamp, mimetype="application/json", status=200)
