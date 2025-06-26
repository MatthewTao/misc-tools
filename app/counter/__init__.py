from nicegui import ui


WELCOME_MARKDOWN = """
# Simple Counter

Basic counter, increases count when button is pressed.

Count is lost after server restarts
"""


class CounterGUI:
    def __init__(self):
        self.count = 0

        with ui.right_drawer() as right_drawer:
            ui.markdown(content=WELCOME_MARKDOWN)

        with ui.row().classes("w-full"):
            ui.label("Simple Counter").style("font-size: 200%; font-weight: 600")
            ui.space()  # hahaha feels hacky, try to use some sort of align maybe
            ui.button(on_click=lambda: right_drawer.toggle(), icon="info").props(
                "flat color=white"
            )

        with ui.row().classes("w-full justify-center"):
            with ui.card(align_items="center"):
                ui.input(label="Name")
                self.counter_label = ui.label("0").style(
                    "font-size: 150%; font-weight: 600"
                )

                ui.button("Count +1", on_click=self.increment_count).style(
                    "font-size: 250%"
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
