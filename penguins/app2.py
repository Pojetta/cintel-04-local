with ui.nav_panel("Plots"):
    # Create the layout with two rows and two columns
    with ui.row():
        # Column 1: Image
        with ui.column():
            # Display the Penguins
            with ui.card():
                ui.card_header("Meet the Palmer Penguins")
                # Display the image
                ui.img(src="penguins.png", alt="Meet the Palmer Penguins")
                # Add the artist credit text under the image
                ui.p("Artwork by @allison_horst", style="font-style: italic; font-size: 14px;")
        
        # Column 2: Plotly Histogram
        with ui.column():
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

    # Second row with two columns
    with ui.row():
        # Column 1: Seaborn Histogram
        with ui.column():
            # Display the Seaborn Histogram (showing all species)
            with ui.card():
                ui.card_header("Seaborn Histogram")
                @render.plot
                def seaborn_histogram():
                    ax = sns.histplot(
                        data=filtered_data(),
                        x=input.selected_attribute(),
                        bins=input.seaborn_bin_count(), 
                        color="#008C95"
                    )
                    ax.set_title("Palmer Penguins")
                    ax.set_xlabel(input.selected_attribute())
                    ax.set_ylabel("Count")
                    return ax

        # Column 2: Plotly Scatterplot
        with ui.column(full_screen=True):
            # Display the Plotly Scatterplot (showing selected species)
            with ui.card():
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
