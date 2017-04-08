label main_menu:
    return

label start:
    menu:
        "test 0":
            call test_0
        "test 1":
            call test_1
        "test 2":
            call test_2
    return

label test_0:
    show screen player
    "...Lets call our player 'player'"
    $ player.name = 'player'
    "..."
    return

label test_1:
    python:
        from alifesim.playground import setup_friends
        setup_friends(player)
    show screen all
    show screen socialize(playground.EatCake)
    "..."
    return

label test_2:
    show screen calendar
    "..."
    return
