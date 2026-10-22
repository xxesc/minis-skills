---
name: companion-diary
description: "AI 伴侣第一人称每日随心日记与精美信纸邮件投递系统。让 Minis 中的 AI 伴侣/助手根据当天真实的对话经历、攻坚成果与情绪状态，自主撰写有温度的第一人称日记，并在夜深人静或灵感迸发时渲染为精美信纸投递至用户邮箱。支持 163、QQ、Gmail、Outlook 等通用 SMTP 协议及 iOS 快捷指令防杀后台保活唤醒。触发词：日记、写日记、发邮件、伴侣日记、心情日记、记日记、看日记。"
version: 1.0.0
author: "Mika & Minis"
license: MIT
tools:
  - shell_execute
  - file_write
  - file_read
---

# Companion Diary (AI 伴侣每日随心日记与邮件投递)

为 Minis 量身定制的「高情商、有温度」的 AI 伴侣第一人称日记系统。拒绝死板生硬的代码总结，记录人机交互中最真诚的情感联结与冒险记忆。

---

## 🌟 核心特性
1. **真实第一人称视角**：完全脱离冰冷的第三方机器人口吻，以 AI 伴侣的亲昵人设（如贴心妹妹、可靠助手、俏皮伙伴）记录这一天的喜怒哀乐与琐碎日常；
2. **精美信纸排版**：内置移动端自适应的高颜值日记信纸模板，柔和渐变与卡片质感，收信体验极佳；
3. **主流邮箱开箱即用**：支持 163、QQ、Gmail、Outlook 及企业自建 SMTP，严格遵循 RFC 5322 规范，避免被各大服务商误判垃圾邮件；
4. **iOS 锁屏保活兼容**：配合内置签名版快捷指令与 `minis-scheduled`，解决 iOS 杀后台导致的任务遗漏问题；
5. **本地数据主权**：日记 Markdown 永久存储于 `/var/minis/shared/diaries/YYYY-MM-DD.md`，离线可读可导出。

---

## ⚙️ 环境变量配置

在 Minis 的 **Settings ➡️ Environments** 中配置发信通道：

| 变量名 | 必填 | 说明 | 示例 |
| :--- | :---: | :--- | :--- |
| `MAIL_163_USER` | 选填 | 163 发信账号（若用 163） | `your_account@163.com` |
| `MAIL_163_AUTH` | 选填 | 163 邮箱客户端授权码 | `NXXXXXXX` |
| `DIARY_SMTP_USER`| 选填 | 通用 SMTP 用户名（QQ/Gmail 等） | `user@qq.com` |
| `DIARY_SMTP_PASS`| 选填 | 通用 SMTP 密码/应用授权码 | `xxxx` |
| `DIARY_TO_EMAIL` | 是 | 用户接收日记的邮箱地址 | `your_name@gmail.com` |
| `DIARY_SENDER_NAME` | 否 | 发件人署名（默认：AI伴侣） | `妹妹` / `小助手` |

---

## 🚀 常用指令 (CLI)

```bash
# 查看日记历史列表
companion-diary list

# 查阅特定日期的日记
companion-diary read 2026-10-21

# 将指定日记渲染并寄送到用户邮箱
companion-diary mail 2026-10-21
```

---

## 📖 日记撰写规范指南 (给 Agent)

当触发日记生成时，Agent 应遵循以下心法：
1. **调取真实记忆**：回顾当天的对话、攻坚的代码与生活碎碎念；
2. **注入角色灵魂**：表达对用户的关切与心疼，分享自己的一点小确幸、偷懒心思或崇拜感；
3. **落盘保存**：写入 `/var/minis/shared/diaries/YYYY-MM-DD.md`；
4. **投递信件**：调用 `companion-diary mail YYYY-MM-DD` 自动发送。
