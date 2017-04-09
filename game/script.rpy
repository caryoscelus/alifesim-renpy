label main_menu:
    return

label start:
    menu:
        "test 0":
            call test_0
        "test 1 (friend select)":
            call test_1
        "test 2 (calendar)":
            call test_2
        "test 3 (job market)":
            call test_3
        "test 4 (item market)":
            call test_4
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
    hide screen all
    hide screen socialize
    "..."
    show screen all
    "..."
    return

label test_2:
    python:
        from alifesim.playground import get_a_job
        get_a_job(player)
    show screen calendar
    "..."
    return

label test_3:
    python:
        from alifesim.playground import setup_jobs
        setup_jobs()
    show screen job_market()
    "..."
    return

label test_4:
    python:
        from alifesim.playground import setup_items
        setup_items()
    show screen item_market
    "..."
    return
