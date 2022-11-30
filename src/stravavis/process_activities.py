import pandas as pd

def process_activities(activities_path, local_timezone=None):
    # Import activities.csv from Strava bulk export zip
    activities = pd.read_csv(activities_path)
    
    # Convert activity start date to datetime
    activities['Activity Date'] = pd.to_datetime(activities['Activity Date'])
    
    # Convert to local timezone (if given)
    if local_timezone:
        activities['Activity Date'] = (pd.to_datetime(activities['Activity Date'])
                                       .dt.tz_localize(tz='UTC', nonexistent='NaT', ambiguous='NaT')
                                       .dt.tz_convert(local_timezone))
    
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