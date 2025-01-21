import open3d as o3d

def save_point_cloud(pcd, path):
    o3d.io.write_point_cloud(path, pcd)

def load_point_cloud(path):
    return o3d.io.read_point_cloud(path)

def save_mesh(mesh, path):
    o3d.io.write_triangle_mesh(path, mesh)

def load_mesh(path):
    return o3d.io.read_triangle_mesh(path)