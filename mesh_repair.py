import open3d as o3d

def repair_mesh(mesh):
    mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(mesh, depth=8)[0]
    mesh.remove_duplicated_vertices()
    mesh.remove_degenerate_triangles()
    return mesh
