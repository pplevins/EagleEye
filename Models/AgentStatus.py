from enum import Enum


class AgentStatus(Enum):
    """Enum for the agent status."""

    ACTIVE = 'Active'
    INJURED = 'Injured'
    MISSING = 'Missing'
    RETIRED = 'Retired'
