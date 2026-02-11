#!/usr/bin/env python3
"""
简单测试：验证 @ 回复规则逻辑
"""

import re
from typing import Dict, Any, List

# 机器人名称列表
BOT_NAMES = ["olama", "openclaw", "bot", "机器人"]

def extract_mentions(content: str) -> List[str]:
    """提取 @ 提及"""
    mentions = re.findall(r"<@!?(\d+)>", content)
    return [f"<@{m}>" for m in mentions]

def clean_content(content: str) -> str:
    """清理消息内容"""
    for bot in BOT_NAMES:
        content = re.sub(rf"@{bot}\s*", "", content, flags=re.IGNORECASE)
    content = re.sub(r"\s+", " ", content).strip()
    return content

def parse_discord_message(message: Dict[str, Any]) -> Dict[str, Any]:
    """解析 Discord 消息"""
    content = message.get("content", "")
    
    return {
        "platform": "discord",
        "sender_id": message.get("author", {}).get("id", ""),
        "sender_name": message.get("author", {}).get("username", ""),
        "target": extract_mentions(content)[0] if extract_mentions(content) else "",
        "content": content,
        "channel": message.get("channel_id", "")
    }

def at_reply_rule(context: Dict[str, Any]) -> str:
    """@ 回复规则"""
    content = context.get("content", "").lower()
    sender_name = context.get("sender_name", "大家")
    
    # 检查是否 @ 了机器人
    for bot_name in BOT_NAMES:
        if bot_name.lower() in content:
            cleaned = clean_content(content)
            
            reply = f"@{sender_name} ✅ 收到任务！\n"
            reply += f"任务内容：{cleaned}\n"
            reply += f"\n正在执行...（AI 将处理具体任务）"
            
            return reply
    
    return ""


# 测试
print("=" * 50)
print("跨平台规则库 - @ 回复规则测试")
print("=" * 50)

test_messages = [
    {
        "content": "@olama 在桌面创建文件，写入测试",
        "author": {"id": "123456", "username": "michael-waterbear"},
        "channel_id": "789"
    },
    {
        "content": "@openclaw 请帮我查询天气",
        "author": {"id": "111", "username": "test-user"},
        "channel_id": "789"
    },
    {
        "content": "@olama 下载 Brave API key",
        "author": {"id": "222", "username": "admin"},
        "channel_id": "789"
    }
]

for msg in test_messages:
    print(f"\n📨 收到消息: {msg['content']}")
    print(f"   来自: @{msg['author']['username']}")
    
    context = parse_discord_message(msg)
    reply = at_reply_rule(context)
    
    if reply:
        print(f"✅ 回复:\n{reply}")
    else:
        print("❓ 无匹配规则")

print("\n" + "=" * 50)
print("✅ 测试完成！")
print("=" * 50)
