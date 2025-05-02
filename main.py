# This is the main file where you control your bot's strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits

# Hi! Corbin here. Note the line below says GoslingUtils in the videos.
# DO NOT change the line below. It's no longer compatible with GoslingUtils so we renamed it.
# There are a few places like this where the code that you started with (the code you downloaded) might
# look different than the videos. THAT'S OK! Don't change it. We've made it better over time.
# Just follow along with the videos and it will all work the same.
class Bot(BotCommandAgent):
    # This function runs every in-game tick (every time the game updates anything)

    def run(self):
        if self.get_intent() is not None:
            return

        # self.print_debug()
        target_boost = self.get_closest_large_boost()
        distance_difference = 5120 + abs(self.me.location.y)
        retreat_distance = 0

        def find_best_shot():
            targets = {
                'at_opponent_goal': (self.foe_goal.left_post, self.foe_goal.right_post),
                'away_from_our_net': (self.friend_goal.right_post, self.friend_goal.left_post)
            }
            hits = find_hits(self, targets)
            if len(hits['at_opponent_goal']) > 0:
                self.set_intent(hits['at_opponent_goal'][0])
                return
            if len(hits['away_from_our_net']) > 0:
                self.set_intent(hits['away_from_our_net'][0])
                return





        # white = self.renderer.white()
        # self.renderer.draw_line_3d(self.me.location, self.ball.location, white)
        #if self.get_intent() is not None:
        #self.debug_intent()
            #return
        if self.kickoff_flag:
            # self.clear_debug_lines()
            self.set_intent(kickoff())
            # self.debug_intent()
            # self.add_debug_line('me_to_kickoff', self.me.location, self.ball.location, [0, 0, 255])
            # self.add_debug_line('kickoff_to_goal', self.ball.location, self.foe_goal.location, [0, 0, 255])
            return

        # self.clear_debug_lines()

# set_intent tells the bot what it's trying to do
        if self.is_in_front_of_ball():
            if distance_difference < 10200:
                retreat_distance = 500
            elif distance_difference >= 10200:
                retreat_distance = 50
            y_value_recovery = self.ball.location.y - (retreat_distance)
            retreat_location = Vector3(self.ball.location.x, y_value_recovery, 0)
            if abs(y_value_recovery) >= 5110:
                self.set_intent(atba())
            else:
                self.set_intent(goto(retreat_location))
                # self.debug_text = 'retreating'
                # self.add_debug_line('retreat', self.me.location, retreat_location, [255, 0, 0])
                # self.debug_intent()
            return



        ball_to_friendgoal = (self.ball.location - self.friend_goal.location).magnitude()

        if ball_to_friendgoal < 1000:
            self.set_intent(goto(self.friend_goal.location))
            self.set_intent(short_shot(self.foe_goal.location))
            return

        if self.me.boost > 90:
            shot_location = self.foe_goal.location
            self.set_intent(short_shot(shot_location))
            # self.debug_text = 'shooting'
            # self.add_debug_line('me_to_ball', self.me.location, self.ball.location, [0, 0, 255])
            # self.add_debug_line('ball_to_net', self.ball.location, shot_location, [0, 0, 255])
            # self.debug_intent()
            return
        if  target_boost is not None and self.me.boost < 10 and self.get_intent() is None:
            boost_location = target_boost.location
            self.set_intent(goto(boost_location))
            # self.debug_text = 'getting boost'
            # self.add_debug_line('getting boost', self.me.location, boost_location, [0, 255, 0])
            # self.debug_intent()
            # return

        find_best_shot()

        # targets = {
        #     'at_opponent_goal': (self.foe_goal.left_post, self.foe_goal.right_post),
        #     'away_from_our_net': (self.friend_goal.right_post, self.friend_goal.left_post)
        # }
        # hits = find_hits(self, targets)
        # if len(hits['at_opponent_goal']) > 0:
        #     self.set_intent(hits['at_opponent_goal'][0])
        #     return
        # if len(hits['away_from_our_net']) > 0:
        #     self.set_intent(hits['away_from_our_net'][0])
        #     return

        #############

        if self.ball.location.z - 10 > self.me.location.z and self.ball.location.x <= self.me.location.x + 100 and self.ball.location.y <= self.me.location.z + 200:
           self.set_intent(jump_shot(self.ball.location, self.time, self.foe_goal.location, 3))
           return

        # if len(available_boosts) > 0:
        #     self.set_intent(goto(available_boosts[0].location))
        #     return



        # targets = {
        #     'at_opponent_goal': (self.foe_goal.left_post, self.foe_goal.right_post),
        #     'away_from_our_net': (self.friend_goal.right_post, self.friend_goal.left_post)
        # }
        # hits = find_hits(self, targets)
        # if len(hits['at_opponent_goal']) > 0:
        #     self.set_intent(hits['at_opponent_goal'][0])
        #     return
        # if len(hits['away_from_our_net']) > 0:
        #     self.set_intent(hits['away_from_our_net'][0])
           # return

        # # if we're in front of the ball, retreat
        # if is_in_front_of_ball:
        #     self.set_intent(goto(self.friend_goal.location))
        #     return
        # self.set_intent(short_shot(self.foe_goal.location))


#print(f'my x position is: {self.me.location.x}')



