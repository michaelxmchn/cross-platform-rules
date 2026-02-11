#!/usr/bin/env python3
"""
跨平台规则库测试
"""

import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from base.rule_engine import RuleEngine, BaseRule, create_engine
from base.platform import PlatformAdapter
from platforms.discord import DiscordAdapter


async def test_discord_at_reply():
    """测试 Discord @ 回复"""
    
    print("=" * 50)
    print("测试 Discord @ 回复规则")
    print("=" * 50)
    
    # 创建规则引擎
    engine = RuleEngine()
    print(f"✅ 加载了 {len(engine.rules)} 个规则")
    
    # 设置 Discord 适配器
    adapter = DiscordAdapter()
    engine.set_adapter(adapter)
    
    # 模拟 Discord 消息
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
        }
    ]
    
    for msg in test_messages:
        print(f"\n📨 收到消息: {msg['content']}")
        print(f"   来自: @{msg['author']['username']}")
        
        # 处理消息
        reply = await engine.process(msg)
        
        if reply:
            print(f"✅ 回复: {reply}")
        else:
            print("❓ 无匹配规则")


if __name__ == "__main__":
    import asyncio
    asyncio.run(test_discord_at_reply())
