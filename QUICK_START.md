# 跨平台规则库 - 快速开始

## ✅ 测试通过

规则逻辑工作正常！

```
📨 收到: @olama 在桌面创建文件
✅ 回复: @michael-waterbear 收到任务！
```

---

## 📁 项目结构

```
~/projects/rules/
├── README.md              # 完整说明
├── QUICK_START.md         # 本文件
├── test_simple.py         # 简单测试
├── test_rules.py          # 完整测试（待修复导入）
├── base/
│   ├── __init__.py
│   ├── platform.py        # 平台适配器抽象
│   └── rule_engine.py     # 规则引擎
├── platforms/
│   ├── __init__.py
│   ├── discord.py         # ✅ Discord 适配器
│   ├── wechat.py          # ⏳ 待开发
│   └── feishu.py          # ⏳ 待开发
└── rules/
    ├── __init__.py
    └── at_reply.py        # ✅ @回复规则
```

---

## 🔧 如何使用

### 1. 导入规则引擎

```python
from base.rule_engine import RuleEngine
from platforms.discord import DiscordAdapter
```

### 2. 创建引擎并设置适配器

```python
engine = RuleEngine()
adapter = DiscordAdapter()
engine.set_adapter(adapter)
```

### 3. 处理消息

```python
# Discord 消息格式
message = {
    "content": "@olama 任务内容",
    "author": {"id": "123", "username": "user"},
    "channel_id": "456"
}

reply = await engine.process(message)
```

---

## 📋 规则列表

| 规则 | 描述 | 状态 |
|------|------|------|
| at_reply | @ 回复规则 | ✅ 完成 |

## 🏗️ 添加新平台

继承 `PlatformAdapter`：

```python
class WeChatAdapter(PlatformAdapter):
    def parse(self, message) -> Dict:
        # 解析微信消息
        pass
    
    def reply(self, context, message) -> bool:
        # 发送微信回复
        pass
    
    def extract_mentions(self, content) -> List[str]:
        # 提取 @ 提及
        pass
```

## 🆕 添加新规则

继承 `BaseRule`：

```python
class NewRule(BaseRule):
    name = "new_rule"
    platforms = ["discord", "wechat"]
    
    async def match(self, context) -> bool:
        # 匹配条件
        pass
    
    async def execute(self, context) -> str:
        # 执行动作
        pass
```

---

## 🎯 计划

- [x] Discord 适配器
- [x] @ 回复规则
- [ ] 微信适配器
- [ ] 飞书适配器
- [ ] 消息转发规则
- [ ] 定时任务规则
