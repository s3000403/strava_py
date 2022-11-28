import pandas as pd

def process_activities(activities_path):
    # Import activities.csv from Strava bulk export zip
    activities = pd.read_csv(activities_path)
    
    # Further processing (to come)
    
    return activities

def add_activities( raw_data, activities ):
    combined = raw_data.merge(
                              right=activities,
                              how='outer',
                              left_on='actid',
                              right_on='Activity ID',
                              )
    return combined