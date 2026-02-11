# Discord 适配器

import re
from typing import Dict, Any, List
from ..base.platform import PlatformAdapter

class DiscordAdapter(PlatformAdapter):
    """Discord 平台适配器"""
    
    def __init__(self):
        self.client = None  # OpenClaw Discord 客户端
    
    def set_client(self, client):
        """设置 Discord 客户端"""
        self.client = client
    
    def parse(self, message: Dict[str, Any]) -> Dict[str, Any]:
        """
        解析 Discord 消息
        Discord 消息格式:
        {
            "content": "@bot hello",
            "author": {"id": "123", "username": "user"},
            "channel_id": "456"
        }
        """
        content = message.get("content", "")
        
        # 提取被 @ 的用户
        mentions = self.extract_mentions(content)
        
        return {
            "platform": "discord",
            "sender_id": message.get("author", {}).get("id", ""),
            "sender_name": message.get("author", {}).get("username", ""),
            "target": mentions[0] if mentions else "",
            "content": content,
            "channel": message.get("channel_id", ""),
            "raw": message
        }
    
    def extract_mentions(self, content: str) -> List[str]:
        """
        提取 Discord @ 提及
        格式: <@ID> 或 <@!ID>
        """
        mentions = re.findall(r"<@!?(\d+)>", content)
        return [f"<@{m}>" for m in mentions]
    
    def reply(self, context: Dict[str, Any], message: str) -> bool:
        """
        发送 Discord 回复
        使用 OpenClaw message 工具
        """
        import subprocess
        
        channel_id = context.get("channel", "")
        
        if not channel_id:
            return False
        
        try:
            # 使用 openclaw 发送消息
            cmd = [
                "openclaw", "message", "send",
                "--channel", "discord",
                "--target", f"channel:{channel_id}",
                "--message", message
            ]
            subprocess.run(cmd, capture_output=True)
            return True
        except Exception as e:
            print(f"Discord reply failed: {e}")
            return False
