import folium
from shapely import wkt
from shapely.geometry import mapping
import pandas as pd
import re

def parse_multilinestring(text):
    # Extract coordinates from MULTILINESTRING format
    # Find all coordinates using regex
    pattern = r'-?\d+\.\d+\s+-?\d+\.\d+'
    matches = re.findall(pattern, text)
    
    # Convert matches to coordinate pairs
    coordinates = []
    for match in matches:
        lon, lat = map(float, match.split())
        coordinates.append([lon, lat])
    
    return coordinates

def create_map_from_routes(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Create a base map centered on Chicago
    m = folium.Map(location=[41.8781, -87.6298], zoom_start=11)
    
    # Different colors for different routes
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 
              'lightred', 'darkblue', 'darkgreen', 'cadetblue']
    
    # Process each route
    for idx, row in df.iterrows():
        try:
            # Parse the coordinates
            coordinates = parse_multilinestring(row.iloc[0])  # First column contains MULTILINESTRING
            
            # Get route number from the 'ROUTE' column (adjust column name if different)
            route_number = row['ROUTE'] if 'ROUTE' in df.columns else f"Route {idx}"
            route_name = row['ROUTE_NAME'] if 'ROUTE_NAME' in df.columns else ""
            
            # Create tooltip with route info
            tooltip = f"Route {route_number}: {route_name}"
            
            # Create a polyline for the route
            color = colors[idx % len(colors)]  # Cycle through colors
            folium.PolyLine(
                locations=[[lat, lon] for lon, lat in coordinates],
                weight=2,
                color=color,
                opacity=0.8,
                tooltip=tooltip
            ).add_to(m)
            
        except Exception as e:
            print(f"Error processing route {idx}: {e}")
    
    return m

def main():
    # Create the map
    m = create_map_from_routes('CTA_-_Bus_Routes_20250224.csv')
    
    if m:
        # Save the map to an HTML file
        output_file = 'bus_routes_map.html'
        m.save(output_file)
        print(f"Map has been saved to {output_file}")

if __name__ == "__main__":
    main()