import pandas as pd

INTRO = """[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](./CONTRIBUTING.md) [![HitCount](https://hits.dwyl.com/AlexMolas/ml-blogs.svg?style=flat-square)](http://hits.dwyl.com/AlexMolas/ml-blogs)

A curated list of personal machine learning and data science blogs. 

To add your blog feel free to open a PR. If you don't feel to open a PR feel free to add your blog in this [spreadsheet](https://docs.google.com/spreadsheets/d/1H9ceAbEkSvtzg8A2x0BkI44qJw3Cq0rPdnCihGMn8rU/edit) and I'll add it in the repo when I have time!

# List of blogs
"""
url = "https://docs.google.com/spreadsheets/d/1H9ceAbEkSvtzg8A2x0BkI44qJw3Cq0rPdnCihGMn8rU/export?format=csv&gid=0"

data = pd.read_csv(url).sort_values(by="Author")

with open("README.md", "w") as f:
    f.write(INTRO)
    for blog in data.itertuples():
        author = blog[1]
        url = blog[2]
        description = blog[3]
        f.write(f"* **Author** : {author} \n")
        f.write(f"* **URL** : [{url}]({url}) \n")
        f.write(f"* **Description** : {description} \n")
        f.write("--- \n")
