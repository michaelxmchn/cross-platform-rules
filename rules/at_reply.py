# @回复规则

import re
from typing import Dict, Any, List
from ..base.rule_engine import BaseRule

class AtReplyRule(BaseRule):
    """
    @回复规则
    
    触发条件:
    - 消息中 @ 了机器人
    - 机器人名称在白名单中
    
    执行动作:
    - 提取发送者信息
    - 执行任务
    - 回复时 @ 发送者
    """
    
    name: str = "at_reply"
    platforms: List[str] = ["discord", "wechat", "feishu"]
    
    # 机器人 @ 标识列表
    bot_names: List[str] = [
        "olama",      # 新电脑
        "openclaw",   # 旧电脑
        "bot",
        "机器人"
    ]
    
    async def match(self, context: Dict[str, Any]) -> bool:
        """
        匹配条件：消息 @ 了机器人
        """
        content = context.get("content", "").lower()
        sender = context.get("sender_name", "").lower()
        
        # 检查是否 @ 了机器人
        for bot_name in self.bot_names:
            if bot_name.lower() in content:
                return True
        
        return False
    
    async def execute(self, context: Dict[str, Any]) -> str:
        """
        执行规则
        1. 提取发送者名字
        2. 清理消息内容
        3. 返回回复（@ 发送者）
        """
        sender_name = context.get("sender_name", "大家")
        sender_id = context.get("sender_id", "")
        content = context.get("content", "")
        
        # 清理消息，移除 @ 机器人和多余空格
        cleaned = self._clean_content(content)
        
        # 模拟执行任务（实际由 AI 处理）
        task = f"收到来自 @{sender_name} 的任务：{cleaned}"
        
        # 返回回复（@ 发送者）
        reply = f"@{sender_name} ✅ 收到任务！\n"
        reply += f"任务内容：{cleaned}\n"
        reply += f"\n正在执行...（AI 将处理具体任务）"
        
        print(f"[AtReplyRule] {task}")
        
        return reply
    
    def _clean_content(self, content: str) -> str:
        """清理消息内容"""
        # 移除 @ 机器人标识
        for bot in self.bot_names:
            content = re.sub(rf"@{bot}\s*", "", content, flags=re.IGNORECASE)
        
        # 移除多余空格
        content = re.sub(r"\s+", " ", content).strip()
        
        return content


# 便捷函数：提取被 @ 的人
def extract_at_target(content: str, platform: str = "discord") -> Dict[str, Any]:
    """
    提取 @ 目标
    返回: {"target": "@username", "sender": "@sender_name"}
    """
    if platform == "discord":
        mentions = re.findall(r"<@!?(\d+)>", content)
        targets = [f"<@{m}>" for m in mentions]
    else:
        targets = re.findall(r"@(\w+)", content)
    
    return {
        "targets": targets,
        "sender": mentions[0] if mentions else ""
    }
