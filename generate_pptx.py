import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

def create_presentation():
    prs = Presentation()
    
    # Set slide dimensions to widescreen (16:9)
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    # Design constants (Seibi App Theme)
    BG_COLOR = RGBColor(11, 14, 20)       # Dark background
    CARD_COLOR = RGBColor(22, 27, 38)     # Slightly lighter dark grey-blue
    TEXT_LIGHT = RGBColor(243, 244, 246)  # Off-white
    TEXT_MUTED = RGBColor(156, 163, 175)  # Muted grey
    ACCENT_BLUE = RGBColor(59, 130, 246)   # Bright blue
    ACCENT_GREEN = RGBColor(16, 185, 129) # Success green
    ACCENT_RED = RGBColor(239, 68, 68)    # Alert red
    
    FONT_TITLE = "Segoe UI"
    FONT_BODY = "Segoe UI"
    
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
    # SLIDE 1: Title Slide
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
    p2.text = "設備管理システム — Equipment Maintenance & Inspection Management"
    p2.font.name = FONT_TITLE
    p2.font.size = Pt(24)
    p2.font.color.rgb = TEXT_LIGHT
    p2.space_before = Pt(10)
    
    # Subtitle
    sub_box = slide.shapes.add_textbox(Inches(1.0), Inches(4.5), Inches(11.333), Inches(1.5))
    tf_sub = sub_box.text_frame
    p_sub = tf_sub.paragraphs[0]
    p_sub.text = "A Premium Digital Solution for Factory Maintenance Operations"
    p_sub.font.name = FONT_BODY
    p_sub.font.size = Pt(16)
    p_sub.font.color.rgb = TEXT_MUTED
    
    p_sub2 = tf_sub.add_paragraph()
    p_sub2.text = "Prepared by Antigravity AI"
    p_sub2.font.name = FONT_BODY
    p_sub2.font.size = Pt(14)
    p_sub2.font.color.rgb = ACCENT_GREEN
    p_sub2.space_before = Pt(5)

    # ==========================================
    # SLIDE 2: The Challenge
    # ==========================================
    slide = prs.slides.add_slide(blank_layout)
    set_background(slide)
    add_slide_header(slide, "The Challenge in Factory Maintenance")
    
    # Left Content - The Problem
    left_box = slide.shapes.add_textbox(Inches(0.75), Inches(1.8), Inches(5.5), Inches(4.5))
    tf_left = left_box.text_frame
    tf_left.word_wrap = True
    p = tf_left.paragraphs[0]
    p.text = "Traditional Maintenance Pain Points"
    p.font.name = FONT_TITLE
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = ACCENT_RED
    p.space_after = Pt(20)
    
    problems = [
        "❌ Lack of Visibility: Factory managers cannot see real-time machine health rates (e.g. only 33% operating normally).",
        "❌ Hard to Track Progress: Paper-based checklists lead to missed tasks (e.g. 0/13 daily tasks completed).",
        "❌ Siloed Communications: Issues reported on paper remain hidden, causing delayed repairs.",
        "❌ Inaccessible Manuals: Operators waste time searching for printed manuals during a breakdown."
    ]
    add_bullets(tf_left, problems)

    # Right Content - The Need
    right_box = slide.shapes.add_textbox(Inches(6.8), Inches(1.8), Inches(5.5), Inches(4.5))
    tf_right = right_box.text_frame
    tf_right.word_wrap = True
    p_right = tf_right.paragraphs[0]
    p_right.text = "The Opportunity"
    p_right.font.name = FONT_TITLE
    p_right.font.size = Pt(20)
    p_right.font.bold = True
    p_right.font.color.rgb = ACCENT_GREEN
    p_right.space_after = Pt(20)
    
    opportunities = [
        "✅ Real-Time Dashboards: Immediate status tracking for workers and managers.",
        "✅ Interactive Factory Maps: Visual wiring layouts and instant equipment health checks.",
        "✅ Collaborative Logs & Chat: Streamlined reporting and direct communication.",
        "✅ AI-Powered Manuals: On-demand answers for immediate troubleshooting."
    ]
    add_bullets(tf_right, opportunities)

    # ==========================================
    # SLIDE 3: Dashboard Overview
    # ==========================================
    slide = prs.slides.add_slide(blank_layout)
    set_background(slide)
    add_slide_header(slide, "Worker Dashboard: Simple & Action-Oriented")
    
    # Left text description
    desc_box = slide.shapes.add_textbox(Inches(0.75), Inches(1.8), Inches(4.5), Inches(4.5))
    tf_desc = desc_box.text_frame
    tf_desc.word_wrap = True
    p = tf_desc.paragraphs[0]
    p.text = "Daily Tasks & Status at a Glance"
    p.font.name = FONT_TITLE
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT
    p.space_after = Pt(15)
    
    bullets = [
        "📊 Task Progress Meter: Simple visualization showing total tasks done vs remaining (0/13 completed).",
        "⚠️ Abnormality Tracker: Bold red counts highlighting active issues ('3' requiring action).",
        "⚙️ Overall Equipment Health: Live calculation of working machines (33% health rate).",
        "📅 Overdue Inspector Alerts: Red-bordered prioritized cards for monthly checks and repairs."
    ]
    add_bullets(tf_desc, bullets)
    
    # Right Image
    img_path = 'app_dashboard.png'
    if os.path.exists(img_path):
        slide.shapes.add_picture(img_path, Inches(5.6), Inches(1.6), width=Inches(7.0))
        
    # ==========================================
    # SLIDE 4: Interactive Wire Map
    # ==========================================
    slide = prs.slides.add_slide(blank_layout)
    set_background(slide)
    add_slide_header(slide, "Floor Layout & Interactive Wire Map")
    
    desc_box = slide.shapes.add_textbox(Inches(0.75), Inches(1.8), Inches(4.5), Inches(4.5))
    tf_desc = desc_box.text_frame
    tf_desc.word_wrap = True
    p = tf_desc.paragraphs[0]
    p.text = "Visualizing the Factory Floor"
    p.font.name = FONT_TITLE
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT
    p.space_after = Pt(15)
    
    bullets = [
        "📍 Interactive Blueprint: Visual layout mapping out TIG/CO2 Welders, Robots, Weld Tables, Controllers, and Gas Tanks.",
        "⚡ Status Indicators: Color-coded nodes (Orange for robots, Blue for controllers, Cyan for weld tables).",
        "🔌 Wiring Overlay: Allows workers to tap on machines to inspect connection paths instantly.",
        "📋 Inspection Planning: Single button access to '点検予定配線' (Scheduled Inspection Wiring) to view upcoming routes."
    ]
    add_bullets(tf_desc, bullets)
    
    img_path = 'app_wire_map.png'
    if os.path.exists(img_path):
        slide.shapes.add_picture(img_path, Inches(5.6), Inches(1.6), width=Inches(7.0))

    # ==========================================
    # SLIDE 5: Auditing & History Logs
    # ==========================================
    slide = prs.slides.add_slide(blank_layout)
    set_background(slide)
    add_slide_header(slide, "Audit Trails & Inspection History Logs")
    
    desc_box = slide.shapes.add_textbox(Inches(0.75), Inches(1.8), Inches(4.5), Inches(4.5))
    tf_desc = desc_box.text_frame
    tf_desc.word_wrap = True
    p = tf_desc.paragraphs[0]
    p.text = "Continuous Historical Tracking"
    p.font.name = FONT_TITLE
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT
    p.space_after = Pt(15)
    
    bullets = [
        "📜 Comprehensive History Log: List of completed inspection entries showing dates, technicians, and outcomes.",
        "🔍 Flexible Filtering: Easy filtering by Date, Equipment, Time Period (30/90 days), and Status (Normal/Repair/Abnormality).",
        "📊 High-Level Stats: Clear metrics summing up total inspections, repairs, and abnormalities discovered in a given window."
    ]
    add_bullets(tf_desc, bullets)
    
    img_path = 'app_history.png'
    if os.path.exists(img_path):
        slide.shapes.add_picture(img_path, Inches(5.6), Inches(1.6), width=Inches(7.0))

    # ==========================================
    # SLIDE 6: Live Bulletin Board & Incident Reporting
    # ==========================================
    slide = prs.slides.add_slide(blank_layout)
    set_background(slide)
    add_slide_header(slide, "Bulletin Board: Communication & Quick Action")
    
    desc_box = slide.shapes.add_textbox(Inches(0.75), Inches(1.8), Inches(4.5), Inches(4.5))
    tf_desc = desc_box.text_frame
    tf_desc.word_wrap = True
    p = tf_desc.paragraphs[0]
    p.text = "Real-time Collaboration"
    p.font.name = FONT_TITLE
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT
    p.space_after = Pt(15)
    
    bullets = [
        "💬 Integrated Incident Feed: Stream of reports directly from operators on the floor.",
        "🛠️ Actionable Items: '修理開始' (Start Repair) button right in the feed, enabling immediate response.",
        "🚨 Categorized Reports: Messages labeled with icons for Safety (安全), Warnings (警告), and Abnormalities (異常).",
        "✍️ Quick Communication: Bottom text field for posting real-time announcements."
    ]
    add_bullets(tf_desc, bullets)
    
    img_path = 'app_bulletin.png'
    if os.path.exists(img_path):
        slide.shapes.add_picture(img_path, Inches(5.6), Inches(1.6), width=Inches(7.0))

    # ==========================================
    # SLIDE 7: AI-Powered Troubleshooting Manuals
    # ==========================================
    slide = prs.slides.add_slide(blank_layout)
    set_background(slide)
    add_slide_header(slide, "Maintenance Manuals with AI Search")
    
    desc_box = slide.shapes.add_textbox(Inches(0.75), Inches(1.8), Inches(4.5), Inches(4.5))
    tf_desc = desc_box.text_frame
    tf_desc.word_wrap = True
    p = tf_desc.paragraphs[0]
    p.text = "AI-Driven Operator Support"
    p.font.name = FONT_TITLE
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT
    p.space_after = Pt(15)
    
    bullets = [
        "💡 Smart Search Box: Operators input complex machine symptoms (e.g. 'J3 joint vibrating').",
        "🤖 AI Q&A Integration: Provides immediate step-by-step instructions from local manuals.",
        "📖 Grouped Procedures: Categorized documentation for easy manual selection (Grinders, CO2 Welding Robots).",
        "📉 Reduced Downtime: Ensures workers have immediate access to resolutions without waiting for senior technicians."
    ]
    add_bullets(tf_desc, bullets)
    
    img_path = 'app_manuals.png'
    if os.path.exists(img_path):
        slide.shapes.add_picture(img_path, Inches(5.6), Inches(1.6), width=Inches(7.0))

    # ==========================================
    # SLIDE 8: Impact & Value
    # ==========================================
    slide = prs.slides.add_slide(blank_layout)
    set_background(slide)
    add_slide_header(slide, "The Value of Seibi App")
    
    # Grid Layout for 4 value propositions
    box_w = Inches(5.5)
    box_h = Inches(2.2)
    
    # Card 1: Operational Efficiency
    c1 = slide.shapes.add_textbox(Inches(0.75), Inches(1.8), box_w, box_h)
    tf1 = c1.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "⚡ Streamlined Daily Tasks"
    p1.font.name = FONT_TITLE
    p1.font.size = Pt(20)
    p1.font.bold = True
    p1.font.color.rgb = ACCENT_BLUE
    p1.space_after = Pt(10)
    add_bullets(tf1, ["Simplifies task checklists for technicians. Direct reporting prevents missed maintenance tasks and ensures smooth operations."])
    
    # Card 2: Reduced Downtime
    c2 = slide.shapes.add_textbox(Inches(6.8), Inches(1.8), box_w, box_h)
    tf2 = c2.text_frame
    tf2.word_wrap = True
    p2 = tf2.paragraphs[0]
    p2.text = "⏱️ Instant Incident Resolution"
    p2.font.name = FONT_TITLE
    p2.font.size = Pt(20)
    p2.font.bold = True
    p2.font.color.rgb = ACCENT_RED
    p2.space_after = Pt(10)
    add_bullets(tf2, ["Real-time bulletin board and 'Start Repair' button reduce communication lag. Machine problems are addressed immediately."])
    
    # Card 3: Visual Intelligence
    c3 = slide.shapes.add_textbox(Inches(0.75), Inches(4.3), box_w, box_h)
    tf3 = c3.text_frame
    tf3.word_wrap = True
    p3 = tf3.paragraphs[0]
    p3.text = "🗺️ Complete Spatial Map"
    p3.font.name = FONT_TITLE
    p3.font.size = Pt(20)
    p3.font.bold = True
    p3.font.color.rgb = ACCENT_GREEN
    p3.space_after = Pt(10)
    add_bullets(tf3, ["Visual Floor Map removes guesswork. Inspectors see the exact location and wiring path of the malfunctioning unit."])
    
    # Card 4: AI Support
    c4 = slide.shapes.add_textbox(Inches(6.8), Inches(4.3), box_w, box_h)
    tf4 = c4.text_frame
    tf4.word_wrap = True
    p4 = tf4.paragraphs[0]
    p4.text = "🤖 On-Demand Knowledge"
    p4.font.name = FONT_TITLE
    p4.font.size = Pt(20)
    p4.font.bold = True
    p4.font.color.rgb = TEXT_LIGHT
    p4.space_after = Pt(10)
    add_bullets(tf4, ["AI-integrated manual search acts as a 24/7 assistant, enabling junior operators to troubleshoot complex mechanical problems."])

    # Save presentation
    output_path = 'seibi_presentation.pptx'
    prs.save(output_path)
    print(f"Presentation successfully created at: {output_path}")

if __name__ == '__main__':
    create_presentation()
