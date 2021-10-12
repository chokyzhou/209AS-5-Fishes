import numpy as np
from gridworld_setup import GridWorld
import random

grid = GridWorld()

#just a helper function for plotting
def draw_square(array):
    print("--------------------------")
    for i in range(grid.gridSize):
        sth = []
        for j in range(grid.gridSize):
            sth.append(array[5*i+j])
        print(sth)
    print("--------------------------")
    return None

def draw_action(array):
    symbol_array = []
    for i in range(len(array)):
        if array[i] == 0:
            symbol_array.append(u'\u2191')
        elif array[i] == 1:
            symbol_array.append(u'\u2193')
        elif array[i] == 2:
            symbol_array.append(u'\u2190')
        elif array[i] == 3:
            symbol_array.append(u'\u2192')
        elif array[i] == 4:
            symbol_array.append(u'\u2298')
    return symbol_array


def reward_function(Rd, Rs, Rw): 
    reward_map = []
    for state_ in grid.stateSpace:
        if_wall = (grid.wall == state_).all(1).any()
        if_block = (grid.blockSpace == state_).all(1).any()
        if_target = (grid.target == state_).all(1).any()
        if if_wall == True:
            reward_map.append(Rw)
        elif if_target == True:
            if np.array_equal(state_,grid.target[0]):
                reward_map.append(Rs)
            else:
                reward_map.append(Rd)
        elif if_block == True:
            reward_map.append(-99) #trivial value, wont consider block in calculation since transition probability is always 0
        else:
            reward_map.append(0)
    return reward_map

def get_available_actions():
    available_action_each_state = []
    for state_ in grid.stateSpace:
        available_action_at_state = []
        if_block_state = (grid.blockSpace == state_).all(1).any()
        if if_block_state == True:
            available_action_each_state.append([4]) #stay
        else:
            for action_index in range(len(grid.actionSpace)):
                next_state = state_ + grid.actionSpace[action_index]
                if_in_block = (grid.blockSpace == next_state).all(1).any()
                if_in_bound = (grid.stateSpace == next_state).all(1).any()
                if if_in_block == False and if_in_bound == True:
                    available_action_at_state.append(action_index)
            available_action_each_state.append(available_action_at_state)
    return np.array(available_action_each_state)


def setup_random_policy(availble_actions):
    policy_map =[]
    for i in range(len(grid.stateSpace)):
        viable_action_set = availble_actions[i]
        pick_random_action = np.random.choice(viable_action_set)
        policy_map.append(pick_random_action)
    return np.array(policy_map)




def policy_function_iteration(discount, reward):
    '''
    Policy Evaluation:
        for each state, use policy to give an action
            for that action, calculate its corresponding v-value
    
    Policy Refinement:
        policy can be improved, by find the action that will maximize the q-value 
    '''
    available_action_set = get_available_actions()
    previous_policy = setup_random_policy(available_action_set)
    initial_policy = setup_random_policy(available_action_set)

    v_i  = reward

    epoch = 0
    while np.array_equal(previous_policy,initial_policy) == False:
        #For policy evaluation:
        for state_index in range(len(grid.stateSpace)):
            v_pi_s_prime = 0
            for action_ in available_action_set[state_index]:
                transit_prob_given_action_state = grid.transition_probability[action_][state_index]
                successor_state = grid.stateSpace[state_index]+grid.actionSpace[action_]
                successor_state_index = successor_state[0]*5+successor_state[1]

                reward_given_action_state = reward[successor_state_index]

                v_s = reward_given_action_state 
                + discount*np.sum(np.multiply(transit_prob_given_action_state,v_i[successor_state_index]))

                v_pi_s_prime = v_s + v_pi_s_prime
            v_pi_s_prime = v_pi_s_prime/len(available_action_set[state_index]) #for this problem particularly,
            #probability of picking an action from available actionset is equal

            #update v_i
            v_i[state_index] = v_pi_s_prime
        
        #For policy refinement:
        for state_index in range(len(grid.stateSpace)):
            q_temp = []
            for action_ in available_action_set[state_index]:
                transit_prob_given_action_state = grid.transition_probability[action_][state_index]
                successor_state = grid.stateSpace[state_index]+grid.actionSpace[action_]
                successor_state_index = successor_state[0]*5+successor_state[1]
                reward_given_action_state = reward[successor_state_index]

                q_state_action = reward_given_action_state 
                + discount*np.sum(np.multiply(transit_prob_given_action_state,v_i[successor_state_index]))

                q_temp.append(q_state_action)
            q_max_index = np.argmax(q_temp)
            policy_at_that_state = available_action_set[state_index][q_max_index]

            #update policy
            previous_policy[state_index] = initial_policy[state_index]
            initial_policy[state_index] = policy_at_that_state

        epoch +=1
        draw_square(draw_action(previous_policy))
        draw_square(draw_action(initial_policy))
        print(epoch)
        
    
    
    return initial_policy, previous_policy
        



#     return NotImplementedError

if __name__ == "__main__":
    available_action = get_available_actions()
    #print(available_action)

    # previous_policy = setup_random_policy(available_action)
    # initial_policy = setup_random_policy(available_action)
    # draw_square(previous_policy)
    # draw_square(initial_policy)
    reward = reward_function(1,10,-1)
    initial_p, previous_p = policy_function_iteration(0.9,reward)
    draw_square(draw_action(initial_p))

