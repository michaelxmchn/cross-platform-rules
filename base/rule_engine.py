# 规则引擎

import os
import importlib
from typing import Dict, Any, List, Type, Optional
from .platform import PlatformAdapter

class BaseRule:
    """规则基类"""
    name: str = "base_rule"
    platforms: List[str] = []
    
    async def match(self, context: Dict[str, Any]) -> bool:
        """匹配条件"""
        return False
    
    async def execute(self, context: Dict[str, Any]) -> str:
        """执行动作，返回回复内容"""
        return ""


class RuleEngine:
    """规则引擎"""
    
    def __init__(self, rules_dir: str = None):
        self.rules: List[BaseRule] = []
        self.adapter: PlatformAdapter = None
        
        if rules_dir is None:
            rules_dir = os.path.dirname(os.path.dirname(__file__))
        
        self.load_rules(rules_dir)
    
    def load_rules(self, rules_dir: str):
        """加载所有规则"""
        rules_path = os.path.join(rules_dir, "rules")
        
        if not os.path.exists(rules_path):
            return
        
        for filename in os.listdir(rules_path):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]
                module = importlib.import_module(f"rules.{module_name}")
                
                # 获取规则类
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if (isinstance(attr, type) and 
                        issubclass(attr, BaseRule) and 
                        attr != BaseRule):
                        self.rules.append(attr())
    
    def set_adapter(self, adapter: PlatformAdapter):
        """设置平台适配器"""
        self.adapter = adapter
    
    async def process(self, message: Any) -> Optional[str]:
        """
        处理消息，返回回复内容
        """
        if not self.adapter:
            return None
        
        # 解析消息
        context = self.adapter.parse(message)
        
        # 匹配规则
        for rule in self.rules:
            if context["platform"] in rule.platforms:
                if await rule.match(context):
                    # 执行规则
                    reply = await rule.execute(context)
                    
                    # 发送回复
                    if reply:
                        self.adapter.reply(context, reply)
                    
                    return reply
        
        return None


# 便捷函数
def create_engine(rules_dir: str = None) -> RuleEngine:
    """创建规则引擎"""
    return RuleEngine(rules_dir)
