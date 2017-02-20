screen player():
    frame:
        vbox:
            text player.name
            text "${}".format(player.money)
            $ stats = alifesim.stat.get_stats(player)
            for stat in stats:
                text "{}: {}".format(stat, stats[stat])
