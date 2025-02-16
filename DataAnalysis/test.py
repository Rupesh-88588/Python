import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import seaborn as sns

import requests

html_code = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=')
print(html_code.text)  # To display the HTML content
