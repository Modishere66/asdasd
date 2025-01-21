import open3d as o3d

def apply_texture_to_mesh(mesh, rgb_image):
    uv_map = compute_uv_map(mesh)  # Define a function to compute the UV map
    mesh.textures = [rgb_image]
    return mesh