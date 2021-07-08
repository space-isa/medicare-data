# medicare-data
Deep 2014 medicare analysis using BigQuery and Tableau

## About 
Medicare provides federal health insurance to people age 65 and over, as well as to younger folks with disabilities. Medicare data from 2014 was cleaned, aggregated, and merged with US census data to gain deeper insights. The Medicare dataset found on BigQuery was provided by the Centers for Medicare & Medicaid Services (CMS), and the estimated state population, population demographics, and poverty rates in 2014 came from the US Census' [website](https://www.census.gov/).

**Goals:**
1. Gain insights into medicare data (inpatient, outpatient, and prescriptions) for the year 2014.
2. Place medicare data into context with estimated 2014 state population and demographics for folks 65 and over.
3. Place medicare data into context with estimated 2014 state poverty rates (all ages).

**Tableau:**

Post-processed data was used in Tableau to generate interactive vizualizations, a screenshot of which is shown below. You can view the interactive map [here](https://public.tableau.com/views/medicare-bivariate-maps/Bivariatemappovertyprescriptions?:language=en-US&:display_count=n&:origin=viz_share_link).

![A geographic map showing the rates of poverty and prescription rates. The title says "Southeastern states have the highest rates of poverty and medication prescriptions"](https://github.com/space-isa/medicare-data/blob/main/docs/figures/bivariate-map-poverty-prescriptions.png?raw=true)
---

## Requirements
This code was developed and tested using Python 3.8.8.

Install before use: 
- Pandas, Geopandas
- Numpy 
- BigQuery
- Scipy
- Plotly, Matplotlib, Seaborn
--- 

## How to use
The exploratory analysis notebook ```medicare_data_analysis.ipynb``` can be found in the ```/src``` directory, or it can be viewed using [this link](https://nbviewer.jupyter.org/github/space-isa/medicare-data/blob/main/src/medicare_data_analysis.ipynb).

Datasets imported by csv can be found in the ```/data/input``` directory.

Datasets saved after processing can be found in the ```/data/output/``` direcotry.

Tableau workbooks can be found in ```/docs/Tableau/```.

---

## Author 
Isabel J. Rodriguez 
