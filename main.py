from trello import TrelloApi

TRELLO_APP_KEY = "app_key_here"
# TODO: add link on how to get app key
trello = TrelloApi(TRELLO_APP_KEY)
# TODO: is there a shorted expiration?
# print(trello.get_token_url('My App', expires='30days', write_access=True))
# TODO: add suggestion to make backup now

# ---------------

# TODO: add acquisition logic here, for an uninterupted flow
# TODO: also: store (permissions!)
# TODO: shred, delete, ask to revoke at the end
USER_TOKEN = "thing you get from link here"
trello.set_token(USER_TOKEN)

# ---------------

# TODO: add board picker
# cards = trello.boards.get_card_filter(filter="closed", board_id="board_id_here")

# with open("ids_to_purge", "w") as f:
    # for c in cards:
        # f.write(f"{c['id']}\n")

# with open("report", "w") as f:
    # for c in cards:
        # f.write(f"{c['name']}\n")

# TODO: add a pause here, so that the user can read the files and then proceed
# TODO: save the proceed and delete at the end

# ---------------
with open("ids_to_purge") as f:
    raw_ids = f.read()

ids = raw_ids.split("\n")[:-1]

try:
    with open("ptr") as ptr:
        ptr = ptr.read()
except FileNotFoundError:
    ptr = None

if not ptr:
    ptr = ids[0]

# this might be fun to pararelize
pointer_reached = False
skip_count = 0
total = len(ids)
for i, card_id in enumerate(ids):
    if pointer_reached:
        ptr = card_id
        progress = total - skip_count
        if i % 100 == 0:
            print(f"{i} / {progress} = {i / progress * 100:.2f}%")
        trello.cards.delete(card_id)
        with open("ptr", "w") as ptr_f:
            ptr_f.write(ptr)
    else:
        if card_id == ptr:
            print(f"skipped {skip_count}")
            pointer_reached = True
            continue

        skip_count += 1
