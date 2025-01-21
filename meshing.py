import open3d as o3d

def create_mesh_from_point_cloud(pcd):
    mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=9)
    return mesh

def simplify_mesh(mesh, target_faces=10000):
    mesh_simplified = mesh.simplify_quadric_decimation(target_faces)
    return mesh_simplified

def fill_mesh_holes(mesh):
    mesh.remove_duplicated_vertices()
    mesh.remove_degenerate_triangles()
    mesh.remove_non_manifold_edges()
    return mesh