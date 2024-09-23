# COSMADS: Composing SMArt Data Services through Large Language Models
This repository contains code for replicating the experiments in *"Composing SMArt Data Services through Large Language Models"* paper.


## Prerequisites
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- [OpenAI API Key](https://platform.openai.com)


## Setup
- Create a virtual environment and install the dependencies
```bash
conda create -n pyllm python=3.9
conda activate pyllm
pip install -r requirements.txt
```
- Create a `.env` file in the root directory of the project and add the following line
```
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
```


## How to replicate the experiments

To run the experiments, execute the following command:
```bash
cd src
python run_evaluation.py
```

The script will create different `.csv` in [evaluation](src/evaluation/) folder containing the results of the run and computed metrics.


## Experiments results

[evaluation](src/evaluation/) folder contains the results of the experiments:
- COSMADS:
    - [evaluation results](src/evaluation/evaluation_results_standard.csv)
    - [metrics](src/evaluation/metrics_results_standard.csv)
- COSMADS (w/o similar pipelines):
    - [evaluation results](src/evaluation/evaluation_results_wrong.csv)
    - [metrics](src/evaluation/metrics_results_wrong.csv)
- COSMADS (w/o pipelines):
    - [evaluation results](src/evaluation/evaluation_results_wo_pipeline.csv)
    - [metrics](src/evaluation/metrics_results_wo_pipeline.csv)
- GitHub Copilot:
    - [evaluation results](src/evaluation/evaluation_results_copilot.csv)
    - [metrics](src/evaluation/metrics_results_copilot.csv)
