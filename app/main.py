import datetime as dt
import os
from nicegui import app, ui

from timed_actions import TimedActionsGUI


WELCOME_MARKDOWN = """
# Misc Tools

This is a collection of random things that might be useful for day to day things.
"""
TIMED_ACTIONS_MARKDOWN = """
# Timed Actions

This is a way to set timers for various timed actions, 
rather than having to manage multiple alarms or timers.
"""


@ui.page("/")
def home():
    ui.markdown(content=WELCOME_MARKDOWN)
    ui.link('Timed actions', timed_actions)


@ui.page("/timed_actions")
def timed_actions():
    ui.markdown(content=TIMED_ACTIONS_MARKDOWN)
    timed_actions_gui = TimedActionsGUI()
    ui.link("Home", home)


def handle_shutdown():
    print(f'{dt.datetime.now().isoformat()} - Shutdown completed!')


app.on_shutdown(handle_shutdown)
ui.run(show=False, dark=True, title="Misc Tools", storage_secret=os.environ['STORAGE_SECRET'], reload=False)
