"""
Healerino
=========

"""

import random

from kivy.app import App
from kivy.clock import Clock
from kivy.logger import Logger
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import NumericProperty
from kivy.properties import OptionProperty
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty
from kivy.properties import BoundedNumericProperty
from kivy.properties import StringProperty


# class PlayerWidget(Widget):
#     mana = BoundedNumericProperty(50, min=0, max=100)
#     mana_regen_rate = NumericProperty(0.1)

#     def regenerate(self, dt):
#         if self.mana < self.property('mana').get_max(self):
#             self.mana += self.mana_regen_rate


# class SpellWidget(Button):
#     name = StringProperty("Spell")
#     description = StringProperty("A spell that costs nothing and does nothing")
#     cost = NumericProperty(0)
#     power = NumericProperty(0)

#     caster = ObjectProperty(None)
#     target = ObjectProperty(None)

#     def on_press(self):
#         if self.caster.mana > self.cost:
#             Logger.info("%s casts '%s' on %s",
#                         self.caster, self.name, self.target)
#             self.caster.mana -= self.cost
#         else:
#             Logger.info("Not enough mana")


class FightWidget(Widget):

    enemy = ObjectProperty(None)
    party = ObjectProperty(None)
    # player = ObjectProperty(None)

    def start(self):
        Logger.info("Starting combat engine")

        Logger.info("Preparing your enemy")
        self.enemy.health = 50
        self.enemy.power = 10
        self.enemy_move_event = Clock.create_trigger(self.enemy_move, 1.0)

        Logger.info("Preparing your party")
        self.party.prepare()
        # TODO party moves

        Logger.info("Preparing yourself")
        # TODO your healing abilities

    def update(self, dt):
        Logger.info("Update: %s", dt)
        self.enemy_move_event()

    def enemy_move(self, dt):
        # TODO focus tanks
        target = self.party.get_random_member()
        if target is None:
            Logger.info("Party died")
            self.cleanup()
        else:
            Logger.info("Attacking party member %s", target)
            self.enemy.attack(target)

    def cleanup(self):
        # TODO game over pop up before returning to main menu
        self.enemy_move_event.cancel()
        Clock.unschedule(self.update)
        self.parent.manager.current = 'welcome_screen'


class Portrait(Widget):
    health = BoundedNumericProperty(100, min=0, max=100)
    role = OptionProperty("healer", options=["tank", "damager", "healer"])
    power = NumericProperty(1)

    def is_alive(self):
        return self.health > 0


class Enemy(Portrait):

    def attack(self, target):
        target.health -= self.power

    def heal(self, amount):
        Logger.info("HP %d <-- healing for %d", self.health, amount)
        try:
            self.health += amount
        except ValueError:
            pass


class Party(Widget):
    n = NumericProperty(3)
    layout = ObjectProperty(None)

    def prepare(self):
        Logger.info("Party: initializing")
        for i in range(self.n):
            w = PartyMember(health=20)
            self.layout.add_widget(w)

    def get_member(self, index):
        return self.layout.children[index]

    def get_random_member(self):
        alive_members = [
            member
            for member in self.layout.children
            if member.is_alive()
        ]
        if alive_members:
            return random.choice(alive_members)
        else:
            return None


class PartyMember(Portrait):

    def __repr__(self):
        return "PartyMember(role=%s, health=%d)" % (self.role, self.health)


class Player(PartyMember):
    pass


class WelcomeScreen(Screen):
    pass


class FightScreen(Screen):

    fight = ObjectProperty(None)

    def on_enter(self):
        self.fight.start()
        # self.fight.update()
        self.update = Clock.schedule_interval(self.fight.update, 1.0 / 4.0)

    def on_leave(self):
        self.fight.cleanup()
        self.update.cancel()


class HealerinoApp(App):
    pass

    # def build(self):
    #     # TODO just to test this widget
    #     # w = Enemy()
    #     # return w

    #     # w = FightWidget()
    #     # w.start()
    #     # return w

    #     sm = ScreenManager()
    #     s = FightScreen()
    #     sm.add_widget(s)
    #     return sm


if __name__ == '__main__':
    HealerinoApp().run()
