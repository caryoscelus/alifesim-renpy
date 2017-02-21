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

screen select_friends(min_, max_):
    default selected = ui_helpers.new_selection(min_, max_)
    frame:
        has vbox
        for i in range(max_):
            frame:
                if i < len(selected):
                    text selected[i].name
                elif i < min_:
                    text "<required>"
                else:
                    text "<empty>"
        textbutton "ok":
            sensitive selected.ready()
            action Function(ui_helpers.process_selection)

screen socialize(activity):
    default result = ui_helpers.set_selection_processor(activity.make_and_run)
    use select_friends(activity.people_min, activity.people_max)
