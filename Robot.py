

class robot:
    position = [0, 0, 'NORTH']
    

    def ifValid(self, x):
        if (x >= 0) and (x <= 4):
            return True
        
        return False
    
    
    def move(self):
        
        if self.position[2] == 'WEST':
            if self.ifValid(self.position[0] - 1) == True:
                self.position[0] = self.position[0] - 1
                return True
        
        elif self.position[2] == 'EAST':
            if self.ifValid(self.position[0] + 1) == True:
                self.position[0] = self.position[0] + 1
                return True
                
        elif self.position[2] == 'NORTH':
            if self.ifValid(self.position[1] + 1) == True:
                self.position[1] = self.position[1] + 1
                return True
                
        elif self.position[2] == 'SOUTH':
            if self.ifValid(self.position[1] - 1) == True:
                self.position[1] = self.position[1] - 1
                return True
                
        return False
    
    
    
    def left(self):
        
        if self.position[2] == 'NORTH':
            self.position[2] = 'WEST'
            return True
        
        if self.position[2] == 'WEST':
            self.position[2] = 'SOUTH'
            return True
        
        if self.position[2] == 'SOUTH':
            self.position[2] = 'EAST'
            return True
        
        if self.position[2] == 'EAST':
            self.position[2] = 'NORTH'
            return True
        
        return False
    
    
    
       
    def right(self):
        
        if self.position[2] == 'NORTH':
            self.position[2] = 'EAST'
            return True
        
        if self.position[2] == 'WEST':
            self.position[2] = 'NORTH'
            return True
        
        if self.position[2] == 'SOUTH':
            self.position[2] = 'WEST'
            return True
        
        if self.position[2] == 'EAST':
            self.position[2] = 'SOUTH'
            return True
        
        return False
    
    


    def place(self, post):
        if self.ifValid(post[0]) == True and self.ifValid(post[1]) == True:
            self.position = post
            return True
        else:
            return False
    
    
    
    
    def report(self):
        print(str(self.position[0]) + ',' + str(self.position[1]) + ',' + self.position[2])
        return True
 