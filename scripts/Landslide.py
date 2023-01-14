import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

# Ideas - 
# 
# Create a categorical based on landslide trigger (what percentage causes the most landslides)
# Plot areas on a tableau map to show where the most landslides happen + size indicator


class Landslide:
  
    def __init__(self, url, image):
        self.url = url
        self.image = plt.imread(image)
        self.data = pd.read_csv(self.url)
        self.formatting()
        
    def formatting(self):
        self.titleFormat = {'size': 30, 'weight': 'bold', 'y': 1.03}
        self.labelFormat = {'size': 20, 'weight': 'bold'}
        self.labelFormatOut = {'size': 20, 'weight': 'bold', 'labelpad': 20}
    
    def map_illustrate(self):
        self.map_info = self.data[['landslide_size', 'longitude', 'latitude']]
        self.slideSize = lambda x: 25 if x == 'small' else (65 if x == 'medium' else 110)
        self.slideColor = lambda x: 'yellow' if x == 'small' else ('orange' if x == 'medium' else 'red')
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
    
lab = Landslide('Global_Landslide_Catalog_Export.csv', 'world_image_adjusted.PNG')
lab.map_illustrate()
