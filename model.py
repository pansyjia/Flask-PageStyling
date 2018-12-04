import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
idnum = 0

def init():
    global entries
    try:

        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
    except:
        print('Couldn\'t open', GUESTBOOK_ENTRIES_FILE)
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, idnum
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")

    entry = {"author": name, "text": text, "timestamp": time_string, "id":idnum} #create a new attribute
    idnum += 1
    # pritn(idnum)
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")


def delete_entry(idnum):
    global entries, GUESTBOOK_ENTRIES_FILE
    for ele in entries:
        if int(idnum) == ele["id"]:
            try:
                entries.remove(ele)
            except:
                pass
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_str = json.dumps(entries)
        f.write(dump_str)
        f.close()
    except:
        print("ERROR! Please try again!" )

    print(entries)
