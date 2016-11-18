# testing out how calling functions work


class LivingRoom(object):

    def enter(self):
        print "you are in the living room"
        print "go to the kitchen"
        return 'kitchen'


class Kitchen(object):

    def enter(self):
        print"you are in the kitchen"
        print "we are going to wrap up"
        return 'finished'


class Finished(object):

    def enter(self):
        print "we are done now"
        return 'finished'


class Map(object):

    scenes = {
        'living_room': LivingRoom(),
        'kitchen': Kitchen(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        # inputs 'hey' as parameter
        return self.next_scene(self.start_scene)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

# what is difference between the current_scene above and below this line?
        while current_scene != last_scene:
            # figure out ".enter()"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

a_map = Map('living_room')
a_game = Engine(a_map)
a_game.play()