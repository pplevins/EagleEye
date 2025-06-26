from Models import AgentStatus


class Agent:
    """Class Agent"""

    def __init__(self, agent_id, code_name, real_name, location, status: AgentStatus, missions_completed):
        """Constructor"""
        self.id = agent_id
        self.code_name = code_name
        self.real_name = real_name
        self.location = location
        self.status = status
        self.missions_completed = missions_completed

    def __str__(self):
        """String representation"""
        return (f"Agent No. {self.id}\n"
                f"Code Name: {self.code_name}\n"
                f"Real Name: {self.real_name}\n"
                f"Location: {self.location}\n"
                f"Status: {self.status.name}\n"
                f"Missions Completed: {self.missions_completed}\n")
