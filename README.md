## Firechat (Python)
A port of Google's Firechat Javascript SDK to Python

### Why?
This project was started due to the need to do Firechat's functionality on the backend.
It will be useful in cases wherein the chat will be integrated with a business data model.
Eg: Automatically creating chatrooms for every department/group that will be created on the company's app.

### What functionalities are available
1. Creating rooms
2. Getting list of rooms

### HOWTO
This library is supposed to be used in conjunction with [Firebase Python Admin SDK](https://github.com/firebase/firebase-admin-python)
```
from firebase_admin import db
from firechat import Firechat


chat_ref = db.reference('chat')
firechat = Firechat(chat_ref)

# create_room('room name', 'room type')
# Room types: public, private
orange_room = firechat.create_room('orange club', 'private')

# get_room_list
firechat_room_list = firechat.get_room_list()
```
