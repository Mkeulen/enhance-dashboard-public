# Imports
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq
import dash_bootstrap_components as dbc
import dash_table
from jupyter_dash import JupyterDash
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# StartUps
app = JupyterDash(__name__)
server = app.server
app = JupyterDash(__name__)

# Style declarations
## Styles overall colours
layout_example = dict(
    hovermode="closest",
    plot_bgcolor="#F9F9F9",
    paper_bgcolor="#F9F9F9",
    autosize=True,
    margin=dict(l=30, r=30, b=20, t=40),
)

## Styles components
style_cell = {"font-size": "14px", "padding": "10px"}
style_row = {"backgroundColor": "#F9F9F9"}
style_header = {
    "font-size": "14px",
    "padding": "3px",
    "textAlign": "center",
    "verticalAlign": "middle",
    "backgroundColor": "#87B9DB",
}
style_tooltip = {"maxWidth": 500, "width": 500, "backgroundColor": "#87B9DB"}
topheader_style = {"color": "#FFFFFF", "textAlign": "center"}


## Styles Tabs
tabs_styles = {
    "height": "40px",
    "padding": "3px",
}
tab_style = {
    "border-style": "solid",
    "borderTop": "1px solid #d6d6d6",
    "borderBottom": "1px solid #d6d6d6",
    "padding": "6px",
    "backgroundColor": "#F9F9F9",
    "color": "black",
}
tab_selected_style = {
    "border-style": "solid",
    "borderTop": "1px solid #d6d6d6",
    "borderBottom": "1px solid #d6d6d6",
    "padding": "6px",
    "backgroundColor": "#193B68",
    "color": "white",
}

# Data
## Analytical Data
df_population_needs = pd.read_csv(
    "data/data_analytical_population_needs_simplified_countries.csv",
    decimal=",",
    sep=";",
    header=[0],
)  # watch the decimal seperator!

df_fooditems = pd.read_csv(
    "data/data_analytical_fooditems_simplified.csv", decimal=",", sep=";", header=0
)  # watch the decimal seperator!

df_optimizedresults = pd.read_csv(
    "data/data_analytical_optimizedresults.csv", decimal=",", sep=";", header=0
)  # watch the decimal seperator!

df_optimizedresults_categorical = pd.read_csv(
    "data/data_analytical_optimizedresults_categorical.csv",
    decimal=",",
    sep=";",
    header=0,
)  # watch the decimal seperator!

## Strategic Data
df_countries = pd.read_csv("data/data_strategic_4.csv", decimal=",", sep=";", header=0)
df_indicators = pd.read_csv(
    "data/data_strategic_goals.csv", decimal=",", sep=";", header=0
)

df_projects = pd.read_csv(
    "data/data_strategic_projects.csv", decimal=",", sep=";", header=0
)

# Visual Components
## Progressbars
pbar_eth_under = daq.GraduatedBar(
    id="indicator_graduatedbar_1",
    color={
        "gradient": True,
        "ranges": {"red": [0, 40], "yellow": [40, 70], "green": [70, 100]},
    },
    showCurrentValue=True,
    max=100,
    value=60.4,
)
pbar_eth_stun = daq.GraduatedBar(
    id="indicator_graduatedbar_2",
    color={
        "gradient": True,
        "ranges": {"red": [0, 40], "yellow": [40, 70], "green": [70, 100]},
    },
    showCurrentValue=True,
    max=100,
    value=42.6,
)
pbar_eth_wast = daq.GraduatedBar(
    id="indicator_graduatedbar_3",
    color={
        "gradient": True,
        "ranges": {"red": [0, 40], "yellow": [40, 70], "green": [70, 100]},
    },
    showCurrentValue=True,
    max=100,
    value=-7.6,
)
pbar_eth_troph = daq.GraduatedBar(
    id="indicator_graduatedbar_4",
    color={
        "gradient": True,
        "ranges": {"red": [0, 40], "yellow": [40, 70], "green": [70, 100]},
    },
    showCurrentValue=True,
    max=100,
    value=-40,
)
pbar_eth_snmi = daq.GraduatedBar(
    id="indicator_graduatedbar_5",
    color={
        "gradient": True,
        "ranges": {"red": [0, 40], "yellow": [40, 70], "green": [70, 100]},
    },
    showCurrentValue=True,
    max=100,
    value=18.5,
)
pbar_eth_income = daq.GraduatedBar(
    id="indicator_graduatedbar_6",
    color={
        "gradient": True,
        "ranges": {"red": [0, 40], "yellow": [40, 70], "green": [70, 100]},
    },
    showCurrentValue=True,
    max=100,
    value=22.7,
)

pbar_ind_under = daq.GraduatedBar(
    id="indicator_graduatedbar_7",
    color={
        "gradient": True,
        "ranges": {"red": [0, 40], "yellow": [40, 70], "green": [70, 100]},
    },
    showCurrentValue=True,
    max=100,
    value=55.1,
)
pbar_ind_stun = daq.GraduatedBar(
    id="indicator_graduatedbar_8",
    color={
        "gradient": True,
        "ranges": {"red": [0, 40], "yellow": [40, 70], "green": [70, 100]},
    },
    showCurrentValue=True,
    max=100,
    value=24.3,
)
pbar_ind_wast = daq.GraduatedBar(
    id="indicator_graduatedbar_9",
    color={
        "gradient": True,
        "ranges": {"red": [0, 40], "yellow": [40, 70], "green": [70, 100]},
    },
    showCurrentValue=True,
    max=100,
    value=9.3,
)
pbar_ind_troph = daq.GraduatedBar(
    id="indicator_graduatedbar_10",
    color={
        "gradient": True,
        "ranges": {"red": [0, 40], "yellow": [40, 70], "green": [70, 100]},
    },
    showCurrentValue=True,
    max=100,
    value=-27,
)
pbar_ind_snmi = daq.GraduatedBar(
    id="indicator_graduatedbar_11",
    color={
        "gradient": True,
        "ranges": {"red": [0, 40], "yellow": [40, 70], "green": [70, 100]},
    },
    showCurrentValue=True,
    max=100,
    value=10.4,
)
pbar_ind_income = daq.GraduatedBar(
    id="indicator_graduatedbar_12",
    color={
        "gradient": True,
        "ranges": {"red": [0, 40], "yellow": [40, 70], "green": [70, 100]},
    },
    showCurrentValue=True,
    max=100,
    value=31.4,
)

## IndicatorLights
inlight_green = daq.Indicator(color="green", value=True)
inlight_red = daq.Indicator(color="red", value=True)

## Tooltips
tooltip_1 = html.Div(
    [
        html.Span(
            "(i)",
            id="tooltip-target-1",
            style={"fontWeight": "bold", "cursor": "pointer"},
        ),
        dbc.Tooltip(
            "The share of the population with a caloric intake which is insufficient to meet minimum requirements for a healthy life.",
            target="tooltip-target-1",
            style=style_tooltip,
        ),
    ]
)
tooltip_2 = html.Div(
    [
        html.Span(
            "(i)",
            id="tooltip-target-2",
            style={"fontWeight": "bold", "cursor": "pointer"},
        ),
        dbc.Tooltip(
            "Prevalence of stunting, height for age (% of children under 5)",
            target="tooltip-target-2",
            style=style_tooltip,
        ),
    ]
)
tooltip_3 = html.Div(
    [
        html.Span(
            "(i)",
            id="tooltip-target-3",
            style={"fontWeight": "bold", "cursor": "pointer"},
        ),
        dbc.Tooltip(
            "Prevalence of wasting, weight for height (% of children under 5)",
            target="tooltip-target-3",
            style=style_tooltip,
        ),
    ]
)
tooltip_4 = html.Div(
    [
        html.Span(
            "(i)",
            id="tooltip-target-4",
            style={"fontWeight": "bold", "cursor": "pointer"},
        ),
        dbc.Tooltip(
            "Trophic levels are a measure of the energy intensity of diet composition and reflect the relative amounts of plants as opposed to animals eaten in a given country. A higher trophic level represents a greater level of consumption of energy-intensive animals.",
            target="tooltip-target-4",
            style=style_tooltip,
        ),
    ]
)
tooltip_5 = html.Div(
    [
        html.Span(
            "(i)",
            id="tooltip-target-5",
            style={"fontWeight": "bold", "cursor": "pointer"},
        ),
        dbc.Tooltip(
            "The Sustainable Nitrogen Management Index (SNMI) is a one-dimensional ranking score that combines two efficiency measures in crop production: Nitrogen use efficiency (NUE) and land use efficiency (crop yield).",
            target="tooltip-target-5",
            style=style_tooltip,
        ),
    ]
)
tooltip_6 = html.Div(
    [
        html.Span(
            "(i)",
            id="tooltip-target-6",
            style={"fontWeight": "bold", "cursor": "pointer"},
        ),
        dbc.Tooltip(
            "The average income of small-scale food producers. The goal is to double the average income by 2030 from its 2012 value",
            target="tooltip-target-6",
            style=style_tooltip,
        ),
    ]
)

## DisclaimerPart
disclaimer_text = "Disclaimer: This dashboard is only intended for research on the preferred design of the dashboard. The data is made-up or edited to fit the dashboard. Not every aspect of the dashboard is working. "

# Dashboard Structure
## Layout Analytical
layout_tab1 = html.Div(
    [
        # disclaimer row
        html.Div(
            [
                html.P(
                    disclaimer_text,
                    style={"textAlign": "center", "verticalAlign": "middle"},
                    className="disclaimer_container",
                )
            ],
            className="row",
        ),
        # Row 1
        html.Div(
            [
                # Block 1.1
                html.Div(
                    [
                        # top line
                        html.H6("Population Settings", style={"textAlign": "center"}),
                        html.H6(""),
                        # middle line
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.P("Select Country:"),
                                    ]
                                ),
                                html.Div(
                                    [
                                        dcc.Dropdown(
                                            id="selector_country",
                                            options=[
                                                {
                                                    "label": "Ethiopia",
                                                    "value": "Ethiopia",
                                                },
                                                {
                                                    "label": "Indonesia",
                                                    "value": "Indonesia",
                                                },
                                            ],
                                            value="Ethiopia",
                                        ),
                                    ]
                                ),
                            ]
                        ),
                        # bottom line
                        html.H6(""),
                        html.Div(
                            [
                                html.H4(""),
                                html.P("Optimize diet for:"),
                                dcc.RadioItems(
                                    id="Population_Selector",
                                    options=[
                                        {"label": "Country Population", "value": "Pop"},
                                        {"label": "Household", "value": "House"},
                                        {"label": "Person", "value": "Person"},
                                    ],
                                    value="Person",
                                ),
                            ]
                        ),
                        html.H1(""),
                        # Button to Data
                        html.Div(
                            [
                                html.Button(
                                    "Import Data",
                                    id="upload-button",
                                    n_clicks=0,
                                    style={
                                        "horizontalAlign": "middle",
                                        "display": "inline-block",
                                    },
                                    className="button",
                                ),
                                html.Button(
                                    "Export Data",
                                    id="export2-button",
                                    n_clicks=0,
                                    style={
                                        "textAlign": "right",
                                        "display": "inline-block",
                                        "margin-left": "30px",
                                    },
                                    className="button",
                                ),
                            ],
                            style={"display": "inline-block"},
                        )
                        # Close Block 1.1
                    ],
                    style={"height": "60vh"},
                    className="pretty_container four columns",
                ),
                # Block 1.2
                html.Div(
                    [
                        html.H6(
                            "Population Daily Diet Requirements",
                            style={"textAlign": "center"},
                        ),
                        html.Div(id="table-population-container", className="table"),
                    ],
                    style={"height": "60vh"},
                    className="pretty_container seven columns",
                )
                # Close the first row
            ],
            className="row",
        ),
        # Row 2
        html.Div(
            [
                # Block 2.1
                html.Div(
                    [
                        html.H6("Diet Constraints", style={"textAlign": "center"}),
                        html.P("Select Diet Type to constrain products used:"),
                        dcc.Dropdown(
                            id="selector_diet",
                            options=[
                                {"label": "Omnivore", "value": "normal"},
                                {"label": "Vegetarian", "value": "vegetarian"},
                                {"label": "Vegan", "value": "vegan"},
                            ],
                            value="normal",
                        ),
                        html.H1(" "),
                        html.P("Daily Costs"),
                        dcc.RangeSlider(
                            id="costs-range-slider",
                            min=0,
                            max=10000,
                            step=None,
                            marks={
                                0: "0",
                                1000: "1000",
                                2000: "2000",
                                3000: "3000",
                                4000: "4000",
                                5000: "5000",
                                6000: "6000",
                                7000: "7000",
                                8000: "8000",
                                9000: "9000",
                                10000: "10000",
                            },
                            value=[3000, 9000],
                            allowCross=False,
                        ),
                        html.P("Energy (kcal)"),
                        dcc.RangeSlider(
                            id="energy-range-slider",
                            min=0,
                            max=3000,
                            step=None,
                            marks={
                                0: "0",
                                500: "500",
                                1000: "1000",
                                1500: "1500",
                                2000: "2000",
                                2500: "2500",
                                3000: "3000",
                            },
                            value=[2000, 3000],
                            allowCross=False,
                        ),
                        html.P("Protein (g)"),
                        dcc.RangeSlider(
                            id="protein-range-slider",
                            min=0,
                            max=100,
                            step=None,
                            marks={
                                0: "0",
                                10: "10",
                                20: "20",
                                30: "30",
                                40: "40",
                                50: "50",
                                60: "60",
                                70: "70",
                                80: "80",
                                90: "90",
                                100: "100",
                            },
                            value=[50, 70],
                            allowCross=False,
                        ),
                        html.P("Fat (g)"),
                        dcc.RangeSlider(
                            id="fat-range-slider",
                            min=0,
                            max=100,
                            step=None,
                            marks={
                                0: "0",
                                10: "10",
                                20: "20",
                                30: "30",
                                40: "40",
                                50: "50",
                                60: "60",
                                70: "70",
                                80: "80",
                                90: "90",
                                100: "100",
                            },
                            value=[30, 60],
                            allowCross=False,
                        ),
                        html.H4(" "),
                        html.H6("Optimization Settings", style={"textAlign": "center"}),
                        # Radio Items
                        dcc.RadioItems(
                            id="Optimize_Selector",
                            options=[
                                {
                                    "label": "Stay close to reference diet",
                                    "value": "ref",
                                },
                                {
                                    "label": "Optimize for given properties",
                                    "value": "opt",
                                },
                            ],
                            value="ref",
                        ),
                        html.H4(" "),
                        dcc.RadioItems(
                            id="Results_Selector",
                            options=[
                                {
                                    "label": "Give single best results",
                                    "value": "single_result",
                                },
                                {
                                    "label": "Give list of results",
                                    "value": "multiple_results",
                                },
                            ],
                            value="single_result",
                        ),
                        html.H4(" "),
                        # Button to optimize
                        html.Div(
                            [
                                html.Button(
                                    "Optimize",
                                    id="optimize-button",
                                    n_clicks=0,
                                    style={
                                        "horizontalAlign": "middle",
                                        "display": "inline-block",
                                    },
                                    className="button",
                                )
                            ],
                            style={"textAlign": "center"},
                        )
                        # close block 2.1
                    ],
                    style={"height": "105vh"},
                    className="pretty_container four columns",
                ),
                # Block 2.2
                html.Div(
                    [
                        html.H6("Food Items in Diet", style={"textAlign": "center"}),
                        html.Div(id="table-fooditems-container", className="table"),
                    ],
                    className="pretty_container seven columns",
                )
                # close the second row
            ],
            className="row",
        ),
        # Row 3
        html.Div(
            [
                # Block 3.1
                html.Div(
                    [
                        html.H6(
                            "Optimized Diets Scores", style={"textAlign": "center"}
                        ),
                        dcc.Graph(
                            id="diet-effects-container",
                            config={"displayModeBar": False},
                        ),
                    ],
                    style={"height": "85vh"},
                    className="pretty_container five columns",
                ),
                # Block 3.2
                html.Div(
                    [
                        html.H6(
                            "Optimized Diets Contents", style={"textAlign": "center"}
                        ),
                        html.Div(
                            dcc.Graph(
                                id="diet-contains-container", style={"display": "none"}
                            )
                        ),
                    ],
                    style={"height": "85vh"},
                    className="pretty_container six columns",
                )
                # close the third row
            ],
            className="row",
        ),
        # Close the Layout
    ]
)


## Layout Strategic
layout_tab2 = html.Div(
    [
        # Disclaimer Row
        html.Div(
            [
                html.P(
                    disclaimer_text,
                    style={"textAlign": "center", "verticalAlign": "middle"},
                    className="disclaimer_container",
                )
            ],
            className="row",
        ),
        # Row 1
        html.Div(
            [
                # Block 1.1 - Country Selector Label
                html.Div(
                    [
                        html.H6("Dashboard Settings", style={"textAlign": "center"}),
                        html.H6(""),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.P("Select Country:"),
                                    ]
                                ),
                                html.Div(
                                    [
                                        dcc.Dropdown(
                                            id="selector_country",
                                            options=[
                                                {
                                                    "label": "Ethiopia",
                                                    "value": "Ethiopia",
                                                },
                                                {
                                                    "label": "Indonesia",
                                                    "value": "Indonesia",
                                                },
                                            ],
                                            value="Ethiopia",
                                        ),
                                    ]
                                ),
                            ]
                        ),
                        html.H1("   "),
                        html.H1("   "),
                        html.H1("   "),
                        html.P("Select Indicator:"),
                        dcc.RadioItems(
                            id="selector_indicators",
                            options=[
                                {
                                    "label": "Prevalence Undernourishment %",
                                    "value": "prevalence_undernourishment",
                                },
                                {
                                    "label": "Prevalence Stunting %",
                                    "value": "prevalence_stunting",
                                },
                                {
                                    "label": "Pevalence Wasting %",
                                    "value": "prevalence_wasting",
                                },
                                {
                                    "label": "Human Trophic Level",
                                    "value": "human_trophic_level",
                                },
                                {"label": "SNMI", "value": "snmi"},
                                {
                                    "label": "Average Income FoodProducers $",
                                    "value": "average_income_foodproducers_$",
                                },
                            ],
                            value="prevalence_undernourishment",
                        ),
                    ],
                    style={"height": "77vh"},
                    className="pretty_container four columns",
                ),
                # Block 1.2 - Indicators Stuff
                html.Div(
                    [
                        # first left side
                        html.Div(
                            [html.Div(id="table-container", className="table")],
                            style={"height": "77vh"},
                            className="pretty_container seven columns",
                        )
                    ]
                ),
                # Close the first row
            ],
            className="row",
        ),
        # Row 2
        html.Div(
            [
                # Block 2.2 - Graph of Sub-SDG
                html.Div(
                    [dcc.Graph(id="line-chart")],
                    style={"height": "75vh"},
                    className="pretty_container six columns",
                ),
                # Block 2.4 - Information on the projects
                html.Div(
                    [
                        html.H4("World Food Programme Projects"),
                        html.Div(id="projects-container"),
                    ],
                    style={"height": "75vh"},
                    className="pretty_container five columns",
                ),
                # close the second row
            ],
            className="row",
        ),
        # Close the Layout
    ]
)

## Layout Header & Tabs
tabs_layout = html.Div(
    [
        html.Div(
            html.H6("Test for Demo Dashboard Project ENHANCE"),
            style=topheader_style,
            className="header_container",
        ),
        dcc.Tabs(
            id="tabs-example",
            value="tab-1",
            children=[
                dcc.Tab(
                    label="Analytical Dashboard",
                    value="tab-1",
                    style=tab_style,
                    selected_style=tab_selected_style,
                ),
                dcc.Tab(
                    label="Strategic Dashboard",
                    value="tab-2",
                    style=tab_style,
                    selected_style=tab_selected_style,
                ),
            ],
            style=tabs_styles,
        ),
        html.Div(id="tabs-example-content"),
    ]
)

## Index layout
app.layout = tabs_layout

## Complete layout
app.validation_layout = html.Div(
    [
        tabs_layout,
        layout_tab1,
        layout_tab2,
    ]
)

# Callbacks
## Full dashboard callbacks
@app.callback(
    Output("tabs-example-content", "children"), Input("tabs-example", "value")
)
def render_content(tab):
    if tab == "tab-1":
        return layout_tab1
    elif tab == "tab-2":
        return layout_tab2


## calbacks for tab 1
@app.callback(
    Output("table-population-container", "children"), Input("selector_country", "value")
)
def display_table(selected_country):
    df_table = df_population_needs[df_population_needs["Country"] == selected_country]
    df_shown = df_table.iloc[:, [0, 1, 2, 3, 4]]

    population_table = html.Div(
        [
            dash_table.DataTable(
                id="table-editing-simple-population",
                columns=[{"name": c, "id": c} for c in df_shown.columns],
                data=df_shown.to_dict("records"),
                merge_duplicate_headers=True,
                editable=False,
                fixed_rows={"headers": True},
                style_cell={
                    "height": "auto",
                    # all three widths are needed
                    "minWidth": "80px",
                    "maxWidth": "180px",
                    "whiteSpace": "normal",
                },
                style_data={"border": "1px #B5D4E9 solid"},
                style_data_conditional=[
                    {"if": {"row_index": "odd"}, "backgroundColor": "#F5F5F5"},
                    {"if": {"row_index": "even"}, "backgroundColor": "#F10F10F10"},
                ],
                style_header={
                    "backgroundColor": "#87B9DB",
                    "fontWeight": "bold",
                    "border": "1px #B5D4E9 solid",
                },
                style_cell_conditional=[
                    {"if": {"column_id": "Person Description"}, "textAlign": "left"}
                ],
            )
        ]
    )

    return population_table


##
@app.callback(
    Output("table-fooditems-container", "children"), Input("selector_diet", "value")
)
def display_table(selected_diet):
    if selected_diet == "vegan":
        df_table_fooditems = df_fooditems[
            (df_fooditems["NotDietType"] != "vegan")
            & (df_fooditems["NotDietType"] != "vegetarian")
        ]

    elif selected_diet == "vegetarian":
        df_table_fooditems = df_fooditems[df_fooditems["NotDietType"] != "vegetarian"]

    else:
        df_table_fooditems = df_fooditems

    df_table_fooditems_shown = df_table_fooditems.iloc[:, [0, 1, 2, 3, 4]]

    fooditems_table = html.Div(
        [
            dash_table.DataTable(
                id="table-editing-simple-products",
                columns=[
                    {"name": c, "id": c} for c in df_table_fooditems_shown.columns
                ],
                data=df_table_fooditems_shown.to_dict("records_fooditems"),
                editable=False,
                fixed_rows={"headers": True},
                style_table={"height": "800px", "overflowX": "auto"},
                style_cell_conditional=[
                    {"if": {"column_id": "Name"}, "textAlign": "left"}
                ],
                style_cell={
                    "height": "auto",
                    # all three widths are needed
                    "minWidth": "80px",
                    "maxWidth": "180px",
                    "whiteSpace": "normal",
                },
                style_data={"border": "1px #B5D4E9 solid"},
                style_data_conditional=[
                    {"if": {"row_index": "odd"}, "backgroundColor": "#F5F5F5"},
                    {"if": {"row_index": "even"}, "backgroundColor": "#F10F10F10"},
                ],
                style_header={
                    "backgroundColor": "#87B9DB",
                    "fontWeight": "bold",
                    "border": "1px #B5D4E9 solid",
                },
            )
        ]
    )

    return fooditems_table


@app.callback(
    Output("diet-effects-container", "figure"), Input("optimize-button", "n_clicks")
)
def display_diet_effects(button_clicks):

    if button_clicks == 0:

        df_reference = df_optimizedresults[
            df_optimizedresults["FoodItem"] == "Reference Diet"
        ]

        diet_effects_graph = go.Figure(
            data=go.Parcoords(
                line=dict(
                    color=df_reference["Daily Costs"],
                    colorscale=[[0, "#7E909A"], [1, "#7E909A"]],
                    showscale=True,
                ),
                dimensions=list(
                    [
                        dict(
                            range=[3000, 9000],
                            label="Daily Costs",
                            values=df_reference["Daily Costs"],
                        ),
                        dict(
                            range=[500, 1200],
                            label="Daily Intake (g)",
                            values=df_reference["Daily Intake (g)"],
                        ),
                        dict(
                            range=[750, 2500],
                            label="Energy (kcal)",
                            values=df_reference["Energy (kcal)"],
                        ),
                        dict(
                            range=[50, 100],
                            label="Protein (g)",
                            values=df_reference["Protein (g)"],
                        ),
                        dict(
                            range=[25, 60],
                            label="Fat (g)",
                            values=df_reference["Fat (g)"],
                        ),
                    ]
                ),
            )
        )

        diet_effects_graph.update_traces(
            line_colorbar=dict(title=" ", tickvals=[6400], ticktext=["Reference Diet"]),
            selector=dict(type="parcoords"),
        )

        diet_effects_graph.update_layout(
            title="Reference Diet", plot_bgcolor="white", paper_bgcolor="white"
        )
        # close the if clicks ==0 statement

    else:

        df_optimizedresults_totals = df_optimizedresults[
            (df_optimizedresults["FoodItem"] == "Total")
            | (df_optimizedresults["FoodItem"] == "Reference Diet")
        ]

        diet_effects_graph = go.Figure(
            data=go.Parcoords(
                line=dict(
                    color=df_optimizedresults_totals["Daily Costs"],
                    colorscale=[
                        [0, "#B5D4E9"],
                        [0.33, "#B5D4E9"],
                        [0.33, "#7E909A"],
                        [0.66, "#7E909A"],
                        [0.66, "#F8E9A1"],
                        [1, "#F8E9A1"],
                    ],
                    showscale=True,
                ),
                dimensions=list(
                    [
                        dict(
                            range=[3000, 9000],
                            label="Daily Costs",
                            values=df_optimizedresults_totals["Daily Costs"],
                        ),
                        dict(
                            range=[500, 1200],
                            label="Daily Intake (g)",
                            values=df_optimizedresults_totals["Daily Intake (g)"],
                        ),
                        dict(
                            range=[750, 2500],
                            label="Energy (kcal)",
                            values=df_optimizedresults_totals["Energy (kcal)"],
                        ),
                        dict(
                            range=[50, 100],
                            label="Protein (g)",
                            values=df_optimizedresults_totals["Protein (g)"],
                        ),
                        dict(
                            range=[25, 60],
                            label="Fat (g)",
                            values=df_optimizedresults_totals["Fat (g)"],
                        ),
                    ]
                ),
            )
        )

        diet_effects_graph.update_traces(
            line_colorbar=dict(
                title="Optimized Results",
                tickvals=[5000, 6500, 8000],
                ticktext=["Diet 2", "Reference Diet", "Diet 1"],
            ),
            selector=dict(type="parcoords"),
        )

        diet_effects_graph.update_layout(
            title="Reference Diets & Optimized Results",
            plot_bgcolor="white",
            paper_bgcolor="white",
        )

        # close the if clicks is more than 0 statement

    return diet_effects_graph


##
@app.callback(
    Output("diet-contains-container", component_property="style"),
    Input("optimize-button", "n_clicks"),
)
def show_diet_contains(button_clicks):
    if button_clicks == 0:
        return {"display": "none"}

    else:
        return {"display": "block"}


##


@app.callback(
    Output("diet-contains-container", "figure"), Input("optimize-button", "n_clicks")
)
def display_diet_contains(button_clicks):

    if button_clicks == 0:

        return {}

    else:

        fig_costeffects = px.bar(
            df_optimizedresults_categorical,
            x="Value",
            y="Diet#",
            color="FoodItem",
            color_discrete_sequence=px.colors.qualitative.Pastel1,
            # text = 'Daily Costs', #gives each thingy a label
            facet_row="Category",
            facet_row_spacing=0.05,
            orientation="h",
        )

        # hide the original labels first
        fig_costeffects.for_each_annotation(lambda a: a.update(text=""))

        # then make the new labels appear where I want them
        fig_costeffects.update_layout(
            # keep the original annotations and add a list of new annotations:
            annotations=list(fig_costeffects.layout.annotations)
            + [
                go.layout.Annotation(
                    x=0.95,
                    y=0.98,
                    font=dict(size=10),
                    showarrow=False,
                    text="Daily Costs",
                    # textangle=-90,
                    xref="paper",
                    yref="paper",
                ),
                go.layout.Annotation(
                    x=0.95,
                    y=0.76,
                    font=dict(size=10),
                    showarrow=False,
                    text="Daily Intake (g)",
                    # textangle=-90,
                    xref="paper",
                    yref="paper",
                ),
                go.layout.Annotation(
                    x=0.95,
                    y=0.53,
                    font=dict(size=10),
                    showarrow=False,
                    text="Daily Energy (kcal)",
                    # textangle=-90,
                    xref="paper",
                    yref="paper",
                ),
                go.layout.Annotation(
                    x=0.95,
                    y=0.30,
                    font=dict(size=10),
                    showarrow=False,
                    text="Daily Protein (g)",
                    # textangle=-90,
                    xref="paper",
                    yref="paper",
                ),
                go.layout.Annotation(
                    x=0.95,
                    y=0.08,
                    font=dict(size=10),
                    showarrow=False,
                    text="Daily Fat (g)",
                    # textangle=-90,
                    xref="paper",
                    yref="paper",
                ),
            ]
        )

        fig_costeffects.update_xaxes(matches=None)

        fig_costeffects.update_yaxes(type="category")

        fig_costeffects.update_xaxes(showticklabels=True)

        fig_costeffects.update_layout(
            title="Optimized Diets",
            legend=dict(
                orientation="h", yanchor="bottom", y=-0.5, xanchor="right", x=1
            ),
        )

        return fig_costeffects


####

# Callbacks for Tab2
# Interactivity
@app.callback(
    Output("line-chart", "figure"),
    Input("selector_country", "value"),
    Input("selector_indicators", "value"),
)
def update_line_chart(selected_country, selected_indicator):

    country_df_indicators = df_countries[(df_countries["country"] == selected_country)]
    country_indicator_df_indicators = country_df_indicators[
        country_df_indicators["indicator"] == selected_indicator
    ]

    world_df_indicators = df_countries[(df_countries["country"] == "World")]
    world_indicator_df_indicators = world_df_indicators[
        world_df_indicators["indicator"] == selected_indicator
    ]

    if selected_indicator == "human_trophic_level":
        goal_value = 2.04
    elif selected_indicator == "average_income_foodproducers_$":
        if selected_country == "Ethiopia":
            goal_value = 913.98
        else:
            goal_value = 5542.68
    else:
        goal_value = 0

    linechart_data = [
        dict(
            type="scatter",
            mode="lines+markers",
            name=selected_country,
            x=country_indicator_df_indicators["year"],
            y=country_indicator_df_indicators["value"],
            line=dict(shape="spline", width=1, color="blue"),
        ),
        dict(
            type="scatter",
            mode="lines+markers",
            name="World Average",
            x=world_indicator_df_indicators["year"],
            y=world_indicator_df_indicators["value"],
            line=dict(shape="spline", width=1, color="goldenrod"),
        ),
    ]

    fig_linechart = go.Figure(data=linechart_data, layout=layout_example)

    fig_linechart.update_xaxes(range=[2000, 2030])

    fig_linechart.update_xaxes(fixedrange=True)
    fig_linechart.update_yaxes(fixedrange=True)

    fig_linechart.add_hline(
        y=goal_value,
        line_dash="dashdot",
        line_color="red",
        annotation_text="SDG Goal",
        annotation_position="bottom right",
    )

    fig_linechart.update_layout(
        title="Progress towards SDG Goal",
        title_x=0.5,
        xaxis_title="Year",
        yaxis_title="Value",
        legend_title="Legend",
    )

    indicator_df = df_projects[df_projects["Indicator"] == selected_indicator]
    list_startingdates = indicator_df["StartingDate"].tolist()
    list_endingdates = indicator_df["EndDate"].tolist()
    list_names = indicator_df["Project Name"].tolist()

    if len(list_names) == 0:
        return fig_linechart

    else:
        for i in range(len(list_names)):
            fig_linechart.add_vrect(
                x0=list_startingdates[i],
                x1=list_endingdates[i],
                annotation_text=list_names[i],
                annotation_position="top left",
                fillcolor="blue",
                opacity=0.25,
                line_width=0,
            )

        return fig_linechart


##


@app.callback(Output("table-container", "children"), Input("selector_country", "value"))
def display_table(selected_country):

    if selected_country == "Ethiopia":

        Ethiopia_table = html.Table(
            [
                html.Tr(
                    [
                        html.Th(
                            ["Indicator from SDG 2: 'Zero Hunger'"], style=style_header
                        ),
                        html.Th(["Indicator Goal"], style=style_header),
                        html.Th(["Current Value"], style=style_header),
                        html.Th(["Progress Towards Goal"], style=style_header),
                        html.Th(["On Track for 2030?"], style=style_header),
                        html.Th(["More Info"], style=style_header),
                    ]
                )
            ]
            + [
                html.Tr(
                    [
                        html.Td(["Prevalence Undernourishment %"], style=style_cell),
                        html.Td("  0.00%  "),
                        html.Td("20.60%"),
                        html.Td(pbar_eth_under),
                        html.Td(inlight_green),
                        html.Td(tooltip_1),
                    ],
                    style=style_row,
                ),
                html.Tr(
                    [
                        html.Td(["Prevalence Stunting %"], style=style_cell),
                        html.Td("0.00%"),
                        html.Td("38.40%"),
                        html.Td(pbar_eth_stun),
                        html.Td(inlight_red),
                        html.Td(tooltip_2),
                    ],
                    style=style_row,
                ),
                html.Tr(
                    [
                        html.Td(["Prevalence Wasting %"], style=style_cell),
                        html.Td("0.00%"),
                        html.Td("9.90%"),
                        html.Td(pbar_eth_wast),
                        html.Td(inlight_red),
                        html.Td(tooltip_3),
                    ],
                    style=style_row,
                ),
                html.Tr(
                    [
                        html.Td(["Human Trophic Level"], style=style_cell),
                        html.Td("2.04"),
                        html.Td("0.07"),
                        html.Td(pbar_eth_troph),
                        html.Td(inlight_red),
                        html.Td(tooltip_4),
                    ],
                    style=style_row,
                ),
                html.Tr(
                    [
                        html.Td(
                            ["Sustainable Nitrogen Management Index (SNMI)"],
                            style=style_cell,
                        ),
                        html.Td("0.00"),
                        html.Td("0.66"),
                        html.Td(pbar_eth_snmi),
                        html.Td(inlight_red),
                        html.Td(tooltip_5),
                    ],
                    style=style_row,
                ),
                html.Tr(
                    [
                        html.Td(["Average Income FoodProducers"], style=style_cell),
                        html.Td("913.98$"),
                        html.Td("560.92$"),
                        html.Td(pbar_eth_income),
                        html.Td(inlight_red),
                        html.Td(tooltip_6),
                    ],
                    style=style_row,
                ),
            ],
        )

        return Ethiopia_table

    else:

        Indonesia_table = html.Table(
            [
                html.Tr(
                    [
                        html.Th(["Indicator"], style=style_header),
                        html.Th(["Indicator Goal"], style=style_header),
                        html.Th(["Current Value"], style=style_header),
                        html.Th(["Progress Towards Goal"], style=style_header),
                        html.Th(["On Track?"], style=style_header),
                        html.Th(["More Info"], style=style_header),
                    ]
                )
            ]
            + [
                html.Tr(
                    [
                        html.Td(["Prevalence Undernourishment %"], style=style_cell),
                        html.Td("  0.00%  "),
                        html.Td("8.30%"),
                        html.Td(pbar_ind_under),
                        html.Td(inlight_green),
                        html.Td(tooltip_1),
                    ],
                    style=style_row,
                ),
                html.Tr(
                    [
                        html.Td(["Prevalence Stunting %"], style=style_cell),
                        html.Td("0.00%"),
                        html.Td("36.40%"),
                        html.Td(pbar_ind_stun),
                        html.Td(inlight_red),
                        html.Td(tooltip_2),
                    ],
                    style=style_row,
                ),
                html.Tr(
                    [
                        html.Td(["Prevalence Wasting %"], style=style_cell),
                        html.Td("0.00%"),
                        html.Td("13.50%"),
                        html.Td(pbar_ind_wast),
                        html.Td(inlight_red),
                        html.Td(tooltip_3),
                    ],
                    style=style_row,
                ),
                html.Tr(
                    [
                        html.Td(["Human Trophic Level"], style=style_cell),
                        html.Td("2.04"),
                        html.Td("0.14"),
                        html.Td(pbar_ind_troph),
                        html.Td(inlight_red),
                        html.Td(tooltip_4),
                    ],
                    style=style_row,
                ),
                html.Tr(
                    [
                        html.Td(
                            ["Sustainable Nitrogen Management Index (SNMI)"],
                            style=style_cell,
                        ),
                        html.Td("0.00"),
                        html.Td("0.69"),
                        html.Td(pbar_ind_snmi),
                        html.Td(inlight_red),
                        html.Td(tooltip_5),
                    ],
                    style=style_row,
                ),
                html.Tr(
                    [
                        html.Td(["Average Income FoodProducers"], style=style_cell),
                        html.Td("5542.6$"),
                        html.Td("3641.9$"),
                        html.Td(pbar_ind_income),
                        html.Td(inlight_red),
                        html.Td(tooltip_6),
                    ],
                    style=style_row,
                ),
            ],
        )

        return Indonesia_table


@app.callback(
    Output("projects-container", "children"), Input("selector_indicators", "value")
)
def display_table(selected_indicator):

    indicator_df = df_projects[df_projects["Indicator"] == selected_indicator]
    list_descriptions = indicator_df["Project Description"].tolist()
    list_names = indicator_df["Project Name"].tolist()

    if len(list_descriptions) == 0:
        html_list = [html.Div([html.H4("No Projects to Display")], className="page-1k")]

    else:
        html_list = []
        for i in range(len(list_descriptions)):
            html_list.append(
                html.Div(
                    [
                        html.H6(list_names[i], style={"font-size": "14px"}),
                        html.P(list_descriptions[i], style={"font-size": "12px"}),
                    ],
                    className="page-1k",
                )
            )

    return html_list


# Run the Dashboard
app.run_server(debug=False)
