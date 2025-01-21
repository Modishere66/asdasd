import open3d as o3d

def save_mesh(mesh, path):
    o3d.io.write_triangle_mesh(path, mesh)

def save_point_cloud(pcd, path):
    o3d.io.write_point_cloud(path, pcd)