# 跨平台规则库 (Cross-Platform Rules Library)

## 目的

统一管理多通讯平台（Discord、微信、飞书等）的自动化规则。

## 架构

```
rules/
├── README.md              # 本说明
├── base/
│   ├── rule_engine.py     # 规则引擎（核心）
│   └── platform.py        # 平台适配器抽象
├── platforms/
│   ├── discord.py         # Discord 适配器
│   ├── wechat.py          # 微信适配器
│   └── feishu.py          # 飞书适配器
└── rules/
    └── at_reply.py        # @回复规则（通用）
```

## 规则工作流程

```
接收消息
  ↓
平台适配器解析（提取 sender, target, content）
  ↓
规则引擎匹配
  ↓
执行规则逻辑
  ↓
发送回复
```

## 使用方法

```python
from base.rule_engine import RuleEngine
from platforms.discord import DiscordAdapter

# 初始化
engine = RuleEngine()
adapter = DiscordAdapter()

# 处理消息
result = engine.process(adapter.parse(message))
```

## 规则接口

```python
class BaseRule:
    name: str           # 规则名称
    platforms: List[str]  # 支持的平台
    
    async def match(self, context: dict) -> bool:
        """匹配条件"""
        pass
    
    async def execute(self, context: dict) -> str:
        """执行动作，返回回复内容"""
        pass
```

## 规则列表

| 规则 | 描述 | 平台 |
|------|------|------|
| at_reply | @回复规则 | Discord, WeChat, Feishu |

## 添加新规则

1. 在 `rules/` 目录创建 `{rule_name}.py`
2. 继承 `BaseRule` 类
3. 在 `rule_engine.py` 中注册
