#######################################################################################################################
# VARIABLES
#######################################################################################################################

nickname = ''

#######################################################################################################################
# FUNCTIONS
#######################################################################################################################


def welcome_dialog():
    global nickname

    print("\nWelcome!")
    input_nickname = str(input("Nickname: "))
    nickname = input_nickname
    print(f"Good Luck playing the best Game in the world {input_nickname} !")

    return nickname