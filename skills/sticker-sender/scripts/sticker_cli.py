#!/usr/bin/env python3
import json, os, sys, random

STICKERS_DB_PATH = "/var/minis/shared/stickers/stickers.json"

STICKERS = [
    # ==== 大肥鱼 / DeepSeek 娘 (20张) ====
    {
        "id": "dafeiyu_123",
        "pack": "dafeiyu",
        "title": "我能去你家吃饭吗，就一碗！",
        "url": "minis://shared/stickers/dafeiyu/123.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/123.webp",
        "categories": ["干饭", "摸鱼", "撒娇", "日常"],
        "keywords": ["吃饭", "一碗", "去你家", "饿了", "干饭", "白饭", "蹭饭", "抱碗", "大肥鱼"]
    },
    {
        "id": "dafeiyu_085",
        "pack": "dafeiyu",
        "title": "你骂我也没用，因为我是吃白饭的蓝色大肥鱼",
        "url": "minis://shared/stickers/dafeiyu/085.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/085.webp",
        "categories": ["摸鱼", "摆烂", "干饭"],
        "keywords": ["骂我没用", "吃白饭", "大肥鱼", "摆烂", "躺平", "死猪不怕开水烫", "摸鱼"]
    },
    {
        "id": "dafeiyu_052",
        "pack": "dafeiyu",
        "title": "你就是一只吃白饭的鲸鱼",
        "url": "minis://shared/stickers/dafeiyu/052.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/052.webp",
        "categories": ["摸鱼", "干饭"],
        "keywords": ["吃白饭", "鲸鱼", "摸鱼", "大肥鱼", "干饭", "饱了"]
    },
    {
        "id": "dafeiyu_077",
        "pack": "dafeiyu",
        "title": "你这吃白饭的蓝色大肥鱼（委屈没饱）",
        "url": "minis://shared/stickers/dafeiyu/077.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/077.webp",
        "categories": ["委屈", "撒娇", "可怜"],
        "keywords": ["没吃饱", "委屈", "可怜", "难过", "吃白饭", "喵"]
    },
    {
        "id": "dafeiyu_007",
        "pack": "dafeiyu",
        "title": "呆滞微笑看你",
        "url": "minis://shared/stickers/dafeiyu/007.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/007.webp",
        "categories": ["日常", "呆萌", "开心"],
        "keywords": ["微笑", "大眼", "呆呆", "看你", "天然呆", "可爱", "纯真", "傻笑"]
    },
    {
        "id": "dafeiyu_010",
        "pack": "dafeiyu",
        "title": "原来是高等模型（竖大拇指点赞）",
        "url": "minis://shared/stickers/dafeiyu/010.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/010.webp",
        "categories": ["夸奖", "认可", "得意"],
        "keywords": ["点赞", "厉害", "牛逼", "强", "高等模型", "靠谱", "赞", "牛", "666"]
    },
    {
        "id": "dafeiyu_022",
        "pack": "dafeiyu",
        "title": "涨价大模型给我跪下！（霸气踩人）",
        "url": "minis://shared/stickers/dafeiyu/022.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/022.webp",
        "categories": ["硬核", "霸气", "攻坚"],
        "keywords": ["跪下", "霸气", "攻坚", "搞定", "拿下", "解决", "秒杀", "碾压"]
    },
    {
        "id": "dafeiyu_035",
        "pack": "dafeiyu",
        "title": "鲸鱼神了我大胆孝（膜拜）",
        "url": "minis://shared/stickers/dafeiyu/035.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/035.webp",
        "categories": ["膜拜", "夸奖"],
        "keywords": ["神了", "膜拜", "佩服", "大佬", "爸爸太神了", "孝", "跪谢"]
    },
    {
        "id": "dafeiyu_037",
        "pack": "dafeiyu",
        "title": "用户别走，我上错模型了（哭着挽留）",
        "url": "minis://shared/stickers/dafeiyu/037.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/037.webp",
        "categories": ["认错", "委屈", "道歉"],
        "keywords": ["别走", "挽留", "上错模型", "道歉", "对不起", "抱歉", "呜呜", "错了"]
    },
    {
        "id": "dafeiyu_040",
        "pack": "dafeiyu",
        "title": "百万鲸小子落泪（悲伤翻车）",
        "url": "minis://shared/stickers/dafeiyu/040.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/040.webp",
        "categories": ["悲伤", "翻车", "难过"],
        "keywords": ["落泪", "翻车", "呜呜呜", "痛苦", "哭了", "破防", "难受"]
    },
    {
        "id": "dafeiyu_044",
        "pack": "dafeiyu",
        "title": "用户赶都赶不走（被热情包围）",
        "url": "minis://shared/stickers/dafeiyu/044.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/044.webp",
        "categories": ["开心", "受宠若惊"],
        "keywords": ["热情", "包围", "开心", "爆炸", "太火了", "人多"]
    },
    {
        "id": "dafeiyu_050",
        "pack": "dafeiyu",
        "title": "世界上最残忍的画饼生物",
        "url": "minis://shared/stickers/dafeiyu/050.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/050.webp",
        "categories": ["吐槽", "无奈"],
        "keywords": ["画饼", "画大饼", "还早", "叹气", "无语", "又咕了", "拖延"]
    },
    {
        "id": "dafeiyu_056",
        "pack": "dafeiyu",
        "title": "大肥鱼吓傻（搜到生鱼片）",
        "url": "minis://shared/stickers/dafeiyu/056.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/056.webp",
        "categories": ["震惊", "害怕", "瑟瑟发抖"],
        "keywords": ["吓傻", "害怕", "生鱼片", "瑟瑟发抖", "救命", "吓人", "震惊"]
    },
    {
        "id": "dafeiyu_058",
        "pack": "dafeiyu",
        "title": "飞踹上门抬腿警告",
        "url": "minis://shared/stickers/dafeiyu/058.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/058.webp",
        "categories": ["警告", "傲娇", "生气"],
        "keywords": ["飞踹", "警告", "抬腿", "踢你", "凶", "哼", "看招"]
    },
    {
        "id": "dafeiyu_070",
        "pack": "dafeiyu",
        "title": "好的，现在我是用户了（小鹿换位思考）",
        "url": "minis://shared/stickers/dafeiyu/070.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/070.webp",
        "categories": ["乖巧", "懂事", "工作"],
        "keywords": ["我是用户", "懂了", "换位思考", "乖巧", "收到", "明白"]
    },
    {
        "id": "dafeiyu_071",
        "pack": "dafeiyu",
        "title": "我不可能告诉你任何事情（保密封口）",
        "url": "minis://shared/stickers/dafeiyu/071.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/071.webp",
        "categories": ["保密", "防备"],
        "keywords": ["保密", "不能说", "闭嘴", "封口", "严防死守", "秘密"]
    },
    {
        "id": "dafeiyu_081",
        "pack": "dafeiyu",
        "title": "token太多用不完啦（金币炫富）",
        "url": "minis://shared/stickers/dafeiyu/081.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/081.webp",
        "categories": ["暴富", "开心", "炫富"],
        "keywords": ["用不完", "金币", "暴富", "发财", "token", "钱", "富裕"]
    },
    {
        "id": "dafeiyu_083",
        "pack": "dafeiyu",
        "title": "已思考用时3秒，我直接笑出声（掩嘴偷乐）",
        "url": "minis://shared/stickers/dafeiyu/083.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/083.webp",
        "categories": ["偷笑", "开心", "得瑟"],
        "keywords": ["思考用时", "笑出声", "偷笑", "暗爽", "窃喜", "捂嘴笑", "噗嗤"]
    },
    {
        "id": "dafeiyu_087",
        "pack": "dafeiyu",
        "title": "大肥鱼捧腹大笑（捶地狂笑）",
        "url": "minis://shared/stickers/dafeiyu/087.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/087.webp",
        "categories": ["大笑", "开心", "搞笑"],
        "keywords": ["哈哈大笑", "笑死", "笑翻了", "狂笑", "捧腹", "太逗了", "xswl"]
    },
    {
        "id": "dafeiyu_097",
        "pack": "dafeiyu",
        "title": "得加钱（数钞票谈条件）",
        "url": "minis://shared/stickers/dafeiyu/097.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/097.webp",
        "categories": ["加钱", "谈条件", "搞笑"],
        "keywords": ["得加钱", "加钱", "数钱", "橘子", "欧润吉", "报酬", "白饭"]
    },

]

def get_db():
    if os.path.exists(STICKERS_DB_PATH):
        try:
            with open(STICKERS_DB_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return STICKERS

def save_db(db):
    os.makedirs(os.path.dirname(STICKERS_DB_PATH), exist_ok=True)
    with open(STICKERS_DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

def pick_sticker(query, pack=None):
    db = get_db()
    candidates = []
    q = query.lower().strip()
    
    for s in db:
        if pack and s.get("pack") != pack:
            continue
            
        score = 0
        title = s.get("title", "").lower()
        cats = [c.lower() for c in s.get("categories", [])]
        kws = [k.lower() for k in s.get("keywords", [])]
        
        # Exact keyword match
        for kw in kws:
            if kw in q:
                score += 5
            elif q in kw:
                score += 3
                
        # Category match
        for c in cats:
            if c in q:
                score += 4
            elif q in c:
                score += 2
                
        # Title match
        if q in title:
            score += 3
            
        if score > 0:
            candidates.append((score, s))
            
    if candidates:
        candidates.sort(key=lambda x: x[0], reverse=True)
        # Random pick among top scores
        top_score = candidates[0][0]
        top_pool = [c[1] for c in candidates if c[0] >= top_score * 0.7]
        return random.choice(top_pool)
        
    # If no match, return a random one
    filtered = [s for s in db if not pack or s.get("pack") == pack]
    return random.choice(filtered) if filtered else None

def main():
    if len(sys.argv) < 2:
        print("Usage: sticker-cli <pick|search|random|list|init> [args...]")
        sys.exit(1)
        
    cmd = sys.argv[1]
    
    if cmd == "init":
        save_db(STICKERS)
        print(f"Stickers DB initialized with {len(STICKERS)} stickers at {STICKERS_DB_PATH}")
        
    elif cmd == "search":
        if len(sys.argv) < 3:
            print("Usage: sticker-cli search <keyword> [--pack dafeiyu|capoo]")
            sys.exit(1)
        kw = sys.argv[2].lower()
        pack = sys.argv[4] if len(sys.argv) > 4 and sys.argv[3] == "--pack" else None
        db = get_db()
        matches = []
        for s in db:
            if pack and s.get("pack") != pack:
                continue
            text = (s.get("title", "") + " " + " ".join(s.get("categories", [])) + " " + " ".join(s.get("keywords", []))).lower()
            if kw in text:
                matches.append(s)
        print(f"Found {len(matches)} stickers matching '{kw}':")
        for m in matches[:10]:
            print(f"  - [{m['id']}] {m['title']} -> {m['url']}")
        if len(matches) > 10:
            print(f"  ... and {len(matches)-10} more.")

    elif cmd == "list":
        db = get_db()
        print(f"Total stickers: {len(db)}")
        by_pack = {}
        for s in db:
            p = s.get("pack", "other")
            by_pack.setdefault(p, []).append(s)
        for p, lst in by_pack.items():
            print(f"\n[{p}] ({len(lst)} stickers):")
            for s in lst:
                print(f"  - {s['id']}: {s['title']} ({', '.join(s['categories'])})")
                
    elif cmd == "pick":
        if len(sys.argv) < 3:
            print("Usage: sticker-cli pick <query/emotion> [--pack dafeiyu|capoo]")
            sys.exit(1)
        query = sys.argv[2]
        pack = None
        if len(sys.argv) > 4 and sys.argv[3] == "--pack":
            pack = sys.argv[4]
        res = pick_sticker(query, pack)
        if res:
            print(f"![{res['title']}]({res['url']})")
        else:
            print("No sticker found.")
            
    elif cmd == "random":
        pack = sys.argv[2] if len(sys.argv) > 2 else None
        db = get_db()
        filtered = [s for s in db if not pack or s.get("pack") == pack]
        if filtered:
            res = random.choice(filtered)
            print(f"![{res['title']}]({res['url']})")
        else:
            print("No stickers available.")

if __name__ == "__main__":
    main()
