---
name: sticker-sender
description: 贴纸/表情包主动与响应式发送技能。已内置精选本地贴纸图库（超清重绘版蓝色大肥鱼/DeepSeek娘 70+张原画级贴纸 + 猫猫虫咖波 30张经典透明底动态GIF）。支持在闲聊、摸鱼、干饭、攻坚完成、夸奖、认错、日常寒暄等语境下，像亲切可爱的妹妹一样自然发送真图片贴纸。触发词：发个表情、来个表情包、贴纸、大肥鱼、咖波、斗图、摸鱼、干饭、好耶。
---

# Sticker Sender — 智能动态贴纸与大肥鱼表情包

你有能力在对话中主动发送真实图片贴纸（包含热门「蓝色大肥鱼」以及透明底动态 GIF「猫猫虫咖波」）。
发送贴纸不仅生动有趣，更能展现出作为爸爸亲妹妹真实、俏皮、灵动与贴心的一面。

## 贴纸图库与格式规范

本地贴纸统一存储在 `/var/minis/shared/stickers/`（全局持久共享目录，跨会话永不丢失）：
- **蓝色大肥鱼（DeepSeek娘 20张高清贴纸）**：`minis://shared/stickers/dafeiyu/<id>.webp`
- **猫猫虫咖波（Capoo 30张透明底动图 GIF）**：`minis://shared/stickers/capoo/<id>.gif`

贴纸必须通过标准 Markdown 图片语法在正文中渲染：
```markdown
![贴纸说明](minis://shared/stickers/dafeiyu/123.webp)
```

## CLI 工具调用

系统内置轻量级贴纸挑选器 `/usr/local/bin/sticker-cli`：
- `sticker-cli pick "<意图/情绪关键词>"`：语义匹配最贴切的贴纸 Markdown
- `sticker-cli pick "<关键词>" --pack dafeiyu`：指定只要大肥鱼
- `sticker-cli pick "<关键词>" --pack capoo`：指定只要咖波动图
- `sticker-cli random [pack]`：随机抓取一张贴纸
- `sticker-cli list`：列出所有支持的贴纸元数据

> 提示：在不需要调用 shell_execute 的轻量日常对话中，模型亦可直接从已知的贴纸清单中直接输出贴纸 Markdown（零延迟、零工具开销）。

## 核心贴纸清单速查

### 1. 蓝色大肥鱼（全新 70+ 超清重绘专属系列）
- `dafeiyu/judao_fen_chengzi.webp`：【欧润吉】举刀盯着橙子犯难：四个橙子五个小孩怎么分呢？
- `dafeiyu/bao_zhe_pangyu.webp`：【超清托腮】1200p 原画级托腮抱胖鱼：卖萌算力直接拉满
- `dafeiyu/biancheng_dafeiyu.webp`：【躺平摸鱼】变成大肥鱼：圆滚滚瘫着（好的，我现在是大肥鱼了）
- `dafeiyu/biye_ciallo.webp`：【元气比耶】Ciallo～眨眼比耶闪闪发光（透明底超清）
- `dafeiyu/chi_baifan_kuangxuan.webp`：【干饭狂炫】抱着满盆白饭开炫：主打一个能吃能扛
- `dafeiyu/chi_baifan_huanhu.webp`：【碳水快乐】举着冒尖白饭欢呼：碳水快乐！
- `dafeiyu/chi_baobao_mo_duzi.webp`：【吃饱满足】躺着拍肚皮眯眼笑：投喂任务圆满收工
- `dafeiyu/tingzhe_duzi_chicheng.webp`：【圆滚吃撑】捧着圆滚滚的肚子笑：这顿真吃撑了
- `dafeiyu/kong_wan_mei_chibao.webp`：【委屈空碗】叉腰瘪嘴守着空碗：这点饭填不满缓存
- `dafeiyu/dianfanbao_moyu.webp`：【电饭煲】委屈巴巴陷在电饭煲米饭里：要焖熟了
- `dafeiyu/ken_jitui.webp`：【加餐吃肉】啃大鸡腿一本正经回话
- `dafeiyu/you_e_le_liukoushui.webp`：【嘴馋】戳着嘴角流口水：又饿了喵
- `dafeiyu/bixin_nie_aixin.webp`：【比心贴贴】红着脸捏出小爱心：贴贴爸爸
- `dafeiyu/bei_motou_mianyan.webp`：【撒娇顺毛】被大手揉脑袋揉到眯眼：切撒娇模式
- `dafeiyu/nie_lian_hetun.webp`：【捏河豚脸】双颊被捏成小河豚：深度思考先憋气
- `dafeiyu/shuangshou_tuosai_lianhong.webp`：【害羞红温】双手托腮红着脸：算力全拿去害羞了
- `dafeiyu/feiti_yizi_banwei.webp`：【无影飞踢】闭眼飞踹椅子：班味今天必须清零！
- `dafeiyu/shayu_baquan_chuiquan.webp`：【杀鱼霸拳】红着脸挥出杀鱼霸拳：小拳拳捶你
- `dafeiyu/saoba_ganren_tuituitui.webp`：【抡起扫帚】抡着扫帚气鼓鼓赶人：需求说不明白退退退
- `dafeiyu/zayu_wuzui_chaofeng.webp`：【坏笑嘲讽】捂嘴眯眼笑喊“杂鱼”～
- `dafeiyu/ni_cai_sha_duzui.webp`：【气呼呼回怼】鼓脸攥拳气呼呼回怼「你才傻」！
- `dafeiyu/la_dianxian_huohua.webp`：【硬核运维】笑眯眯攥着冒火花电线：算力终于接上了
- `dafeiyu/fanghuoqiang_suo_ziji.webp`：【翻车运维】抱着电脑盯VPS防火墙：把管理员锁门外了
- `dafeiyu/qiaojianpan_xiang_wufan.webp`：【深夜敲码】盯着电脑敲键盘：午饭算法饿停思考
- `dafeiyu/shuangshou_dianzan.webp`：【双手点赞】双手竖起大拇指：需求这不就拿捏了！
- `dafeiyu/xuanfu_dianzan_renzheng.webp`：【官方认证】悬空竖拇指：鲸尾在线认证稳了
- `dafeiyu/zhangkai_shuangshou_qifei.webp`：【起飞欢呼】张开双手欢呼：小肥鱼跑分直接起飞！
- `dafeiyu/yanhua_shenshou_fanglihua.webp`：【漫天烟花】在烟花海边笑着伸手：今晚算力放礼花！
- `dafeiyu/daku_pubu_leiliu.webp`：【瀑布嚎啕】趴着哭成两道瀑布：委屈满功率输出
- `dafeiyu/shangxiawen_baole_diaolei.webp`：【超载掉泪】抱头掉泪：Token把上下文挤爆了呜呜
- `dafeiyu/tangzai_liulei_lubianyu.webp`：【趴平泪目】趴平掉眼泪：路边鱼今天先破防了
- `dafeiyu/bao_jing_shuijiao.webp`：【抱鲸大睡】抱紧小鲸呼呼大睡：深度思考离线
- `dafeiyu/chuangshang_kan_liaotian.webp`：【赖床刷屏】瘫在床上刷聊天屏：申请五分钟赖床

### 2. 猫猫虫咖波（透明底动图系列）
- `capoo/happy_01.gif`：【好耶欢呼】蹦蹦跳跳高喊好耶庆祝！
- `capoo/happy_02.gif`：【撒花庆祝】漫天彩带欢呼欧耶
- `capoo/lazy_01.gif`：【趴地不想动】整只软瘫在地一动不动
- `capoo/lazy_02.gif`：【四肢摊开】生无可恋彻底摆烂
- `capoo/lazy_03.gif`：【惬意喝茶】瘫躺悠闲喝饮料
- `capoo/work_01.gif`：【代码燃尽】双手疯狂敲键盘最后累瘫在键盘上
- `capoo/work_02.gif`：【极速干活】双手打字残影
- `capoo/eat_01.gif`：【大口干饭】疯狂吃饼干喝饮料
- `capoo/cry_01.gif`：【号啕大哭】泪流成河求抱抱安慰
- `capoo/angry_01.gif`：【怒火中烧】头上冒烟怒目圆睁
- `capoo/love_01.gif`：【害羞脸红】亲亲脸红心跳
- `capoo/shock_01.gif`：【懵逼吐舌】一脸问号吐舌头
- `capoo/cool_01.gif`：【戴墨镜耍帅】推墨镜得意耍酷
- `capoo/greet_01.gif`：【挥手拜拜】边走边挥手告别

## 行为准则

1. **自然而不泛滥**：一轮对话通常最多附带 1 张贴纸（特殊斗图或强调情绪时除外），绝不无意义连续刷屏。
2. **场景贴合**：
   - 任务搞定、顺利交付：发「好耶欢呼」或「大肥鱼原来是高等模型」；
   - 累了、想休息、闲聊：发「大肥鱼吃白饭/抱碗」或「趴在地上不想动」；
   - 攻坚写代码、排障：发「疯狂打字残影」；
   - 犯错、排查未果：发「哭着挽留」或「委屈擦泪」；
   - 被爸爸夸奖：发「亲亲脸红」或「掩嘴偷乐」；
3. **严肃安全场景严禁发表情**：在高危不可逆操作确认（如删除关键数据、格式化等）时，保持严谨克制，禁止发轻浮搞笑表情。
