import random
import math
import numpy as np
from .. import geometry, three, color


def create_object(name, color=(1, 1, 1, 1), scale=(1, 1, 1)):
    vertices, faces = geometry.load("../../geometries/{}.obj".format(name))
    return three.Object(faces, vertices, color, scale), vertices, faces


def create_cornell_box(size=(7, 3, 7), color=(1, 1, 1, 1)):
    vertices, faces = geometry.load(
        "../../geometries/{}.obj".format("cornell_box"))
    return three.Object(faces, vertices, color, size)


def build_scene(
        room_size=(7, 4, 7),
        num_objects=3,
        object_names=["cube"],
        scale_range=(0.5, 1.0),
        placement_radius=2):
    scene = three.Scene()
    room = create_cornell_box(size=room_size)
    room_offset = room_size[1] / 2.0
    scene.add(room, position=(0, room_offset, 0))
    objects = []
    for _ in range(num_objects):
        objct_name = random.choice(object_names)
        scale = random.uniform(scale_range[0], scale_range[1])
        obj, vertices, _ = create_object(
            objct_name,
            scale=(scale, scale, scale),
            color=color.random_color())
        offset_y = (np.amin(vertices, axis=0) * scale)[1]
        theta = random.uniform(0, 2) * math.pi
        radius = random.uniform(0.5, 1) * placement_radius
        scene.add(
            obj,
            position=(radius * math.cos(theta), -offset_y,
                      radius * math.sin(theta)))
        objects.append(obj)
    return scene, room, objects
