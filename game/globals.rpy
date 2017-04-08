init -1 python:
    from datetime import date, timedelta

    import alifesim
    from alifesim.player import Player
    from alifesim.name import get_by_name
    from alifesim import ui_helpers
    ui_helpers.show_screen = renpy.show_screen
    from alifesim import playground
    def hidden_imports():
        from alifesim import name, money, basic_stats
    hidden_imports()

default player = Player()
