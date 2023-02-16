# This should be the general config for the tradebot
# Client.txt will be used to check for incoming trades
# Wether or not this works with Korean messages isn't known atm
# 

resolution_x = 800 # This could be anything, as we we should get offset as a percentage of screen resolution
resolution_y = 600

trade_msg = "Hi, I would like to buy your" # This is the incoming message from the trade partner

give_me_msg = "I'm gunna give you the goods" # We will use this to supply our bot with items

client = "C:/Program Files (x86)/Grinding Gear Games/Path of Exile/logs/Client.txt"

inventory_offset = [0.5, 0.5] # Top left-most cell of the inventory [0.6625, 0.5486]

trade_window_offset = [0.5, 0.5] # Top left-most cell of party member's trade [0.2470, 0.1910]

stash_offset = [0.5, 0,5] # Top left-most cell of Stash grid

stash_tab_offset = [0.5, 0.5] # Top left-most cell of tabbed list [0.0100, 0.1195]

