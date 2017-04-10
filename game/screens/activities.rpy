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

screen social_activities:
    frame:
        has vbox
        for activity in socialize.all():
            textbutton "{}".format(activity.__name__) action Function(prepare_socialize, activity)

screen socialize(activity):
    frame:
        has vbox
        text "{}".format(activity.__name__)
        use select_friends()

init python:
    def socialize_processor(activity):
        def f(*selection):
            renpy.hide_screen('socialize')
            activity.make_and_run(*selection)
        return f
    def prepare_socialize(activity):
        selection_manager.set_processor(socialize_processor(activity))
        selection_manager.new(activity.people_min, activity.people_max)
        renpy.show_screen('socialize', activity)
