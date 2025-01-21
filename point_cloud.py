import open3d as o3d
import numpy as np
import cv2


def generate_point_cloud(rgb_image, depth_image, intrinsics):
    # Resize depth image to match the RGB image size
    depth_image_resized = cv2.resize(depth_image, (rgb_image.shape[1], rgb_image.shape[0]),
                                     interpolation=cv2.INTER_NEAREST)

    # Debug: Print the min and max values of the depth image
    print(f"Depth image min: {np.min(depth_image_resized)}, max: {np.max(depth_image_resized)}")

    # Convert to Open3D PointCloud
    depth_image_o3d = o3d.geometry.Image(depth_image_resized)
    rgb_image_o3d = o3d.geometry.Image(rgb_image)

    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
        rgb_image_o3d, depth_image_o3d, convert_rgb_to_intensity=False)

    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image, intrinsics)

    # Debug: Check the number of points in the point cloud
    print(f"Number of points in point cloud: {len(pcd.points)}")

    return pcd


def downsample_point_cloud(pcd, voxel_size=0.05):
    pcd_downsampled = pcd.voxel_down_sample(voxel_size)
    return pcd_downsampled