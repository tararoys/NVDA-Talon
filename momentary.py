import os
import platform
import pprint
import re
from itertools import islice
from typing import Union

from talon import Module, actions, app, clip, registry, scope, speech_system, ui
from talon.grammar import Phrase

mod = Module()

import csv
from pathlib import Path

from talon import resource

# NOTE: This method requires this module to be one folder below the top-level
#   knausj folder.
SETTINGS_DIR = Path(__file__).parents[1] / "settings"

if not SETTINGS_DIR.is_dir():
    os.mkdir(SETTINGS_DIR)

@mod.action_class
class Actions:
    def talon_locate_rule(phrase: Union[str, Phrase]):
        """locates the file, rule, and line number where a particular voice command is defined, and copies it to the clipboard so NVDA can speak it"""
        print("**** Simulated Phrse **** ")
        location = speech_system._sim(str(phrase))
        print(location)
        filepath=location.partition("path: ")[2].split('\n')[0]
        print(filepath)

        rule_to_locate = location.partition("rule: \"")[2].split("\"")[0]
        number = ""
        with open(filepath) as myFile:
            for num, line in enumerate(myFile, 1):
                if rule_to_locate in line: 
                    number = num
                    print('found at line', num)
        complete_location = location + "\n\t line number " + str(number)
        print(complete_location)
        print("*************************")
        clip.set_text(complete_location) # sets the result to the clipboard
        actions.sleep("10ms")
        actions.key("insert:down c insert:up")   #makes nvda read the clipboard so that you know the file name, the written rule, and the line number the rule is on so that you can find it easily.       

#actions.path.talon_user()

def start_talon_in_sleep_mode():
    """when talon starts up, automatically puts it into sleep mode, so that NVDA screen reader will not inadvertantly give it orders as NVDA reads things out while Talon is listening"""
    actions.speech.disable()

app.register("ready", start_talon_in_sleep_mode)
