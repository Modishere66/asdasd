import os


def create_data_directories(base_dir="data_saved"):
    subdirs = ["point_clouds", "meshes", "textures", "depth_maps", "rgb_images"]

    # Create the base directory if it doesn't exist
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Create subdirectories
    for subdir in subdirs:
        subdir_path = os.path.join(base_dir, subdir)
        if not os.path.exists(subdir_path):
            os.makedirs(subdir_path)
            print(f"Created directory: {subdir_path}")
        else:
            print(f"Directory already exists: {subdir_path}")


if __name__ == "__main__":
    create_data_directories()