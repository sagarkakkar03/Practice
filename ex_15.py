class alien(object):
    pass 

class ship(object):
    pass 

class scene(object):
    def enter(self):
        print('This is not yet developed') 

class gothom(object):
    pass 

class escape_pod(scene):
    pass 

class planet(object):
    pass 

class engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        self.scene_map.opening_scene()

class death(scene):
    def enter(self):
        pass  

class central_corridor(scene):
    def enter(self):
        print('game begins')
        return 'laser_weapon_armory'

class laser_weapon_armory(scene):
    def enter(self):
        print('laser')
        return 'bridge'

class bridge(scene):
    def enter(self):
        print('bridge')
        return 'finished' 

class finished(scene):
    def enter(self):
        print('game finished') 

    
class map(object):
    scenes = {
        'central_corridor': central_corridor(),
        'laser_weapon_armory': laser_weapon_armory(),
        'death': death(),
        'bridge': bridge(),
        'finished': finished()
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = map.scenes.get(scene_name).enter()
        if val in self.scenes:
            self.next_scene(val)
        return val 

    def opening_scene(self):
        self.next_scene(self.start_scene)




a_map = map('central_corridor')
a_game = engine(a_map)
a_game.play()