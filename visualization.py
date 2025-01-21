import open3d as o3d

class RealTimeVisualizer:
    def __init__(self):
        self.vis = o3d.visualization.VisualizerWithKeyCallback()
        self.vis.create_window(window_name="3D Scanner")
        self.pcd = o3d.geometry.PointCloud()
        self.vis.add_geometry(self.pcd)
        self.is_running = False

    def update_point_cloud(self, pcd):
        self.pcd.points = pcd.points
        self.pcd.colors = pcd.colors
        self.vis.update_geometry(self.pcd)
        self.vis.poll_events()
        self.vis.update_renderer()

    def run(self):
        self.is_running = True
        while self.is_running:
            self.vis.poll_events()
            self.vis.update_renderer()

    def stop(self):
        self.is_running = False
        self.vis.destroy_window()