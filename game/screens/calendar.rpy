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
    DAYS_IN_WEEK = 7
    DISPLAY_WEEKS = 2

screen calendar:
    default today = date.today()
    default date_start = today-timedelta(today.weekday())
    frame:
        has grid DAYS_IN_WEEK DISPLAY_WEEKS
        for week in range(DISPLAY_WEEKS):
            for day in range(DAYS_IN_WEEK):
                $ day = date_start+timedelta(week*7+day)
                frame:
                    text "{}".format(day.day) bold (day == today)
