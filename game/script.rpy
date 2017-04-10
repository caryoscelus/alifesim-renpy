label main_menu:
    return

define demo = True

label start:
    if demo:
        call test_6
        return
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
        "test 5 (top panel)":
            call test_5
        "test 6 (hack together)":
            call test_6
        "test 7 (courses)":
            call test_7
    return

label test_0:
    show screen player
    "...Lets call our player 'player'"
    $ player.name = 'player'
    "..."
    return

label test_1:
    $ playground.setup_friends(player)
    show screen player_and_friends
    $ prepare_socialize(playground.EatCake)
    "..."
    return

label test_2:
    $ playground.get_a_job(player)
    show screen calendar
    "..."
    return

label test_3:
    $ playground.setup_jobs()
    show screen job_market()
    "..."
    return

label test_4:
    python:
        playground.setup_items()
        player.money = 300
    show screen item_market
    show screen items
    "..."
    return

label test_5:
    $ playground.setup_all(player)
    show screen top_panel
    "..."
    return

screen dummy:
    xalign 0.0

label test_6:
    $ playground.setup_all(player)
    show screen next_day
    show screen plans
    show screen calendar
    show screen player_and_friends
    call screen top_panel
    return

label test_7:
    $ playground.setup_courses()
    show screen courses
    "..."
    return
