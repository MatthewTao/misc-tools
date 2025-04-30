from nicegui import ui


TIMED_ACTIONS_MARKDOWN = """
# Timed Actions

This is a way to set timers for various timed actions, 
rather than having to manage multiple alarms or timers.
"""


class TimedActionsGUI:
    def __init__(self):
        ui.markdown(content=TIMED_ACTIONS_MARKDOWN)
        ui.label("Maybe a way to set various timers in one spot")
