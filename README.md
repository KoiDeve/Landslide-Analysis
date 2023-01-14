# Landslide-Analysis

This analysis was created to understand the current events that revolve around landslides triggered by rainfalls around the world. NASA's Open Data Portal provides an export of a Global Landslide Catalog (GLC), which provides information about landslides that have occurred, as well as the sources and locations of said incidents. Most of the landslides provided occurred from the years of 2007 - 2017.

Although the API for the site did provide a csv file, the contents of the file seemed inefficient for the analysis. Upon further inspection, there were no reports made on landslides above approximately 4 **degrees** latitude when performing an API request. However, the export option did provide a csv file whose contents did contain additional information about events that were not listed in the API request. Regardless, the data is provided as well in this repo, with the credibility of the databases listed at the bottom of this README.md file.






Credibility to data used in this analysis (CSV file included under the 'data' folder):

Kirschbaum, D. B., Adler, R., Hong, Y., Hill, S., & Lerner-Lam, A. (2010). A global landslide catalog for hazard applications: method, results, and limitations. Natural Hazards, 52(3), 561–575. doi:10.1007/s11069-009-9401-4. [1]
Kirschbaum, D.B., T. Stanley, Y. Zhou (In press, 2015). Spatial and Temporal Analysis of a Global Landslide Catalog. Geomorphology. doi:10.1016/j.geomorph.2015.03.016. [2]

Link to the site for more information: 

https://data.nasa.gov/Earth-Science/Global-Landslide-Catalog-Export/dd9e-wu2v 
