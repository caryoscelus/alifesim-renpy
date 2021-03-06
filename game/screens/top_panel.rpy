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

## Top panel: switch between active screens

init python:
    def toggle_screen(scr):
        if renpy.get_screen(scr):
            renpy.hide_screen(scr)
        else:
            renpy.show_screen(scr)

screen top_panel:
    frame:
        xalign 0.5 yalign 0.0
        has vbox
        hbox:
            for scr in ['player_and_friends', 'items', 'item_market', 'job_market', 'courses']:
                textbutton scr action Function(toggle_screen, scr)
        hbox:
            for scr in ['calendar', 'plans', 'social_activities', 'single_activities']:
                textbutton scr action Function(toggle_screen, scr)
