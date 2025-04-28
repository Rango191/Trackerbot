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
        self.print_debug()
        # white = self.renderer.white()
        # self.renderer.draw_line_3d(self.me.location, self.ball.location, white)
        if self.get_intent() is not None:
            self.debug_intent()
            return
        


        
        # d1 = abs(self.ball.location.y - self.foe_goal.location.y)
        # d2 = abs(self.me.location.y - self.foe_goal.location.y)
        # is_in_front_of_ball = d1 > d2

# set_intent tells the bot what it's trying to do
        if self.kickoff_flag:
            self.clear_debug_lines()
            self.set_intent(kickoff())
            self.add_debug_line('me_to_kickoff', self.me.location, self.ball.location, [0, 0, 255])
            self.add_debug_line('kickoff_to_goal', self.ball.location, self.foe_goal.location, [0, 0, 255])
            return
        
        self.clear_debug_lines()
        if self.is_in_front_of_ball():
            retreat_location = self.friend_goal.location
            self.set_intent(goto(retreat_location))
            self.debug_text = 'retreating'
            self.add_debug_line('retreat', self.me.location, retreat_location, [255, 0, 0])
            return
        
        if self.me.boost > 99:
            shot_location = self.foe_goal.location
            self.set_intent(short_shot(shot_location))
            self.debug_text = 'shooting'
            self.add_debug_line('me_to_ball', self.me.location, self.ball.location, [0, 0, 255])
            self.add_debug_line('ball_to_net', self.ball.location, shot_location, [0, 0, 255])
            return

        target_boost = self.get_closest_large_boost()
        if target_boost is not None:
            boost_location = target_boost.location
            self.set_intent(goto(boost_location))
            self.debug_text = 'getting boost'
            self.add_debug_line('getting boost', self.me.location, boost_location, [0, 255, 0])
            return
        
        # if len(available_boosts) > 0:
        #     self.set_intent(goto(available_boosts[0].location))
        #     return
        
        
        """
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
        """
        # # if we're in front of the ball, retreat
        # if is_in_front_of_ball:
        #     self.set_intent(goto(self.friend_goal.location))
        #     return
        # self.set_intent(short_shot(self.foe_goal.location))


#print(f'my x position is: {self.me.location.x}')



