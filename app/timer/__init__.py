from nicegui import ui
import time


WELCOME_MARKDOWN = """
# Simple Timer

Basic timer with no pause or resume.

Time is lost after page is refreshed or when the server restarts
"""


class TimerGUI:
    def __init__(self):
        self.start_time = 0

        with ui.right_drawer() as right_drawer:
            ui.markdown(content=WELCOME_MARKDOWN)

        with ui.row().classes("w-full"):
            ui.label("Simple Timer").style("font-size: 200%; font-weight: 600")
            ui.space()  # hahaha feels hacky, try to use some sort of align maybe
            ui.button(on_click=lambda: right_drawer.toggle(), icon='info').props('flat color=white')

        with ui.row().classes("w-full justify-center"):
            with ui.card(align_items="center"):
                ui.input(label="Name")
                self.timer = ui.timer(
                    0.1, lambda: label.set_text(self.format_time()), active=False
                )
                self.timer_label = label = ui.label("00:00:00.00").style(
                    "font-size: 200%; font-weight: 600"
                )

                with ui.row():
                    self.start_button = ui.button("Start", on_click=self.start)
                    self.stop_button = ui.button("Stop", on_click=self.stop)

                self.stop_button.disable()

    def start(self):
        self.start_time = time.time()
        self.timer.active = True
        self.start_button.disable()
        self.stop_button.enable()

    def stop(self):
        self.timer.active = False
        self.start_button.enable()
        self.stop_button.disable()

    def format_time(self):
        seconds_past = time.time() - self.start_time

        hours = seconds_past // 3600
        remainder = seconds_past - hours * 3600

        minutes = remainder // 60
        remainder = remainder - minutes * 60

        seconds = remainder
        return f"{int(hours):02}:{int(minutes):02}:{seconds:05.2f}"
