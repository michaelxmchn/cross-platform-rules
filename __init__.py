# 跨平台规则库

from .base.rule_engine import RuleEngine, BaseRule, create_engine
from .base.platform import PlatformAdapter
from .platforms.discord import DiscordAdapter

__version__ = "1.0.0"
__all__ = ["RuleEngine", "BaseRule", "PlatformAdapter", "DiscordAdapter", "create_engine"]
