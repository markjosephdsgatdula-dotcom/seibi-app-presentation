import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

def create_presentation():
    prs = Presentation()
    
    # Set slide dimensions to widescreen (16:9)
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    # Design constants (Seibi App Theme)
    BG_COLOR = RGBColor(11, 14, 20)       # Dark background
    TEXT_LIGHT = RGBColor(243, 244, 246)  # Off-white
    TEXT_MUTED = RGBColor(156, 163, 175)  # Muted grey
    ACCENT_BLUE = RGBColor(59, 130, 246)   # Bright blue
    ACCENT_GREEN = RGBColor(16, 185, 129) # Success green
    ACCENT_RED = RGBColor(239, 68, 68)    # Alert red
    
    # Using standard Japanese fonts available on Windows
    FONT_TITLE = "Yu Gothic"
    FONT_BODY = "Yu Gothic"
    
    # Helper to set slide background
    def set_background(slide):
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = BG_COLOR
        
    # Helper to create a slide title
    def add_slide_header(slide, title_text):
        title_box = slide.shapes.add_textbox(Inches(0.75), Inches(0.5), Inches(11.833), Inches(0.8))
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = FONT_TITLE
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = ACCENT_BLUE
        
    # Helper to format bullets nicely
    def add_bullets(text_frame, items, is_muted=False):
        for idx, item in enumerate(items):
            if idx == 0:
                p = text_frame.paragraphs[0]
            else:
                p = text_frame.add_paragraph()
            p.text = item
            p.font.name = FONT_BODY
            p.font.size = Pt(14)
            p.font.color.rgb = TEXT_MUTED if is_muted else TEXT_LIGHT
            p.space_after = Pt(10)
            p.level = 0

    blank_layout = prs.slide_layouts[6]
    
    # ==========================================
    # SLIDE 1: タイトルスライド (Title Slide)
    # ==========================================
    slide = prs.slides.add_slide(blank_layout)
    set_background(slide)
    
    # Large Logo Title
    title_box = slide.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(11.333), Inches(2.0))
    tf = title_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Seibi"
    p.font.name = FONT_TITLE
    p.font.size = Pt(72)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    
    p2 = tf.add_paragraph()
    p2.text = "設備管理システム — 設備点検アプリのご紹介"
    p2.font.name = FONT_TITLE
    p2.font.size = Pt(24)
    p2.font.color.rgb = TEXT_LIGHT
    p2.space_before = Pt(10)
    
    # Subtitle
    sub_box = slide.shapes.add_textbox(Inches(1.0), Inches(4.5), Inches(11.333), Inches(1.5))
    tf_sub = sub_box.text_frame
    p_sub = tf_sub.paragraphs[0]
    p_sub.text = "紙ベースの点検作業から、リアルタイム共有、AIによる現場修理サポートへ"
    p_sub.font.name = FONT_BODY
    p_sub.font.size = Pt(16)
    p_sub.font.color.rgb = TEXT_MUTED
    
    p_sub2 = tf_sub.add_paragraph()
    p_sub2.text = "Antigravity AI によってカスタマイズ"
    p_sub2.font.name = FONT_BODY
    p_sub2.font.size = Pt(14)
    p_sub2.font.color.rgb = ACCENT_GREEN
    p_sub2.space_before = Pt(5)

    # ==========================================
    # SLIDE 2: 経緯と従来の課題 (The Background)
    # ==========================================
    slide = prs.slides.add_slide(blank_layout)
    set_background(slide)
    add_slide_header(slide, "1. 導入の経緯と従来の課題")
    
    # Left Content - The Problem
    left_box = slide.shapes.add_textbox(Inches(0.75), Inches(1.8), Inches(5.5), Inches(4.5))
    tf_left = left_box.text_frame
    tf_left.word_wrap = True
    p = tf_left.paragraphs[0]
    p.text = "従来の紙ベース運用の限界"
    p.font.name = FONT_TITLE
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = ACCENT_RED
    p.space_after = Pt(20)
    
    problems = [
        "❌ 履歴が残らない: 全て手書きの紙で点検を行い、提出後はファイル保管か処分するのみで検索できない。",
        "❌ 過去の状況が不明: 過去の不具合や前月・去年の状況を確認する手段がなかった。",
        "❌ 状況のブラックボックス化: 点検表を持っている技術者本人以外には、設備の稼働・不具合状況が見えない。"
    ]
    add_bullets(tf_left, problems)

    # Right Content - Operational Blocks
    right_box = slide.shapes.add_textbox(Inches(6.8), Inches(1.8), Inches(5.5), Inches(4.5))
    tf_right = right_box.text_frame
    tf_right.word_wrap = True
    p_right = tf_right.paragraphs[0]
    p_right.text = "現場で発生していた具体的な問題"
    p_right.font.name = FONT_TITLE
    p_right.font.size = Pt(20)
    p_right.font.bold = True
    p_right.font.color.rgb = TEXT_LIGHT
    p_right.space_after = Pt(20)
    
    opportunities = [
        "⚠️ 記憶頼みの点検: 同じ不具合が繰り返し起きていても、個人の記憶に頼らざるを得なかった。",
        "⚠️ 修理状況の追跡不可: 不具合を発見しても、実際に修理が完了したかを追跡する仕組みがない。",
        "⚠️ マニュアルの検索性悪化: 作業中に手順を確認する際、分厚い紙マニュアルをめくるか周りに聞くしかなかった。"
    ]
    add_bullets(tf_right, opportunities)

    # ==========================================
    # SLIDE 3: 点検作業のデジタル化 (Dashboard)
    # ==========================================
    slide = prs.slides.add_slide(blank_layout)
    set_background(slide)
    add_slide_header(slide, "2. 解決策 (1) 点検作業のデジタル化")
    
    desc_box = slide.shapes.add_textbox(Inches(0.75), Inches(1.8), Inches(4.5), Inches(4.5))
    tf_desc = desc_box.text_frame
    tf_desc.word_wrap = True
    p = tf_desc.paragraphs[0]
    p.text = "その場での入力と履歴蓄積"
    p.font.name = FONT_TITLE
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT
    p.space_after = Pt(15)
    
    bullets = [
        "📱 モバイル端末での入力: タブレットやスマートフォンを使い、現場で即座に点検表を入力・提出可能。",
        "🔍 検索可能な履歴保存: 提出されたデータは自動蓄積され、過去の不具合履歴をいつでも検索・確認できるように。",
        "📊 稼働ダッシュボード: 今日のタスク進捗（例：0/13件完了）、異常発生件数、全体設備健全率を可視化。"
    ]
    add_bullets(tf_desc, bullets)
    
    img_path = 'app_dashboard.png'
    if os.path.exists(img_path):
        slide.shapes.add_picture(img_path, Inches(5.6), Inches(1.6), width=Inches(7.0))
        
    # ==========================================
    # SLIDE 4: 現場マップでの視覚的管理 (Wire Map)
    # ==========================================
    slide = prs.slides.add_slide(blank_layout)
    set_background(slide)
    add_slide_header(slide, "2. 解決策 (2) 現場マップでの視覚的管理")
    
    desc_box = slide.shapes.add_textbox(Inches(0.75), Inches(1.8), Inches(4.5), Inches(4.5))
    tf_desc = desc_box.text_frame
    tf_desc.word_wrap = True
    p = tf_desc.paragraphs[0]
    p.text = "グラフィカルな配線・配置の把握"
    p.font.name = FONT_TITLE
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT
    p.space_after = Pt(15)
    
    bullets = [
        "🗺️ インタラクティブ平面図: 工場内の溶接機やロボット、制御盤、ガスタンク等の配置を地図上で確認可能。",
        "🔌 配線ルートの確認: 設備をタップするだけで、給電や通信の配線ルートをビジュアル表示。",
        "⚡ 直感的なトラブルシューティング: 異常が発生しているノードを素早く特定し、影響範囲を判断。"
    ]
    add_bullets(tf_desc, bullets)
    
    img_path = 'app_wire_map.png'
    if os.path.exists(img_path):
        slide.shapes.add_picture(img_path, Inches(5.6), Inches(1.6), width=Inches(7.0))

    # ==========================================
    # SLIDE 5: 履歴の自動蓄積と監査性 (History Log)
    # ==========================================
    slide = prs.slides.add_slide(blank_layout)
    set_background(slide)
    add_slide_header(slide, "2. 解決策 (3) 点検・修理履歴の監査ログ")
    
    desc_box = slide.shapes.add_textbox(Inches(0.75), Inches(1.8), Inches(4.5), Inches(4.5))
    tf_desc = desc_box.text_frame
    tf_desc.word_wrap = True
    p = tf_desc.paragraphs[0]
    p.text = "継続的なデータ追跡と改善"
    p.font.name = FONT_TITLE
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT
    p.space_after = Pt(15)
    
    bullets = [
        "📋 包括的な履歴ログ: 過去に実施した点検結果、不具合の内容、作業担当者をタイムスタンプ付きで記録。",
        "🔍 多彩なフィルタ機能: 日付順、設備順、期間（30日〜今年）やステータス（異常ありなど）で瞬時に絞り込み可能。",
        "📈 修理進捗の追跡: 不具合に対する修理が完了しているかをデジタル上で管理し、対応漏れを防ぐ。"
    ]
    add_bullets(tf_desc, bullets)
    
    img_path = 'app_history.png'
    if os.path.exists(img_path):
        slide.shapes.add_picture(img_path, Inches(5.6), Inches(1.6), width=Inches(7.0))

    # ==========================================
    # SLIDE 6: 状況のリアルタイム共有と通知 (Bulletin Board)
    # ==========================================
    slide = prs.slides.add_slide(blank_layout)
    set_background(slide)
    add_slide_header(slide, "2. 解決策 (4) リアルタイム状況共有・タスク化")
    
    desc_box = slide.shapes.add_textbox(Inches(0.75), Inches(1.8), Inches(4.5), Inches(4.5))
    tf_desc = desc_box.text_frame
    tf_desc.word_wrap = True
    p = tf_desc.paragraphs[0]
    p.text = "伝え忘れを防ぐ自動連携"
    p.font.name = FONT_TITLE
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT
    p.space_after = Pt(15)
    
    bullets = [
        "🚨 自動タスク登録 & 通知: 不具合検知時、システムが自動的に修理タスクを作成し関係者に通知。",
        "💬 チャット・掲示板機能: 異常内容に対して、現場から「修理開始 (修理開始)」ボタンで即座に担当宣言が可能。",
        "🔗 社内連絡ツールとの自動連携: 重大な不具合の場合は、社内チャットツールへ自動で警告通知を送信。"
    ]
    add_bullets(tf_desc, bullets)
    
    img_path = 'app_bulletin.png'
    if os.path.exists(img_path):
        slide.shapes.add_picture(img_path, Inches(5.6), Inches(1.6), width=Inches(7.0))

    # ==========================================
    # SLIDE 7: AIによる修理サポート機能 (AI Manuals)
    # ==========================================
    slide = prs.slides.add_slide(blank_layout)
    set_background(slide)
    add_slide_header(slide, "2. 解決策 (5) AIによる現場修理サポート")
    
    desc_box = slide.shapes.add_textbox(Inches(0.75), Inches(1.8), Inches(4.5), Inches(4.5))
    tf_desc = desc_box.text_frame
    tf_desc.word_wrap = True
    p = tf_desc.paragraphs[0]
    p.text = "現場の相談相手としてのAI"
    p.font.name = FONT_TITLE
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT
    p.space_after = Pt(15)
    
    bullets = [
        "🤖 自然言語での質問: 分厚いマニュアルをめくる代わりに、普段の言葉で質問可能（例：「J3関節で異音、ロボットアームが震えている」）。",
        "📖 引用元の提示: AIが関連するマニュアル部分を特定し、「どの箇所の記述か」を示しながら的確に回答。",
        "⚙️ カテゴリ別の構成: グラインダやCO2溶接ロボットなどのハードウェアごとに整理された手順書へ素早くアクセス。"
    ]
    add_bullets(tf_desc, bullets)
    
    img_path = 'app_manuals.png'
    if os.path.exists(img_path):
        slide.shapes.add_picture(img_path, Inches(5.6), Inches(1.6), width=Inches(7.0))

    # ==========================================
    # SLIDE 8: 成果と今後の展望 (Achievements & Outlook)
    # ==========================================
    slide = prs.slides.add_slide(blank_layout)
    set_background(slide)
    add_slide_header(slide, "3. 成果と今後の展望")
    
    box_w = Inches(5.5)
    box_h = Inches(2.2)
    
    # Card 1: Current Status & Direct Benefits
    c1 = slide.shapes.add_textbox(Inches(0.75), Inches(1.8), box_w, box_h)
    tf1 = c1.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "🚀 現在のステータスと導入効果"
    p1.font.name = FONT_TITLE
    p1.font.size = Pt(20)
    p1.font.bold = True
    p1.font.color.rgb = ACCENT_GREEN
    p1.space_after = Pt(10)
    add_bullets(tf1, [
        "開発はすべて完了し、現在は本格運用に向けた最終確認段階。",
        "紙廃止による履歴の蓄積、自動通知による迅速な初動、マニュアル検索時間のゼロ化による修理時間の大幅短縮を見込む。"
    ])
    
    # Card 2: AI manual expansion
    c2 = slide.shapes.add_textbox(Inches(6.8), Inches(1.8), box_w, box_h)
    tf2 = c2.text_frame
    tf2.word_wrap = True
    p2 = tf2.paragraphs[0]
    p2.text = "📚 AI対応マニュアルの拡充"
    p2.font.name = FONT_TITLE
    p2.font.size = Pt(20)
    p2.font.bold = True
    p2.font.color.rgb = ACCENT_BLUE
    p2.space_after = Pt(10)
    add_bullets(tf2, [
        "現在は一部の設備のみ対応しているマニュアルの範囲を広げ、工場内のすべての主要設備でAIサポートを利用可能に。"
    ])
    
    # Card 3: Self-improving AI
    c3 = slide.shapes.add_textbox(Inches(0.75), Inches(4.3), box_w, box_h)
    tf3 = c3.text_frame
    tf3.word_wrap = True
    p3 = tf3.paragraphs[0]
    p3.text = "📈 使うほど賢くなるAIフィードバック"
    p3.font.name = FONT_TITLE
    p3.font.size = Pt(20)
    p3.font.bold = True
    p3.font.color.rgb = ACCENT_RED
    p3.space_after = Pt(10)
    add_bullets(tf3, [
        "技術者がAIにした質問と、その回答が役に立ったかどうかのフィードバックをログ化。",
        "有効な回答パターンを蓄積し、現場の利用実績に応じてAIの回答精度が自動で向上するエコシステムを構築。"
    ])
    
    # Card 4: Executive Closing
    c4 = slide.shapes.add_textbox(Inches(6.8), Inches(4.3), box_w, box_h)
    tf4 = c4.text_frame
    tf4.word_wrap = True
    p4 = tf4.paragraphs[0]
    p4.text = "💡 今後の展望"
    p4.font.name = FONT_TITLE
    p4.font.size = Pt(20)
    p4.font.bold = True
    p4.font.color.rgb = TEXT_LIGHT
    p4.space_after = Pt(10)
    add_bullets(tf4, [
        "設備のダウンタイムを最小化し、保全業務のナレッジを組織的に共有・蓄積することで、工場稼働率の圧倒的向上を目指します。"
    ])

    # Save presentation
    output_path = 'seibi_presentation.pptx'
    prs.save(output_path)
    print(f"Presentation successfully created at: {output_path}")

if __name__ == '__main__':
    create_presentation()
