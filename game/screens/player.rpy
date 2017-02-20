screen player():
    frame:
        vbox:
            text player.name
            text "${}".format(player.money)
            $ stats = alifesim.stat.get_stats(player)
            for stat in stats:
                text "{}: {}".format(stat, stats[stat])

screen friend(name):
    default friend = get_by_name(name)
    frame:
        vbox:
            text friend.name

screen friends():
    frame:
        vbox:
            for name in player.friends:
                use friend(name)

screen all():
    hbox:
        use friends
        use player
