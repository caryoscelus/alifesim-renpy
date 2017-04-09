init -1 python:
    import datetime
    from datetime import timedelta

    import alifesim
    from alifesim.player import Player
    from alifesim.name import get_by_name
    from alifesim import ui_helpers
    ui_helpers.show_screen = renpy.show_screen
    from alifesim import playground
    from alifesim import plan, job, items, money, date, day, courses
    from alifesim.plan import WeekTime, RealTime
    def hidden_imports():
        from alifesim import name, basic_stats, job
    hidden_imports()

    date.today = datetime.date.today()

default player = Player()
default world = alifesim.entity.world
