import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import flask
import os
import plotly.graph_objects as go
import plotly.express as px

server = flask.Flask('app')
server.secret_key = os.environ.get('secret_key', 'secret')

app = dash.Dash('app', server=server)

df = pd.read_csv('covid_2020_daily.csv')
df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)
us_total = df.groupby(['date'], as_index=False).sum()

options = [{'label': i, 'value': i} for i in df['state'].unique()]
options.insert(0, {'label': 'All States', 'value': 'All States'})

app.layout = html.Div(
    children=[
        html.Div([html.H1('US COVID-19 Data Analysis')]),

        html.Div([
            html.H2('Select State(s)'),
            dcc.Dropdown(
                id='state-dropdown',
                options=options,
                multi=True,
                placeholder='Select State(s)',
            ),
        ], className="state-dropdown"),

        html.Div([
            html.H2('Date Range Selection'),
            dcc.DatePickerRange(
                id='date-picker-range',
                start_date=df['date'].min(),
                end_date=df['date'].max(),
                display_format='MM/DD/YYYY',
            ),
        ], className="date-picker-range"),

        html.Div([
            html.H2('Positive and Total Cases by State'),
            dcc.Graph(id='my-graph')
        ], className="barchart"),

        html.Div([
            html.H2('Map of Total Cases by State'),
            dcc.Graph(id='my-map')
        ], className="map"),

        html.Div([
            dcc.Slider(
                id='my-slider',
                min=0,
                max=353,
                step=1,
                value=150,
                marks={0: 'Jan', 19: 'Feb',
                       48: 'Mar',
                       79: 'Apr',
                       109: 'May',
                       140: 'Jun',
                       170: 'July',
                       201: 'Aug',
                       232: 'Sept',
                       262: 'Oct',
                       293: 'Nov',
                       323: 'Dec'
                       }
            ),
            html.Div(id='slider-output')
        ], className="slider"),

        html.Div([
            html.H2('COVID-19 Deaths by State Over Time'),
            dcc.Graph(id='death-line-chart')
        ], className="line-chart")
    ]
)


@app.callback(
    [Output('my-graph', 'figure'),
     Output('my-map', 'figure'),
     Output('death-line-chart', 'figure')],
    [Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date'),
     Input('state-dropdown', 'value'),
     Input('my-slider', 'value')]
)
def update_charts(start_date, end_date, selected_states, selected_date):
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

    if selected_states:
        filtered_df = filtered_df[filtered_df['state'].isin(selected_states)]

    fig_bar_chart = go.Figure(data=[
        go.Bar(name='Total Tests', x=us_total.date, y=us_total.totalTestResults),
        go.Bar(name='Positive Tests', x=us_total.date, y=us_total.positive)
    ])
    fig_bar_chart.update_layout(barmode='overlay')

    df_day = df[df.date == (df.date.min() + pd.DateOffset(days=selected_date))]
    fig_map = go.Figure(data=go.Choropleth(
        locations=df_day['state'],
        z=df_day['totalTestResults'],
        locationmode='USA-states',
        colorscale='Reds',
        colorbar_title="Total Tests",
    ))
    fig_map.update_layout(title_text='2020 US Covid Testing Total by State', geo_scope='usa', height=700, width=1100)

    death_line_chart = px.line(filtered_df, x='date', y='death', color='state', labels={'death': 'Deaths'})
    death_line_chart.update_layout(title='COVID-19 Deaths by State Over Time')

    return fig_bar_chart, fig_map, death_line_chart


if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port=8050, debug=True)
