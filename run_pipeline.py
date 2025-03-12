import os
import nbformat
import subprocess
from nbconvert.preprocessors import ExecutePreprocessor

def run_notebook(notebook_path, timeout=600):
    """Executes a Jupyter notebook and saves the output."""
    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook = nbformat.read(f, as_version=4)
    
    executor = ExecutePreprocessor(timeout=timeout, kernel_name="python3")
    executor.preprocess(notebook, {'metadata': {'path': os.path.dirname(notebook_path)}})
    
    with open(notebook_path, "w", encoding="utf-8") as f:
        nbformat.write(notebook, f)
    
    print(f"Executed: {notebook_path}")

def run_pipeline(notebooks_dir):
    """Executes specific Jupyter notebooks in a predefined sequence."""
    notebook_sequence = ["EDA.ipynb", "Modeling.ipynb", "fraud_detection_dashboard.ipynb"]
    
    for notebook in notebook_sequence:
        notebook_path = os.path.join(notebooks_dir, notebook)
        if os.path.exists(notebook_path):
            print(f"Running {notebook}...")
            try:
                run_notebook(notebook_path)
            except Exception as e:
                print(f"Error running {notebook}: {e}")
                break  # Stop execution if an error occurs
        else:
            print(f"Notebook {notebook} not found. Skipping...")

if __name__ == "__main__":
    notebooks_directory = r"C:\Users\user\Documents\PROJECTS\DATA SCIENCE PROJECTS\CREDIT CARD FRAUD DETECTION\notebook"
    run_pipeline(notebooks_directory)
