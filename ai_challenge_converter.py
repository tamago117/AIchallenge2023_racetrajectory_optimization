import numpy as np
import pandas as pd

# Load the provided CSV files
outer_track_path = 'converted_inner_track_line.csv'
inner_track_path = 'converted_outer_track_line.csv'

# Function to calculate the center and width of the track
def calculate_track_center_and_width_corrected(outer_track, inner_track):
    # Extracting x and y coordinates
    outer_x = outer_track['x']
    outer_y = outer_track['y']
    inner_x = inner_track['x']
    inner_y = inner_track['y']

    # Calculating the center points
    center_x = (outer_x + inner_x) / 2
    center_y = (outer_y + inner_y) / 2

    # Calculating the width (distance) between the outer and inner track
    width = np.sqrt((outer_x - inner_x)**2 + (outer_y - inner_y)**2)

    return pd.DataFrame({
        'x_m': center_x,
        'y_m': center_y,
        'w_tr_right_m': width / 2,  # Assuming the width is evenly divided
        'w_tr_left_m': width / 2
    })

# Defining column names
column_names = ['x', 'y', 'z', 'yaw']

# Re-load the CSV files with column names
outer_track_df = pd.read_csv(outer_track_path, names=column_names, header=0)
inner_track_df = pd.read_csv(inner_track_path, names=column_names, header=0)

print(outer_track_df.head(), inner_track_df.head())

# Recalculate the track center and width with the correct format
track_center_width_corrected_df = calculate_track_center_and_width_corrected(outer_track_df, inner_track_df)

# Define the output path
output_corrected_path = './inputs/tracks/ai_challenge.csv'

# Define the custom header string
custom_header = '# x_m, y_m, w_tr_right_m, w_tr_left_m\n'

# Open the file in write mode and write the custom header
with open(output_corrected_path, 'w') as f:
    f.write(custom_header)

    # Append the DataFrame content without the default header
    track_center_width_corrected_df.to_csv(f, index=False, header=False)