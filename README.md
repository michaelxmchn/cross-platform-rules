# 跨平台规则库 (Cross-Platform Rules Library)

统一管理多通讯平台（Discord、微信、飞书等）的自动化规则。

## 📡 部署状态

| 电脑 | IP | 状态 |
|------|-----|------|
| 旧电脑 | 192.168.1.17 | ✅ 已部署 |
| 新电脑 | 192.168.1.67 | ✅ 已部署 |

## 🏷️ GitHub 仓库

https://github.com/michaelxmchn/cross-platform-rules

## 📁 项目结构

```
rules/
├── README.md              # 本说明
├── QUICK_START.md         # 快速开始
├── base/
│   ├── platform.py        # 平台适配器抽象
│   └── rule_engine.py     # 规则引擎
├── platforms/
│   ├── discord.py         # ✅ Discord 适配器
│   ├── wechat.py          # ⏳ 待开发
│   └── feishu.py          # ⏳ 待开发
└── rules/
    └── at_reply.py         # ✅ @回复规则
```

## 🚀 快速使用

```bash
# 克隆到新电脑
git clone https://github.com/michaelxmchn/cross-platform-rules ~/projects/rules

# 测试
cd ~/projects/rules
python3 test_simple.py
```

## 📋 规则列表

| 规则 | 描述 | 平台 | 状态 |
|------|------|------|------|
| at_reply | @回复规则 | Discord, WeChat, Feishu | ✅ |

## 🆕 添加新电脑

```bash
# SSH 连接新电脑
ssh user@新电脑IP

# 克隆规则库
git clone https://github.com/michaelxmchn/cross-platform-rules ~/projects/rules

# 运行测试
cd ~/projects/rules
python3 test_simple.py
```

## 🎯 计划

- [x] Discord 适配器
- [x] @ 回复规则
- [ ] 微信适配器
- [ ] 飞书适配器
- [ ] 消息转发规则
- [ ] 定时任务规则

---

**维护者**: @michaelxmchn  
**License**: MIT
