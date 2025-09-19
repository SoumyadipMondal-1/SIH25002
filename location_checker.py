from shapely.geometry import Point, Polygon

# Define the zones 
zones = [
    {
        "name": "RED",
        "priority": 3,
        "polygon": Polygon([
            # lon       lat
            (88.45294, 22.98805),
            (88.45321, 22.98799),
            (88.45361, 22.98892),
            (88.45332, 22.98902),
            (88.45294, 22.98805)  
        ])
    },
    {
        "name": "GREEN",
        "priority": 2,
        "polygon": Polygon([
            (88.45272, 22.98816),
            (88.45285, 22.9881),
            (88.45323, 22.98905),
            (88.45309, 22.9891),
            (88.45272, 22.98816)  
        ])
    },
    {
        "name": "YELLOW",
        "priority": 1,
        "polygon": Polygon([
            (88.45285, 22.9881),
            (88.45295, 22.98808),
            (88.45332, 22.98902),
            (88.45323, 22.98905),
            (88.45285, 22.9881)  
        ])
    }
]

def detect_zone(lat, lon):
    point = Point(lon, lat)
    matched = []

    for zone in zones:
        if zone["polygon"].contains(point) or zone["polygon"].touches(point):
            matched.append(zone)

    if not matched:
        return None
    return max(matched, key=lambda z: z["priority"])["name"]

if __name__ == "__main__":
    print("Zone checker running... Enter coordinates one by one.")
    print("Priority: RED > GREEN > YELLOW")
    print("Press CTRL+C to stop\n")

    while True:
        try:
            lat_raw = input("Enter latitude : ").strip()
            lon_raw = input("Enter longitude: ").strip()

            if not lat_raw or not lon_raw:
                print("Both latitude and longitude are required.")
                continue

            lat, lon = map(float, (lat_raw, lon_raw))
            zone = detect_zone(lat, lon)

            if zone:
                print(f"You are in the {zone} zone\n")
            else:
                print("You are in SAFE zone (outside all polygons)\n")
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}\n")
