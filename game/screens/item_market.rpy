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

init python:
    ## TODO: move to core
    def buy_item(item):
        money.spend_money(player, item.price, lambda: items.give(player, item))

screen item_market():
    frame:
        has vbox
        for item in items.all():
            frame:
                has vbox
                text "{} ({})".format(item.name, item.price)
                textbutton "buy" action Function(buy_item, item)
