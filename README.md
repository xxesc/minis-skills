# Minis Skills

自用的 Minis (iOS) 实用极客技能合集。专注于提升 AI 伴侣体验、系统自动化与设备控制。

## 📦 技能清单

### 1. [companion-diary](./skills/companion-diary)
> **AI 伴侣第一人称每日随心日记与精美信纸邮件投递系统**
- **第一人称有温度**：让 AI 伴侣根据当天的对话攻坚与日常经历，自主记录第一人称日记；
- **精美信纸邮件**：支持自动渲染为自适应信纸排版，并通过主流 SMTP（163/QQ/Gmail/Outlook 等）发送到邮箱；
- **本地持久存储**：日记 Markdown 永久沉淀于 `/var/minis/shared/diaries/`。

### 2. [sticker-sender](./skills/sticker-sender)
> **大肥鱼与咖波高质量贴纸/表情包智能收发技能**
- **超清重绘版大肥鱼**：内置 70+ 张原画级超清大肥鱼贴纸（512p～1254p）+ 30 张经典猫猫虫咖波透明底 GIF；
- **智能语义匹配**：支持通过 `/usr/local/bin/sticker-cli` 或意图识别，在干饭、摸鱼、攻坚、撒娇、傲娇回怼等语境下精准发图；
- **开箱即用与跨会话自举**：自动挂载于 `/var/minis/shared/stickers/`，提供完整 metadata 数据库索引。

*(更多自研技能持续补充中...)*

---

## 🚀 安装与使用

将 `skills/` 下的目标技能目录复制到 Minis 的技能目录即可开箱即用：

```bash
/var/minis/skills/<skill-name>/
```

## 📄 License
MIT License.
