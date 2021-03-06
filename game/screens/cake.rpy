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

screen cake():
    modal True
    frame:
        xalign 0.5 yalign 0.5
        has vbox
        text "Cake eaten!"
        textbutton "Ok" action Hide('cake')

screen cake_special(person):
    modal True
    frame:
        xalign 0.5 yalign 0.5
        has vbox
        text "{} got poisoned by the cake O_o".format(person.name)
        textbutton "Close" action Hide('cake_special')
