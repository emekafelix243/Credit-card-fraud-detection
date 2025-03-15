# Importing Dependable Libraries
import os
import numpy as np
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import dash  # Use Dash instead of JupyterDash
from dash import dcc, html, Input, Output  # Condense all Dash-related imports
import pickle  # For loading saved models

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define relative file paths
DATA_FOLDER = "data"
data_credit_card = pd.read_csv(os.path.join(DATA_FOLDER, "credit.csv"))
model_metrics = pd.read_csv(os.path.join(DATA_FOLDER, "model_metrics.csv"))

# Dictionary of file paths for confusion matrices
file_paths = {
    "logistic": os.path.join(DATA_FOLDER, "confusion_matrix_logistic.csv"),
    "rf": os.path.join(DATA_FOLDER, "confusion_matrix_rf.csv"),
    "xgb": os.path.join(DATA_FOLDER, "confusion_matrix_xgb.csv")
}

# App Layout
app.layout = html.Div([
    html.H1("Fraud Detection Dashboard", style={"text-align": "center"}),

    # Section 1: Model Performance Metrics
    html.H3("1. Model Performance Metrics"),
    dcc.Graph(id="model-metrics-bar-chart", style={"height": "500px"}),

    # Section 2: Confusion Matrix Visualizations
    html.H3("2. Confusion Matrix Visualization"),
    dcc.Dropdown(
        id="confusion-matrix-selector",
        options=[
            {"label": "Logistic Regression", "value": "logistic"},
            {"label": "Random Forest", "value": "rf"},
            {"label": "XGBoost", "value": "xgb"}
        ],
        value="logistic",
        style={"width": "50%"}
    ),
    dcc.Graph(id="confusion-matrix-plot"),

    # Section 3: Data Exploration
    html.H3("3. Data Exploration"),
    dcc.Dropdown(
        id="data-exploration-selector",
        options=[
            {"label": "Histogram: Limit Balance", "value": "hist_limit_bal"},
            {"label": "Scatter Plot: Limit Balance vs Age", "value": "scatter_limit_age"}
        ],
        value="hist_limit_bal",
        style={"width": "50%"}
    ),
    dcc.Graph(id="data-exploration-plot")
])

# Callback for Model Metrics Bar Chart
@app.callback(
    Output("model-metrics-bar-chart", "figure"),
    Input("model-metrics-bar-chart", "id")
)
def update_model_metrics_bar_chart(_):
    fig = px.bar(
        model_metrics,
        x="Model",
        y=["Accuracy", "Precision", "Recall", "F1-Score", "ROC-AUC"],
        barmode="group",
        title="Model Performance Metrics",
        labels={"value": "Score", "variable": "Metric"}
    )
    return fig

# Callback to Update Confusion Matrix Plot
@app.callback(
    Output("confusion-matrix-plot", "figure"),
    Input("confusion-matrix-selector", "value")
)
def update_confusion_matrix_plot(model_type):
    file_path = file_paths.get(model_type)

    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found!")
        return px.imshow([[0, 0], [0, 0]], title="Missing Data")  # Placeholder plot

    cm = pd.read_csv(file_path)
    fig = px.imshow(
        cm.values,
        labels=dict(x="Predicted", y="Actual"),
        x=["Not Fraud", "Fraud"],
        y=["Not Fraud", "Fraud"],
        text_auto=True,
        title=f"Confusion Matrix: {model_type.capitalize()}"
    )
    return fig

# Callback for Data Exploration Plots
@app.callback(
    Output("data-exploration-plot", "figure"),
    Input("data-exploration-selector", "value")
)
def update_data_exploration_plot(plot_type):
    if plot_type == "hist_limit_bal":
        return px.histogram(data_credit_card, x="LIMIT_BAL", title="Histogram of Limit Balance")
    elif plot_type == "scatter_limit_age":
        return px.scatter(
            data_credit_card,
            x="LIMIT_BAL",
            y="AGE",
            color="default.payment.next.month",
            title="Limit Balance vs Age (Fraud Highlighted)"
        )
    return px.scatter()  # Return an empty figure to avoid errors

# Run the Dash app
if __name__ == "__main__":
    app.run_server(debug=True)