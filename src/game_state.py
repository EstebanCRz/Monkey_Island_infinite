import json

class GameState:
    def __init__(self, parameters):
        self.state = {
            "player": parameters.get("player", {}),
            "world": parameters.get("world", {}),
            "progress": [],
        }

    def get_state(self):
        return self.state

    def update_state(self, action, outcome):
        self.state["progress"].append({"action": action, "outcome": outcome})
        self.state.update(outcome.get("state_updates", {}))
