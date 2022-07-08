import random
import time


class Thing:
    

    def is_alive(self):
        return hasattr(self, 'alive') and self.alive

    def show_state(self):
        print("I don't know how to show_state.")


class Agent(Thing):

    def __init__(self, program=None):
        self.alive = True
        self.performance = 0
        self.program = program

    def can_grab(self, thing):
        return False

def TableDrivenAgentProgram(table):
    percepts = []

    def program(percept):
        percepts.append(percept)
        action=table.get(tuple(percept))
        return action

    return program

loc_A, loc_B, loc_C, loc_D, loc_E, loc_F = (0,0), (0,1), (0,2), (1,2), (1,1), (1,0) 

def TableDrivenVacuumAgent():
    table = {(loc_A, 'Clean'): 'Right1',
             (loc_A, 'Dirty'): 'Suck',
             (loc_B, 'Clean'): 'Right2',
             (loc_B, 'Dirty'): 'Suck',
             (loc_C, 'Clean'): 'Up',
             (loc_C, 'Dirty'): 'Suck',
             (loc_D, 'Clean'): 'Left1',
             (loc_D, 'Dirty'): 'Suck',
             (loc_E, 'Clean'): 'Left2',
             (loc_E, 'Dirty'): 'Suck',
             (loc_F, 'Clean'): 'Down',
             (loc_F, 'Dirty'): 'Suck',
             
             
    }
    return Agent(TableDrivenAgentProgram(table))
#right1,2,3,4 start left1,2 up1,2

class Environment:

    def __init__(self):
        self.things = []
        self.agents = []

    def percept(self, agent):
        raise NotImplementedError

    def execute_action(self, agent, action):
        raise NotImplementedError

    def default_location(self, thing):
        return None

    def is_done(self):
        return not any(agent.is_alive() for agent in self.agents)

    def step(self):
        if not self.is_done():
            actions = []
            for agent in self.agents:
                if agent.alive:
                    actions.append(agent.program(self.percept(agent)))
                else:
                    actions.append("")
            for (agent, action) in zip(self.agents, actions):
                self.execute_action(agent, action)

    def run(self, steps=1000):
        for step in range(steps):
            if self.is_done():
                return
            self.step()

    def add_thing(self, thing, location=None):
        if not isinstance(thing, Thing):
            thing = Agent(thing)
        if thing in self.things:
            print("Can't add the same thing twice")
        else:
            thing.location = location if location is not None else self.default_location(thing)
            self.things.append(thing)
            if isinstance(thing, Agent):
                thing.performance = 0
                self.agents.append(thing)

    def delete_thing(self, thing):
        try:
            self.things.remove(thing)
        except ValueError as e:
            print(e)
            print("  in Environment delete_thing")
            print("  Thing to be removed: {} at {}".format(thing, thing.location))
            print("  from list: {}".format([(thing, thing.location) for thing in self.things]))
        if thing in self.agents:
            self.agents.remove(thing)


class TrivialVacuumEnvironment(Environment):
    def __init__(self):
        super().__init__()
        self.status = {loc_A: random.choice(['Clean', 'Dirty']),
                       loc_B: random.choice(['Clean', 'Dirty']),
                       loc_C: random.choice(['Clean', 'Dirty']),
                       loc_D: random.choice(['Clean', 'Dirty']),
                       loc_E: random.choice(['Clean', 'Dirty']),
                       loc_F: random.choice(['Clean', 'Dirty']),}        

    def thing_classes(self):
        return [ TableDrivenVacuumAgent]

    def percept(self, agent):
        return agent.location, self.status[agent.location]
    def clean_check(self):
        number_of_clean_rooms=0
        for key in [loc_A, loc_B, loc_C, loc_D, loc_E, loc_F]:
            if self.status[key] =='Clean':
                number_of_clean_rooms=number_of_clean_rooms+1
        return number_of_clean_rooms
    def execute_action(self, agent, action):
        if (self.clean_check()!=9):
            
            if action=='Right1':
                agent.location = loc_B
                agent.performance -=1
            elif action=='Right2':
                agent.location = loc_C
                agent.performance -=1
            elif action=='Left1':
                agent.location = loc_E
                agent.performance -=1
            elif action=='Left2':
                agent.location = loc_F
                agent.performance -=1
            elif action=='Up':
                agent.location = loc_D
                agent.performance -=1
            elif action=='Start':
                agent.location = loc_A
                agent.performance -=1
            elif action=='Suck':
                if self.status[agent.location]=='Dirty':
                    agent.performance+=10
                self.status[agent.location]='Clean'

    def default_location(self, thing):
        return random.choice([loc_A, loc_B, loc_C, loc_D, loc_E, loc_F])


if __name__ == "__main__":
    agent = TableDrivenVacuumAgent()
    environment = TrivialVacuumEnvironment()
    environment.add_thing(agent)
    print('Agent Before Action\n\n',environment.status)
    print('\nAgent Location : ',agent.location)
    print('\nAgent Performance : ',agent.performance)
    print("\nClean rooms : ",environment.clean_check())

    environment.run(steps=6)
    print('\n\nAgent after Action\n\n',environment.status)
    print('\nAgent Location : ',agent.location)
    print('\nAgent Performance : ',agent.performance)
    print("\nClean rooms : ",environment.clean_check())
        

