from nicegui import ui


WELCOME_MARKDOWN = """
# Simple Counter

Basic counter, increases count when button is pressed.

Count is lost after server restarts
"""


class CounterGUI:
    def __init__(self):
        ui.markdown(content=WELCOME_MARKDOWN)
        self.count = 0

        with ui.card(align_items="center").classes("fixed-center"):
            ui.input(label="Name")
            self.counter_label = ui.label("0").style(
                "font-size: 200%; font-weight: 600"
            )

            ui.button("Count +1", on_click=self.increment_count).style(
                "font-size: 300%"
            )
            ui.button("Opps", on_click=self.reduce_count).props("outline")
            ui.button("Reset Counter", on_click=self.reset).props("outline")

    def update_label(self):
        self.counter_label.set_text(str(self.count))

    def increment_count(self):
        self.count += 1
        self.update_label()

    def reduce_count(self):
        self.count -= 1
        self.update_label()

    def reset(self):
        self.count = 0
        self.update_label()
