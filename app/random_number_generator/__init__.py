from nicegui import ui
import random
import time


WELCOME_MARKDOWN = """
# Random Number Generator

Basic Random Number Generator.

Enter in a min and max amount and click Generate.
Default to min of 1 and max of 6.
"""


class RandomNumberGeneratorGUI:
    def __init__(self):
        with ui.right_drawer() as right_drawer:
            ui.markdown(content=WELCOME_MARKDOWN)

        with ui.row().classes("w-full"):
            ui.label("Random Number Generator").style(
                "font-size: 200%; font-weight: 600"
            )
            ui.space()
            ui.button(on_click=lambda: right_drawer.toggle(), icon="info").props(
                "flat color=white"
            )

        with ui.row().classes("w-full justify-center"):
            with ui.card(align_items="center"):
                with ui.row():
                    self.min_input = ui.number(label="Min", value=1).classes("w-32")
                    self.max_input = ui.number(label="Max", value=6).classes("w-32")

                self.generate_button = ui.button(
                    "Generate", on_click=self.generate_number
                )
                self.result_label = ui.label("Result will appear here").style(
                    "font-size: 150%; font-weight: 600"
                )
                ui.separator()
                ui.button("Reset", on_click=self.reset).props("outline")

    def generate_number(self):
        try:
            min_val = self.min_input.value
            max_val = self.max_input.value

            # Validate inputs
            if min_val is None or max_val is None:
                self.result_label.set_text("Please enter both min and max values")
                return

            if not isinstance(min_val, (int, float)) or not isinstance(
                max_val, (int, float)
            ):
                self.result_label.set_text("Please enter valid numbers")
                return

            if min_val > max_val:
                self.result_label.set_text("Min value cannot be greater than max value")
                return

            # Generate random integer
            result = random.randint(int(min_val), int(max_val))

            self.result_label.set_text(str(result))
        except Exception as e:
            self.result_label.set_text(f"Error generating number: {str(e)}")

    def reset(self):
        self.min_input.value = 1
        self.max_input.value = 6
        self.result_label.set_text("Result will appear here")
