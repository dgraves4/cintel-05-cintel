from shiny import reactive, render
from shiny.express import ui
import random
from datetime import datetime
from faicons import icon_svg

# Set a constant UPDATE INTERVAL for all live data
UPDATE_INTERVAL_SECS: int = 1

# Initialize a REACTIVE CALC to get the latest data and display it
@reactive.calc()
def reactive_calc_combined():
    # Invalidate this calculation every UPDATE_INTERVAL_SECS to trigger updates
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)

    # Data generation logic: Get random temperature between -18 and -16 C, rounded to 1 decimal place
    temp = round(random.uniform(-18, -16), 1)

    # Get the current timestamp and format it
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    latest_dictionary_entry = {"temp": temp, "timestamp": timestamp}

    # Return the latest data
    return latest_dictionary_entry

# Define the page options: title and fillable width
ui.page_opts(title="PyShiny Express: Live Data (Basic)", fillable=True)

# Define the sidebar with relevant information
with ui.sidebar(open="open"):
    ui.h2("Antarctic Explorer", class_="text-center")
    ui.p("A demonstration of real-time temperature readings in Antarctica.", class_="text-center")

# Display current temperature
ui.h2("Current Temperature")

@render.text
def display_temp():
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['temp']} C"

ui.p("warmer than usual")
icon_svg("snowflake")  # snowflake icon
ui.hr()

# Display current date and time with a clock icon
ui.h2("Current Date and Time")
icon_svg("clock") # clock icon

@render.text
def display_time():
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['timestamp']}"