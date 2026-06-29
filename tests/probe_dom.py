"""Probe BOSS 聊天页真实 DOM —— 打开 chrome profile，切到聊天 tab，dump 窗口结构。"""
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from boss_auto_apply.browser.auth import BossAuth
from boss_auto_apply.paths import DATA_DIR

auth = BossAuth(DATA_DIR)
if not auth.check_login():
    print("[probe] 未登录")
    sys.exit(1)
page = auth.page
print(f"[probe] current url: {page.url}")

if "chat" not in page.url:
    page.get("https://www.zhipin.com/web/chat/index")
    time.sleep(3)

print("[probe] 请在10秒内手动点开一个有消息的聊天窗口...")
time.sleep(10)

selectors = [
    ".chat-no-data",
    ".im-list",
    ".chat-record-box",
    ".im-message-list",
    "ul.im-list",
    ".chat-conversation",
    ".chat-content",
    ".message-list",
    ".conversation-list",
    ".chat-body",
    ".message-item",
    "li.message-item",
    ".msg-item",
    ".im-bubble",
    ".im-msg",
    '[class*="message"]',
    '[class*="msg"]',
    '[class*="chat-record"]',
    '[class*="im-list"]',
]
for sel in selectors:
    try:
        eles = page.eles(sel)
        if eles:
            cnt = len(eles) if isinstance(eles, list) else 1
            print(f"  {sel:40s} -> 找到 {cnt} 个")
    except Exception as e:
        print(f"  {sel:40s} -> ERR {e}")

print("\n[probe] 尝试 dump 聊天窗口 outerHTML 前 3000 字符:")
for sel in [".chat-conversation", ".chat-record-box", ".im-list", ".chat-content"]:
    try:
        el = page.ele(sel, timeout=1)
        if el:
            html = el.html[:3000]
            print(f"\n=== {sel} ===\n{html}\n")
            dump_path = DATA_DIR / "probe_dump.html"
            dump_path.write_text(f"<!-- {sel} -->\n{el.html}", encoding="utf-8")
            print(f"[probe] full html saved to {dump_path}")
            break
    except Exception:
        pass
