label main_menu:
    return

label start:
    menu:
        "test 0":
            call test_0
        "test 1":
            call test_1
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
