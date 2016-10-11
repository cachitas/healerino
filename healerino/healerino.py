"""
Healerino
=========

"""

from kivy.app import App
from kivy.clock import Clock
from kivy.logger import Logger
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
    player = ObjectProperty(None)

    def start(self):
        Logger.info("Starting combat engine")

        Logger.info("Preparing your enemy")
        self.enemy.health = 50

        Logger.info("Preparing your party")
        self.party.prepare()

        Logger.info("Preparing yourself")


class Portrait(Widget):
    health = BoundedNumericProperty(100, min=0, max=100)
    role = OptionProperty("healer", options=["tank", "damager", "healer"])


class Enemy(Portrait):

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
        # TODO
        Logger.info("Party: initializing")
        for i in range(self.n):
            w = PartyMember()
            self.layout.add_widget(w)


class PartyMember(Portrait):
    pass


class Player(PartyMember):
    pass


class WelcomeScreen(Screen):
    pass


class FightScreen(Screen):

    fight = ObjectProperty(None)

    def on_enter(self):
        self.fight.start()

    # player = ObjectProperty()
    # party_members = ListProperty()
    # boss = ObjectProperty()

    # def on_enter(self):
    #     self.ids.cooldown_indicator.value = 0
    #     self.cd_refresh = Clock.schedule_interval(self.cooldown, 1./60.)
    #     self.regen = Clock.schedule_interval(self.player.regenerate, 1.0/30.0)

    # def on_leave(self):
    #     self.ids.cooldown_indicator.value = 0
    #     self.cd_refresh.cancel()

    # def cooldown(self, dt):
    #     indicator = self.ids.cooldown_indicator
    #     if indicator.value < indicator.max:
    #         indicator.value += 1
    #     else:
    #         indicator.value = 0


class HealerinoApp(App):
    # pass

    def build(self):
        # TODO just to test this widget
        # w = Enemy()
        w = FightWidget()
        w.start()
        return w


if __name__ == '__main__':
    HealerinoApp().run()
