import datetime as dt
import os
from nicegui import app, ui

from counter import CounterGUI
from timed_actions import TimedActionsGUI
from timer import TimerGUI

WELCOME_MARKDOWN = """
# Misc Tools

This is a collection of random things that might be useful for day to day things.
"""


def common_elements():
    menu_items = {
        "Timed Actions": timed_actions,
        "Timer": timer,
        "Counter": counter,
    }
    with ui.header(elevated=True).style("background-color: #3874c8").classes(
        "justify-left"
    ):
        # Button to hide or show the drawer
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
        ui.link("Home", home).classes(replace="text-2xl text-white")

    with ui.left_drawer() as left_drawer:
        ui.link("Home", home).classes(replace="text-2xl text-white")
        ui.separator()
        for label, target in menu_items.items():
            ui.link(label, target).classes(replace="text-lg text-white")


@ui.page("/")
def home():
    common_elements()
    ui.markdown(content=WELCOME_MARKDOWN)


@ui.page("/timed_actions")
def timed_actions():
    common_elements()
    TimedActionsGUI()


@ui.page("/timer")
def timer():
    common_elements()
    TimerGUI()


@ui.page("/counter")
def counter():
    common_elements()
    CounterGUI()


def handle_shutdown():
    print(f"{dt.datetime.now().isoformat()} - Shutdown completed!")


if __name__ == "__main__":
    app.on_shutdown(handle_shutdown)
    ui.run(
        show=False,
        dark=True,
        title="Misc Tools",
        favicon="🛠️",
        storage_secret=os.environ["STORAGE_SECRET"],
        reload=False,
        port=int(os.getenv("PORT", 8080)),
    )
