import depthai as dai
import numpy as np
import cv2


class Camera:
    def __init__(self):
        self.pipeline = dai.Pipeline()
        self.device = None
        self.q_rgb = None
        self.q_depth = None

    def initialize(self):
        # Create pipeline for the Oak-D Lite
        cam_rgb = self.pipeline.createColorCamera()
        cam_rgb.setBoardSocket(dai.CameraBoardSocket.RGB)
        cam_rgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
        cam_rgb.setFps(30)

        # Create mono cameras for depth stream
        cam_left = self.pipeline.createMonoCamera()
        cam_left.setBoardSocket(dai.CameraBoardSocket.LEFT)
        cam_left.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)

        cam_right = self.pipeline.createMonoCamera()
        cam_right.setBoardSocket(dai.CameraBoardSocket.RIGHT)
        cam_right.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)

        # Create depth stream
        cam_depth = self.pipeline.createStereoDepth()
        cam_depth.setConfidenceThreshold(255)
        cam_depth.setLeftRightCheck(True)
        cam_depth.setSubpixel(True)

        # Link mono cameras to depth stream
        cam_left.out.link(cam_depth.left)
        cam_right.out.link(cam_depth.right)

        # Create XLinkOut nodes for RGB and depth streams
        xout_rgb = self.pipeline.createXLinkOut()
        xout_rgb.setStreamName("rgb")
        cam_rgb.video.link(xout_rgb.input)

        xout_depth = self.pipeline.createXLinkOut()
        xout_depth.setStreamName("depth")
        cam_depth.depth.link(xout_depth.input)

        # Start pipeline
        self.device = dai.Device(self.pipeline)

        # Create output queues
        self.q_rgb = self.device.getOutputQueue(name="rgb", maxSize=8, blocking=False)
        self.q_depth = self.device.getOutputQueue(name="depth", maxSize=8, blocking=False)

    def capture_frames(self):
        while True:
            frame_rgb = self.q_rgb.get()
            frame_depth = self.q_depth.get()

            rgb_frame = frame_rgb.getCvFrame()
            depth_frame = frame_depth.getFrame()

            # Debugging: Check the contents of the depth frame
            print(f"Depth frame data type: {depth_frame.dtype}, shape: {depth_frame.shape}")

            yield rgb_frame, depth_frame