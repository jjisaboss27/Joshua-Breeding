board = True
cap_on = False
ink = True




def use_marker(board, cap_on, ink):
    if not board:
        print("No board in area.")
    elif cap_on:
        print("The cap is still on.")
    elif not ink:
        print("No ink left.")
    else:
        return use_marker and print("You used the marker.")

use_marker(True, False, True)
