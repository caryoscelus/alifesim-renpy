label main_menu:
    return

label start:
    menu:
        "test 0":
            call test_0
    return

label test_0:
    show screen player
    "...Lets call our player 'player'"
    $ player.name = 'player'
    "..."
    return
