import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

# Ideas - 
# 
# Create a categorical based on landslide trigger (what percentage causes the most landslides)
# Plot areas on a tableau map to show where the most landslides happen + size indicator

class Landslide:
    
    # Initializes class and puts data into a dataframe, as well as storing the map image for later use.
    def __init__(self, url, image):
        self.url = url
        self.image = plt.imread(image)
        self.data = pd.read_csv(self.url)
        self.formatting()
        
    # Format parameters for illustrations. Used as a preset for axis and title information.
    def formatting(self):
        self.titleFormat = {'size': 30, 'weight': 'bold', 'y': 1.03}
        self.labelFormat = {'size': 20, 'weight': 'bold'}
        self.labelFormatOut = {'size': 20, 'weight': 'bold', 'labelpad': 20}
    
    # Shows a map illustration of where the landslide reports occurred. 
    # Parameter [mag] - The magnitude of the landslide. Acceptable input below: 
    # ['all', 'small', 'medium', 'large', 'very_large', 'catastrophic']
    def map_illustrate(self, mag):
        self.m = 20
        self.map_info = self.data[['landslide_size', 'longitude', 'latitude']]
        if(mag != 'all'):
            self.map_info = self.map_info[self.map_info.landslide_size == mag]
        self.slideSize = lambda x: 1*self.m if x=='small' else (self.m*2 if x=='medium' else (4*self.m if x == 'large' else (6*self.m if x=='very_large' else (8*self.m if x=='catastrophic' else 1*self.m))))
        self.slideColor = lambda x: '#ffff00' if x=='small' else ('#ffa500' if x=='medium' else ((1,0,0) if x=='large' else('#800000' if x=='very_large' else('#4c00b0' if x=='catastrophic' else '#ffa500'))))
        self.fig, self.ax = plt.subplots()
        self.ax.imshow(self.image, extent = [-180, 180, -60, 90])
        self.ax.scatter(self.map_info.longitude, self.map_info.latitude, s=self.map_info.landslide_size.apply(self.slideSize), alpha=0.5, c=self.map_info.landslide_size.apply(self.slideColor))
        self.fig.set_size_inches(17.5, 10.5, forward=True)
        plt.title('Landslide Occurrences 2007 - 2017', **self.titleFormat)
        plt.xlabel('Longitude', **self.labelFormatOut)
        plt.ylabel('Latitude', **self.labelFormatOut)
        plt.xticks(fontsize = 12)
        plt.yticks(fontsize = 12)
        plt.show()
        
    # Shows the top x sources that the reports comes from. Organizes based on the amount of reports made per country. 
    def top_x_sources(self, x):
        self.countries = self.data[['country_name']].reset_index()
        self.total_val = self.countries.country_name.count()
        self.slides = self.countries.country_name.value_counts().sort_values(ascending=False)[:x].sort_values(ascending=True).reset_index()
        self.slides.columns = ['country_name', 'reports']
        plt.figure(figsize = (12, 7))
        plt.barh(self.slides.country_name, self.slides.reports, color=(0.8, 0, 0))
        plt.title('Top {} Reporting Countries'.format(x), **self.titleFormat)
        plt.xlabel('Amount of Reports', **self.labelFormatOut)
        plt.ylabel('Country', **self.labelFormatOut)
        plt.show()
        
    # Creates a visualization for the date occurrences of all the landslides
    def source_dates(self):
        plt.figure(figsize = (11, 8))
        self.findYear = lambda x: x.split(' ')[0].split('/')[-1]
        self.yearsList = self.data.event_date.apply(self.findYear).reset_index(drop=True)
        self.yearsList[self.yearsList > '2005'].value_counts().sort_index().plot(kind = 'bar', color=(0,0.8,0.8))
        plt.title('Highest Reporting Years', **self.titleFormat)
        plt.xlabel('Year', **self.labelFormatOut)
        plt.ylabel('Number of Reports', **self.labelFormatOut)
        plt.xticks(fontsize=12, rotation=30)
        plt.show()
                                                                                                                                   
lab = Landslide('Global_Landslide_Catalog_Export.csv', 'world_image_adjusted.PNG')
# lab.map_illustrate('all')
# lab.top_x_sources(20)
lab.source_dates()

