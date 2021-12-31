from BaguetteEngine import *

cube = [Application.Voxel(voxel_type = "model")]

paddle = [Application.Voxel(y=-1,voxel_type = "model"),
                    Application.Voxel(voxel_type = "model"),
                    Application.Voxel(y=1,voxel_type = "model")]

cup = [Application.Voxel(x=-2,y=3,voxel_type = "model"),Application.Voxel(x=-1,y=3,voxel_type = "model"),Application.Voxel(y=3,voxel_type = "model"),Application.Voxel(x=1,y=3,voxel_type = "model"),Application.Voxel(x=2,y=3,voxel_type = "model"),
              Application.Voxel(y=2,x=-2,voxel_type = "model"),Application.Voxel(y=2,x=-1,voxel_type = "model"),Application.Voxel(y=2,voxel_type = "model"),Application.Voxel(y=2,x=1,voxel_type = "model"),Application.Voxel(y=2,x=2,voxel_type = "model"),
              Application.Voxel(y=1,x=-1,voxel_type = "model"),Application.Voxel(y=1,voxel_type = "model"),Application.Voxel(y=1,x=1,voxel_type = "model"),
              Application.Voxel(y=0,voxel_type = "model"),
              Application.Voxel(y=-1,voxel_type = "model"),
              Application.Voxel(y=-2,voxel_type = "model"),
              Application.Voxel(y=-3,x=-1,voxel_type = "model"),Application.Voxel(y=-3,voxel_type = "model"),Application.Voxel(y=-3,x=1,voxel_type = "model")]
