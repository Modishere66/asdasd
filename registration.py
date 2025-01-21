import open3d as o3d
import numpy as np

def icp_registration(source_pcd, target_pcd, threshold=0.02):
    reg_icp = o3d.registration.registration_icp(
        source_pcd, target_pcd, threshold, np.eye(4),
        o3d.registration.TransformationEstimationPointToPlane())
    return reg_icp.transformation

def multi_resolution_registration(source_pcd, target_pcd, voxel_sizes=[0.05, 0.02, 0.01]):
    current_transformation = np.eye(4)
    for voxel_size in voxel_sizes:
        source_downsampled = source_pcd.voxel_down_sample(voxel_size)
        target_downsampled = target_pcd.voxel_down_sample(voxel_size)
        current_transformation = icp_registration(source_downsampled, target_downsampled, threshold=voxel_size * 1.5)
        source_pcd.transform(current_transformation)
    return current_transformation