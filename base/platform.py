# 平台适配器抽象类

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List

class PlatformAdapter(ABC):
    """平台适配器抽象基类"""
    
    @abstractmethod
    def parse(self, message: Any) -> Dict[str, Any]:
        """
        解析平台消息，返回统一格式
        返回: {
            "platform": "discord",
            "sender_id": "123456789",
            "sender_name": "用户名",
            "target": "@bot",
            "content": "消息内容",
            "channel": "频道ID",
            "raw": "原始消息"
        }
        """
        pass
    
    @abstractmethod
    def reply(self, context: Dict[str, Any], message: str) -> bool:
        """
        发送回复消息
        """
        pass
    
    @abstractmethod
    def extract_mentions(self, content: str) -> List[str]:
        """
        提取 @ 提及的用户
        """
        pass
