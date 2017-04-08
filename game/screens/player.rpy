##
##  Copyright (C) 2017 caryoscelus
##
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.
##

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
            text "{}: {}".format(friend.name, friend.satiation)
            textbutton "Select":
                sensitive ui_helpers.can_select()
                action Function(ui_helpers.select, friend)

screen friends():
    frame:
        vbox:
            for name in player.friends:
                use friend(name)

screen all():
    hbox:
        xalign 1.0
        use friends
        use player
