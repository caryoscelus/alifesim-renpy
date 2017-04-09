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
    def toggle_course(course):
        if course.name in player.courses:
            player.courses.remove(course.name)
        else:
            player.courses.add(course.name)

screen courses():
    $ clist = courses.all()
    frame:
        has grid 2 len(clist)+1
        text "Courses"
        text ""
        for course in clist:
            text course.name
            textbutton "({})".format('x' if course.name in player.courses else ' ') action Function(toggle_course, course)
