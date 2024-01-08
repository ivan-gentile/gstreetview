APIKEY= "AIzaSyB41DRUbKWJHPxaFjMAwdrzWzbVKartNGg" 
output_dir= "output_gstreetview"

from gmap_retrieval import get_street_view_image
import pandas as pd
import urllib.request

data = pd.DataFrame({'id': [1, 2], 
                     'loc': ['40.752937,-73.977240', '51.531090,-0.125752'], 
                     'place': ['NYC Grand Central', 'London St Pancras']})
get_street_view_image(directory_name=f'{output_dir}/street_view', 
                      API_key=APIKEY, 
                      IDs=data['id'], 
                      latitude_longitude=data['loc'], 
                      n_images=10, 
                      search_radius=100, 
                      n_jobs=-1)
