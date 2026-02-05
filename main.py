import requests
from datetime import datetime

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_weibo_hot():
    try:
        url = "https://weibo-hot.vercel.app/api"
        data = requests.get(url, timeout=10).json()
        return [i["title"] for i in data["data"][:10]]
    except:
        return []

def get_douyin_hot():
    try:
        url = "https://www.iesdouyin.com/web/api/v2/hotsearch/billboard/word/"
        data = requests.get(url, timeout=10).json()
        return [i["word"] for i in data["word_list"][:10]]
    except:
        return []

def get_zhihu_hot():
    try:
        url = "https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total"
        data = requests.get(url, headers=headers, timeout=10).json()
        return [i["target"]["title"] for i in data["data"][:10]]
    except:
        return []

def get_bilibili_hot():
    try:
        url = "https://api.bilibili.com/x/web-interface/popular"
        data = requests.get(url, timeout=10).json()
        return [i["title"] for i in data["data"]["list"][:10]]
    except:
        return []

def get_xhs_hot():
    try:
        url = "https://www.xiaohongshu.com/fe_api/burdock/weixin/v2/hot_notes"
        data = requests.get(url, headers=headers, timeout=10).json()
        return [i["title"] for i in data["data"][:10]]
    except:
        return []

def main():
    today = datetime.utcnow().strftime("%Y-%m-%d")
    lines = [f"# 🔥 每日热点汇总 {today}\n"]

    def add(title, items):
        lines.append(f"## {title}")
        if items:
            for i, h in enumerate(items, 1):
                lines.append(f"{i}. {h}")
        else:
            lines.append("获取失败")
        lines.append("")

    add("微博热搜", get_weibo_hot())
    add("抖音热榜", get_douyin_hot())
    add("知乎热榜", get_zhihu_hot())
    add("B站热榜", get_bilibili_hot())
    add("小红书热榜", get_xhs_hot())

    with open("daily_hot.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    main()
