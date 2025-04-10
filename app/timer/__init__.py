from nicegui import ui
import time


WELCOME_MARKDOWN = """
# Simple Timer

Basic timer with no pause or resume.

Time is lost after server restarts
"""


class TimerGUI:
    def __init__(self):
        ui.markdown(content=WELCOME_MARKDOWN)
        self.start_time = 0
        self.end_time = 0

        with ui.card(align_items="center").classes("fixed-center"):
            ui.input(label="Name")
            self.timer = ui.timer(
                0.1, lambda: label.set_text(self.format_time()), active=False
            )
            self.timer_label = label = ui.label("0.00").style(
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
        return f"{time.time() - self.start_time:.2f} seconds"
