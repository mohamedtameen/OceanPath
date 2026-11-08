
import os
import pickle

files = [
    "objects/num_cols_per_row2.pkl",
    "objects/all_points2.pkl",
    "objects/grid_cells2.pkl",
    "objects/points_to_ind2.pkl",
    "objects/grid2.pkl",
    "objects/points_to_bathy2.pkl",
    "objects/weather_grid.pkl",
]

for path in files:
    print(f"\nChecking: {path}", flush=True)

    if not os.path.exists(path):
        print("File not found!", flush=True)
        break

    try:
        with open(path, "rb") as f:
            data = pickle.load(f)

        print(f"Loaded successfully: {type(data)}", flush=True)
        del data

    except Exception as e:
        print(f"Failed: {type(e).__name__}: {e}", flush=True)
        break
