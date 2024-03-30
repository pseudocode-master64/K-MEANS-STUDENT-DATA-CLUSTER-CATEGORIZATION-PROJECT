# K-Means Student Data Cluster Categorization Project

This Python-based project is developed to assist educators in analyzing student performance data. The program utilizes K-means clustering to categorize over 300 students' academic data to identify those who require academic support, enhancing targeted assistance strategies.

## Installation

To set up the project environment, ensure that Python 3.x is installed on your machine. 

## Usage

Run the main script with Python in your terminal. Follow the on-screen prompts to upload a CSV file with the student data and specify the number of clusters.

```bash
python3 main.py
```
## Features
- Analyze student performance data using K-means clustering.
- Generate 3D color-graded diagrams for visual data analysis.
- Produce Excel reports with categorized student data.
- Create an animated GIF to visualize the clustering process.

## Input and Output

The program accepts a CSV file containing student IDs, subjects, and Z-scores. It outputs Excel documents, images of clusters, and an animated GIF file representing centroid movements.

## Libraries Used

- `matplotlib` and `imageio.v2`: For data visualization and generating animations.
- `csv`: To read and write CSV files.
- `openpyxl`: For creating Excel documents.
- `numpy`: For numerical computations involved in K-means clustering.

## Sample Input and Output

Included within the `sample_data` folder.
