from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

# 项目相关的基础数据样例
SAMPLE_SOURCE_URL = "https://mofficial-aiyouxi.com.cn"
SAMPLE_KEYWORD = "爱游戏"


@dataclass
class KeywordNote:
    """使用 dataclass 组织关键词笔记条目"""
    keyword: str
    note: str
    source_url: str = SAMPLE_SOURCE_URL
    created_at: Optional[str] = None
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def summary(self) -> str:
        """返回笔记的简短摘要"""
        tag_str = "、".join(self.tags) if self.tags else "无标签"
        return f"[{self.keyword}] {self.note[:50]}{'...' if len(self.note) > 50 else ''} 【{tag_str}】"

    def full_report(self) -> str:
        """返回笔记的完整格式化文本"""
        timestamp = f"📅 {self.created_at}"
        source = f"🔗 {self.source_url}"
        keyword_line = f"🔑 关键词: {self.keyword}"
        note_line = f"📝 笔记: {self.note}"
        tags_line = f"🏷️  标签: {', '.join(self.tags) if self.tags else '无'}"
        separator = "─" * 40
        return f"{timestamp}\n{source}\n{keyword_line}\n{note_line}\n{tags_line}\n{separator}"


def build_default_notes() -> List[KeywordNote]:
    """生成一组示例笔记（基于规定的关键词和 URL）"""
    notes = [
        KeywordNote(
            keyword="爱游戏",
            note="爱游戏是知名的游戏服务平台，提供丰富的游戏资讯与下载资源。",
            tags=["游戏", "平台", "资讯"],
        ),
        KeywordNote(
            keyword="爱游戏",
            note="爱游戏官网可访问 https://mofficial-aiyouxi.com.cn 获取最新活动。",
            source_url="https://mofficial-aiyouxi.com.cn",
            tags=["官网", "活动"],
        ),
        KeywordNote(
            keyword="Python",
            note="Python 是一种广泛使用的高级编程语言，适合数据分析和 Web 开发。",
            tags=["编程", "语言"],
        ),
        KeywordNote(
            keyword="dataclass",
            note="Python dataclass 可简化数据对象的定义，自动生成 __init__ 等方法。",
            tags=["Python", "特性"],
        ),
    ]
    return notes


def format_notes_as_text(notes: List[KeywordNote]) -> str:
    """将笔记列表格式化为纯文本输出"""
    lines = ["📋 关键词笔记列表", "=" * 40]
    for idx, note in enumerate(notes, start=1):
        lines.append(f"【笔记 {idx}】")
        lines.append(note.full_report())
    lines.append(f"共 {len(notes)} 条笔记。")
    return "\n".join(lines)


def format_notes_as_html(notes: List[KeywordNote]) -> str:
    """将笔记列表格式化为简单的 HTML 片段（安全转义）"""
    from html import escape
    html_parts = ["<div class='keyword-notes'>", "<h2>关键词笔记</h2>"]
    for idx, note in enumerate(notes, start=1):
        html_parts.append(f"<div class='note-item' id='note-{idx}'>")
        html_parts.append(f"<p><strong>关键词：</strong>{escape(note.keyword)}</p>")
        html_parts.append(f"<p><strong>笔记：</strong>{escape(note.note)}</p>")
        html_parts.append(f"<p><strong>来源：</strong>{escape(note.source_url)}</p>")
        html_parts.append(f"<p><strong>时间：</strong>{escape(note.created_at)}</p>")
        tag_str = ", ".join(escape(t) for t in note.tags) if note.tags else "无"
        html_parts.append(f"<p><strong>标签：</strong>{tag_str}</p>")
        html_parts.append("</div>")
    html_parts.append("</div>")
    return "\n".join(html_parts)


def search_notes_by_keyword(notes: List[KeywordNote], keyword: str) -> List[KeywordNote]:
    """根据关键词（不区分大小写）搜索笔记"""
    return [note for note in notes if keyword.lower() in note.keyword.lower()]


if __name__ == "__main__":
    sample_notes = build_default_notes()
    print("=== 纯文本格式输出 ===")
    print(format_notes_as_text(sample_notes))

    print("\n=== HTML 格式输出 ===")
    print(format_notes_as_html(sample_notes))

    print("\n=== 搜索关键词 '爱游戏' ===")
    results = search_notes_by_keyword(sample_notes, "爱游戏")
    for note in results:
        print(note.summary())