"""
Create an interactive web application using 'Dash' that visualizes the quantities of different fruits, 
such as apples, oranges, bananas, grapes, and strawberries. 

Users will be able to select a specific fruit from a dropdown menu, 
and the app will display a bar chart showing the amount of that fruit.

You can use the following data:

data = {
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Strawberries'],
    'Amount': [4, 1, 2, 5, 3],
}

Check the screenshot1.png for reference on how the app should look.

Required Libraries: dash, plotly, pandas
pip install dash plotly pandas
"""

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Sample data
data = {
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Strawberries'],
    'Amount': [4, 1, 2, 5, 3],
}

df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Fruit Quantity Visualization"),
    dcc.Dropdown(
        id='fruit-dropdown',
        options=[{'label': fruit, 'value': fruit} for fruit in df['Fruit']],
        value='Apples'
    ),
    dcc.Graph(id='fruit-graph')
])

# Define the callback to update the graph
@app.callback(
    Output('fruit-graph', 'figure'),
    [Input('fruit-dropdown', 'value')]
)
def update_graph(selected_fruit):
    filtered_df = df[df['Fruit'] == selected_fruit]
    fig = px.bar(filtered_df, x='Fruit', y='Amount', title=f'Quantity of {selected_fruit}')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)