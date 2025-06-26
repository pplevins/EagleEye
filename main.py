from DAL.AgentDAL import AgentDAL
from Models import Agent, AgentStatus


def agents_init():
    """Initialize an agents list with pre-defined agents."""
    return [
        Agent(1, "ShadowFox", "Ethan Cole", "Berlin", AgentStatus.ACTIVE, 12),
        Agent(2, "NightHawk", "Samantha Reid", "Tokyo", AgentStatus.ACTIVE, 9),
        Agent(3, "Ghost", "Liam Drake", "London", AgentStatus.RETIRED, 25),
        Agent(4, "Falcon", "Ava Morgan", "Paris", AgentStatus.ACTIVE, 7),
        Agent(5, "Viper", "Noah Black", "New York", AgentStatus.MISSING, 15),
        Agent(6, "Specter", "Chloe Bennett", "Moscow", AgentStatus.ACTIVE, 18),
        Agent(7, "Raven", "Logan Pierce", "Dubai", AgentStatus.ACTIVE, 5),
        Agent(8, "Phantom", "Maya Lin", "Beijing", AgentStatus.INJURED, 14),
        Agent(9, "Jaguar", "Carlos Ramirez", "Rio de Janeiro", AgentStatus.ACTIVE, 11),
        Agent(10, "Wolf", "Isabelle Hart", "Rome", AgentStatus.ACTIVE, 20),
    ]


def print_agents(agents):
    """Print agents list."""
    for agent in agents:
        print(agent)


def main():
    """Main function to demonstrate usage of agents and their CRUD operations."""
    agent_dal = AgentDAL()
    agent_dal.reset_agents_table()

    for agent in agents_init():
        agent_dal.add_agent(agent)

    print("=== Initial Agents ===")
    print_agents(agent_dal.get_all_agents())

    agent_dal.update_agent_location(1, "Tel Aviv")
    agent_dal.delete_agent(9)

    print("\n=== After Updates ===")
    print_agents(agent_dal.get_all_agents())


if __name__ == "__main__":
    main()
