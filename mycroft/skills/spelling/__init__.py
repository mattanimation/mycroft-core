# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder
from os.path import dirname, join

from mycroft.skills.core import MycroftSkill

__author__ = 'seanfitz'


# TODO - Localization
class SpellingSkill(MycroftSkill):
    def __init__(self):
        super(SpellingSkill, self).__init__(name="SpellingSkill")

    def initialize(self):
        self.load_vocab_files(join(dirname(__file__), 'vocab', self.lang))
        self.load_regex_files(join(dirname(__file__), 'regex', self.lang))

        intent = IntentBuilder("SpellingIntent").require(
            "SpellingKeyword").require("Word").build()
        self.register_intent(intent, self.handle_intent)

    def handle_intent(self, message):
        word = message.data.get("Word")
        spelled_word = ', '.join(word).lower()
        self.speak(spelled_word)

    def stop(self):
        pass


def create_skill():
    return SpellingSkill()
