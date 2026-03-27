import subprocess

def generatePlot():
    subprocess.run(["Rscript", "generate_insight.R"], check=True)
