import g2o
import numpy as np

class PoseGraphOptimization:
    def __init__(self):
        self.optimizer = g2o.SparseOptimizer()
        self.optimizer.set_verbose(True)

    def add_pose(self, pose_id, pose_matrix):
        pose = g2o.SlamVertexSE3()
        pose.set_id(pose_id)
        pose.set_estimate(pose_matrix)
        self.optimizer.add_vertex(pose)

    def add_edge(self, from_pose_id, to_pose_id, transformation_matrix, information_matrix):
        edge = g2o.SlamEdgeSE3()
        edge.set_vertex(0, self.optimizer.vertex(from_pose_id))
        edge.set_vertex(1, self.optimizer.vertex(to_pose_id))
        edge.set_measurement(transformation_matrix)
        edge.set_information(information_matrix)
        self.optimizer.add_edge(edge)

    def optimize(self, iterations=100):
        self.optimizer.initialize_optimization()
        self.optimizer.optimize(iterations)

    def get_optimized_poses(self):
        poses = []
        for vertex in self.optimizer.vertices():
            pose = vertex[1].estimate()
            poses.append(pose)
        return poses