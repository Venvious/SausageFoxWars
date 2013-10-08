import Zero
import Events
import Property
import VectorMath

Vec3 = VectorMath.Vec3

class MapCreate:
    def Initialize(self, initializer):
        # SIZE:
        # 42 x 42 is the biggest square plausable for Zero
        self.xsize = 30
        self.ysize = 14
        
        # END:
        # (Make sure it is within the size bounds)
        self.endx = 2
        self.endy = 3
        
        # SPWN:
        # (Make sure it is within the size bounds)
        self.spwnx = 20
        self.spwny = 6
        
        # Place those magnificent sprites
        self.node_array = [[[0] * self.ysize for i in range(self.ysize)][0] * self.xsize for i in range(self.xsize)]
        
        for i in range(self.xsize):
            for j in range(self.ysize):
                # BORDER:
                if(i == 0 or i == self.xsize - 1 or j == 0 or j == self.ysize - 1):
                    wall = self.Space.CreateAtPosition("Wall", Vec3(i, 0 - j, 0))
                    
                # END:
                elif(i == self.endx and j == self.endy):
                    end = self.Space.CreateAtPosition("End", Vec3(i, 0 - j, 0))
                    
                # SPWN:
                elif(i == self.spwnx and j == self.spwny):
                    spwn = self.Space.CreateAtPosition("EnemySpawner", Vec3(i, 0 - j, 0))
                    
                # EMPTY:
                else:
                    cell = self.Space.CreateAtPosition("Cell", Vec3(i, 0 - j, 0))
                    
        

Zero.RegisterComponent("MapCreate", MapCreate)