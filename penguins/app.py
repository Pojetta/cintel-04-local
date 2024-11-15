from shiny import reactive
import plotly.express as px
from palmerpenguins import load_penguins
from shiny.express import input, ui, render
from shinywidgets import render_widget, render_plotly
import seaborn as sns

# Load the penguins dataset
penguins = load_penguins()

# Define a color map to fix specific colors for each species
color_map = {
    "Adelie": "#C964CF",  
    "Gentoo": "#008C95",  
    "Chinstrap": "#FFAA4D"   
}

# Set up the UI options
ui.page_opts(title="Pojetta and the Penguin Plots", fillable=True)

# ADD A SIDEBAR
with ui.sidebar(
    open="open"
): 
    ui.h2("Sidebar")  # Sidebar header

    # Dropdown menu selected attribute
    ui.input_selectize(
        "selected_attribute",
        "Attributes",
        choices=["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
    )

    # Numeric input for Plotly histogram
    ui.input_numeric("plotly_bin_count", "Bin Count (Plotly Histogram)", 50, min=1, max=100)

    # Slider input for Seaborn
    ui.input_slider(
        "seaborn_bin_count", "Bin Count (Seaborn Histogram)", 5, 100, 50
    )

    # Checkbox to filter species
    ui.input_checkbox_group(
        "selected_species_list",
        "Select a Species",
        choices=["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie", "Gentoo", "Chinstrap"],
        inline=False,
    )

    # Dividing line
    ui.hr()

    # Hyperlink to GitHub repo
    ui.h5("GitHub Repo")
    ui.a(
        "cintel-04-data",
        href="https://github.com/Pojetta/cintel-04-data",
        target="_blank",
    )

# Main content layout
with ui.nav_panel("Plots"):

    # Display the Penguins
    with ui.card():
        ui.card_header("Meet the Palmer Penguins")
        # Display the image
        ui.img(src="penguins.png", alt="Meet the Palmer Penguins";)
        # Add the artist credit text under the image
        ui.p("Artwork by @allison_horst", style="font-style: italic; font-size: 14px;")

    # Display the Plotly Histogram
    with ui.card():
        ui.card_header("Plotly Histogram")
        @render_plotly
        def plotly_histogram():
            return px.histogram(
                filtered_data(),
                x=input.selected_attribute(),
                nbins=input.plotly_bin_count(),
                color="species",
                color_discrete_map=color_map
            )

    # Display the Seaborn Histogram (showing all species)
    with ui.card():
        ui.card_header("Seaborn Histogram")
        @render.plot
        def seaborn_histogram():
            ax = sns.histplot(
                data=filtered_data(),
                x=input.selected_attribute(),
                bins=input.seaborn_bin_count(), 
                color = "#008C95"
            )
            ax.set_title("Palmer Penguins")
            ax.set_xlabel(input.selected_attribute())
            ax.set_ylabel("Count")
            return ax

    # Display the Plotly Scatterplot (showing selected species)
    with ui.card(full_screen=True):
        ui.card_header("Plotly Scatterplot: Species")
        @render_plotly
        def plotly_scatterplot():
            return px.scatter(
                data_frame=filtered_data(),  
                x="body_mass_g",
                y="bill_length_mm",
                color="species",
                labels={
                    "bill_length_mm": "Bill Length (mm)",
                    "body_mass_g": "Body Mass (g)",
                },
                color_discrete_map=color_map
            )
        
with ui.nav_panel("Data"): 

    # Display Data Table (showing all data)
    with ui.card(full_screen=True):
        ui.card_header("Data Table")

        @render.data_frame
        def data_table():
            return render.DataTable(filtered_data())


    # Display Data Grid (showing all data)
    with ui.card(full_screen=True):
        ui.card_header("Data Grid")

        @render.data_frame
        def data_grid():
            return render.DataGrid(filtered_data())
# --------------------------------------------------------
# Reactive calculations and effects
# --------------------------------------------------------

# Add a reactive calculation to filter the data
# By decorating the function with @reactive, we can use the function to filter the data
# The function will be called whenever an input functions used to generate that output changes.
# Any output that depends on the reactive function (e.g., filtered_data()) will be updated when the data changes.

# Reactive function to filter data
@reactive.Calc
def filtered_data():
    selected_species = input.selected_species_list()
    if selected_species:
        return penguins[penguins['species'].isin(selected_species)]
    return penguins  # Return all data if no species are selected