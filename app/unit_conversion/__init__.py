from nicegui import ui
import time


WELCOME_MARKDOWN = """
# Unit Conversions

Small tool to convert between measurement units
"""

TSP_TO_ML = 4.929
TBS_TO_ML = 14.787


class UnitConversionGUI:
    def __init__(self):
        ui.markdown(content=WELCOME_MARKDOWN)

        with ui.expansion('Temperature').classes('w-full'):
            self._input_temperature = ui.number("Temperature in °F", on_change=self._calculate_temperature)
            self._temperature_celsius = ui.label('Input a Temperature above')

        with ui.expansion('Volume').classes('w-full'):
            ui.label('inside the expansion')

        with ui.expansion('Weight').classes('w-full'):
            ui.label('inside the expansion')

        with ui.expansion('Cooking').classes('w-full'):
            self._cooking_unit = ui.select(label="Unit", options=["cup", "tbs", "tsp"])
            self._cooking_input = ui.number("Value", on_change=self._calculate_cooking_unit)
            self._cooking_label = ui.label('inside the expansion')

    def _calculate_temperature(self):
        temp_f = self._input_temperature.value
        if temp_f and isinstance(temp_f, (int, float)):
            temp_c = (temp_f - 32) * 5 / 9
            self._temperature_celsius.set_text(f"Temperature: {round(temp_c, 1)}°C")

    def _calculate_cooking_unit(self):
        input_value = self._cooking_input.value
        input_unit = self._cooking_unit.value
        if input_unit == "tsp":
            output_value = input_value * TSP_TO_ML
        elif input_unit == "tbs":
            output_value = input_value * TBS_TO_ML
        else:
            output_value = None

        if output_value:
            self._cooking_label.set_text(f"{input_value} {input_unit} is {round(output_value, 1)} mL")
