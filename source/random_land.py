import bpy
import random


defmap = [[[1]*10 for i in range(10)] for j in range(10)]

for x in range(10):
    for y in range(10):
        for z in range(10):
            if(random.randint(0,2)==0):
                defmap[x][y][z] = 0;

for z in range(10):
    for y in range(10):
        for x in range(10):
            if(random.randint(0,2)==0):
                bpy.ops.mesh.primitive_cube_add(location(x*2,y*2,z*2))

