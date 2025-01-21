import open3d as o3d
from camera import Camera
from point_cloud import generate_point_cloud, downsample_point_cloud
from visualization import RealTimeVisualizer
from ui import ScannerUI
import threading
import numpy as np

class ScannerApp:
    def __init__(self):
        self.camera = Camera()
        self.visualizer = RealTimeVisualizer()
        self.ui = ScannerUI(self.start_scan, self.stop_scan)
        self.intrinsics = o3d.camera.PinholeCameraIntrinsic(
            o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault)
        self.scanning = False

    def start_scan(self):
        self.scanning = True
        self.capture_thread = threading.Thread(target=self.capture_frames)
        self.capture_thread.start()
        self.visualizer.run()

    def stop_scan(self):
        self.scanning = False
        self.capture_thread.join()
        self.visualizer.stop()

    def capture_frames(self):
        self.camera.initialize()
        while self.scanning:
            rgb, depth = self.camera.capture_frames()
            pcd = generate_point_cloud(rgb, depth, self.intrinsics)
            self.visualizer.update_point_cloud(pcd)

    def run(self):
        self.ui.run()

if __name__ == "__main__":
    app = ScannerApp()
    app.run()