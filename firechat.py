from datetime import datetime


class Firechat():

    def __init__(self, firebase_ref):
        self._room_ref = firebase_ref.child('room-metadata')
        self._message_ref = firebase_ref.child('room-messages')
        self._users_online_ref = firebase_ref.child('user-names-online')

    def create_room(self, room_name, room_type='public'):
        new_room_ref = self._room_ref.push()

        room_info = {
            'id': new_room_ref.key,
            'name': room_name,
            'type': room_type,
            'createdAt': datetime.now().timestamp(),
        }

        new_room_ref.set(room_info)

        return new_room_ref.key
