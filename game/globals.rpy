init -1 python:
    import alifesim
    from alifesim.player import Player
    def hidden_imports():
        from alifesim import name, money, basic_stats
    hidden_imports()

default player = Player()
