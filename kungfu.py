# You are a Kung Fu master and a warring clan has killed your master. You go to their dojo
# in seek of vengeance. There are three floors in which you have to defeat, with their master
# at the top.

# Death
# One- Floor one
# Two- Floor two
# Three- Floor three, (boss)

# NOUNS
# Enemy
# Player
# Floor
# Map


# *Map
# - next_scene
# - opening_scene
# *Engine
# - Play
# *Scene
# - enter
#   *One
#   *Two
#   *Three

from sys import exit
from random import randint


class Scene(object):
    def enter(self):
        print "Undefined"
        exit(1)


class One(Scene):
    def enter(self):
        print "You come across your first Opponent. He tries to strike first."
        print "What do you do?"
        print "1) Counter his punch"
        print "2) Duck"
        print "3) Absorb the punch"

        action = raw_input("> ")

        if action == "1":
            print "You destroy him."
            Two()
        else:
            print "you suck"
            Death()


class Death(Scene):

    lines = {
        "You are dead.",
        "you suck.",
        "bye bye"
    }

    def enter(self):
        print Death.lines[randint(0, len(self.lines) - 1)]
        exit(1)


class Two(Scene):
    def enter(self):
        pass


class Three(Scene):
    def enter(self):
        pass


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.map.next_scene(next_scene_name)


class Map(object):

    scenes = {

        'one': One(),
        'two': Two(),
        'three': Three()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene):
        value = Map.scenes.get(scene)
        return value

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('one')
a_engine = Engine(a_map)
a_engine.play()