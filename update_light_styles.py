light_css = """/* Reset & Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Outfit', 'Noto Sans JP', sans-serif;
  background-color: #f8fafc;
  color: #0f172a;
  height: 100vh;
  width: 100vw;
  overflow: hidden;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

/* Background animated glow orbs - Soft Light Tones */
.bg-glow {
  position: absolute;
  border-radius: 50%;
  filter: blur(140px);
  z-index: 0;
  opacity: 0.35;
  pointer-events: none;
}

.bg-glow-1 {
  width: 600px;
  height: 600px;
  background: #dbeafe;
  top: -100px;
  right: -50px;
  animation: float-slow 20s infinite alternate;
}

.bg-glow-2 {
  width: 700px;
  height: 700px;
  background: #e0e7ff;
  bottom: -200px;
  left: -100px;
  animation: float-slow 25s infinite alternate-reverse;
}

@keyframes float-slow {
  0% { transform: translate(0, 0) scale(1); }
  50% { transform: translate(50px, 30px) scale(1.1); }
  100% { transform: translate(-30px, -50px) scale(0.9); }
}

/* Global Header */
.global-header {
  position: relative;
  z-index: 10;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 3rem;
  background: rgba(255, 255, 255, 0.9);
  border-bottom: 1px solid #e2e8f0;
  backdrop-filter: blur(8px);
}

.brand {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.brand-icon {
  font-size: 1.8rem;
  color: #2563eb;
}

.brand-text {
  font-size: 1.5rem;
  font-weight: 800;
  letter-spacing: 1px;
  color: #1e3a8a;
}

.slide-indicator {
  font-size: 1.1rem;
  font-weight: 700;
  background: #ffffff;
  color: #334155;
  padding: 0.5rem 1.2rem;
  border-radius: 20px;
  border: 1px solid #cbd5e1;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.03);
}

/* Slide Container & Layouts */
.presentation-container {
  flex-grow: 1;
  position: relative;
  z-index: 5;
  width: 94%;
  max-width: 1550px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
}

.slide {
  position: absolute;
  width: 100%;
  height: 96%;
  opacity: 0;
  pointer-events: none;
  transform: scale(0.97) translateY(20px);
  transition: opacity 0.6s cubic-bezier(0.25, 1, 0.5, 1), 
              transform 0.6s cubic-bezier(0.25, 1, 0.5, 1);
  display: flex;
  align-items: center;
  justify-content: center;
}

.slide.active {
  opacity: 1;
  pointer-events: auto;
  transform: scale(1) translateY(0);
}

.slide-content {
  width: 100%;
  height: 100%;
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 24px;
  padding: 2.2rem 3rem;
  box-shadow: 0 15px 35px rgba(15, 23, 42, 0.08);
  display: flex;
  overflow: hidden;
}

/* 1. Title Layout */
.title-layout {
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title-badge {
  background: #dbeafe;
  color: #1d4ed8;
  font-size: 0.95rem;
  font-weight: 700;
  padding: 0.6rem 1.4rem;
  border-radius: 30px;
  margin-bottom: 1.5rem;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

.main-title {
  font-size: 4.8rem;
  font-weight: 800;
  letter-spacing: -1px;
  background: linear-gradient(135deg, #1e3a8a, #2563eb);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 0.8rem;
}

.main-subtitle {
  font-size: 1.8rem;
  font-weight: 600;
  color: #475569;
  max-width: 800px;
  line-height: 1.4;
}

.title-divider {
  width: 80px;
  height: 4px;
  background: #2563eb;
  border-radius: 2px;
  margin: 2.2rem 0;
}

.presenter-tag {
  font-size: 1.1rem;
  color: #64748b;
  font-weight: 600;
}

/* 2. Problem Grid Layout */
.problem-layout {
  flex-direction: column;
}

.slide-title {
  font-size: 1.95rem;
  font-weight: 800;
  color: #0f172a;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.4rem;
}

.slide-title i {
  color: #2563eb;
}

.slide-subtitle {
  font-size: 1.15rem;
  color: #475569;
  margin-bottom: 2rem;
  font-weight: 500;
}

.problem-cards-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  flex-grow: 1;
}

.problem-card {
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  border-radius: 18px;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  transition: transform 0.3s ease;
  box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03);
}

.problem-card:hover {
  transform: translateY(-4px);
  border-color: #2563eb;
  box-shadow: 0 10px 25px rgba(37, 99, 235, 0.12);
}

.card-icon {
  width: 54px;
  height: 54px;
  border-radius: 14px;
  background: #dbeafe;
  color: #2563eb;
  font-size: 1.6rem;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.5rem;
}

.problem-card h3 {
  font-size: 1.4rem;
  color: #0f172a;
  font-weight: 700;
  margin-bottom: 0.8rem;
}

.problem-card p {
  font-size: 1.05rem;
  color: #475569;
  line-height: 1.65;
}

/* 3. Split Layout (Text + Visual) */
.split-layout {
  display: flex;
  gap: 3rem;
  align-items: center;
}

.text-col {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.bullet-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  margin-top: 1rem;
}

.bullet-list li {
  display: flex;
  align-items: flex-start;
  gap: 1.2rem;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  padding: 1.2rem 1.4rem;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
}

.list-num {
  font-family: 'Outfit', sans-serif;
  font-size: 1.1rem;
  font-weight: 800;
  color: #2563eb;
  background: #dbeafe;
  width: 42px;
  height: 42px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.list-text {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.list-text strong {
  font-size: 1.2rem;
  color: #0f172a;
  font-weight: 700;
}

.list-text span {
  font-size: 1rem;
  color: #475569;
  line-height: 1.5;
}

.visual-col {
  flex: 1.1;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.video-frame {
  width: 100%;
  border-radius: 18px;
  overflow: hidden;
  background: #ffffff;
  border: 1px solid #cbd5e1;
  box-shadow: 0 12px 30px rgba(15, 23, 42, 0.1);
  display: flex;
  flex-direction: column;
}

.app-video {
  width: 100%;
  height: auto;
  max-height: 460px;
  object-fit: cover;
  display: block;
}

.video-caption {
  padding: 0.8rem 1.2rem;
  background: #f8fafc;
  color: #475569;
  font-size: 0.95rem;
  font-weight: 600;
  border-top: 1px solid #e2e8f0;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.video-caption i {
  color: #2563eb;
}

/* 4. Predictive Maintenance Visual Card */
.predictive-card {
  width: 100%;
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 18px;
  padding: 1.8rem;
  box-shadow: 0 10px 25px rgba(15, 23, 42, 0.06);
}

.card-header-predictive {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 1.25rem;
  font-weight: 800;
  color: #1e3a8a;
  margin-bottom: 1.4rem;
  padding-bottom: 0.8rem;
  border-bottom: 1px solid #e2e8f0;
}

.card-header-predictive i {
  color: #2563eb;
}

.stat-body {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}

.stat-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 1rem;
}

.stat-label {
  color: #334155;
  font-weight: 600;
}

.stat-val {
  font-weight: 700;
  font-size: 0.95rem;
}

.val-danger { color: #dc2626; }
.val-warning { color: #d97706; }

.progress-bar-light {
  width: 100%;
  height: 8px;
  background: #f1f5f9;
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill-light {
  height: 100%;
  border-radius: 4px;
}

.fill-danger { background: #dc2626; }
.fill-warning { background: #d97706; }

.predictive-action {
  margin-top: 1.4rem;
  padding: 1.2rem;
  background: #eff6ff;
  border: 1px solid #bfdbfe;
  border-radius: 14px;
}

.action-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: #1e40af;
  margin-bottom: 0.4rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.predictive-action p {
  font-size: 0.98rem;
  color: #1e3a8a;
  line-height: 1.55;
}

/* 5. Value Grid Layout (Future AI) */
.value-layout {
  flex-direction: column;
  align-items: center;
}

.value-title {
  text-align: center;
  justify-content: center;
}

.value-subtitle {
  text-align: center;
  margin-bottom: 2rem;
}

.value-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
  width: 100%;
  max-width: 1100px;
}

.value-card {
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  border-radius: 18px;
  padding: 2.2rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
}

.value-card-icon {
  width: 50px;
  height: 50px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  margin-bottom: 1.2rem;
}

.accent-color-blue { background: #dbeafe; color: #2563eb; }
.accent-color-green { background: #d1fae5; color: #059669; }

.value-card h3 {
  font-size: 1.4rem;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 0.8rem;
}

.value-card p {
  font-size: 1.05rem;
  color: #475569;
  line-height: 1.6;
}

.closing-statement {
  margin-top: 2.5rem;
  font-size: 1.2rem;
  font-weight: 700;
  color: #1d4ed8;
  text-align: center;
}

/* 6. Section Intro Layout (Agenda/Map) */
.section-intro-layout {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  height: 100%;
}

.section-intro-title {
  font-size: 2.8rem;
  font-weight: 800;
  color: #0f172a;
  margin-bottom: 2rem;
  letter-spacing: -0.5px;
}

.section-intro-list {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  width: 100%;
  max-width: 650px;
}

.section-intro-item {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  padding: 1.2rem 2rem;
  border-radius: 16px;
  box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
}

.section-intro-index {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #2563eb;
  color: #ffffff;
  font-weight: 800;
  font-size: 1.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.section-intro-text {
  font-size: 1.35rem;
  font-weight: 700;
  color: #0f172a;
}

/* Global Footer Controls */
.global-footer {
  position: relative;
  z-index: 10;
  padding: 0.8rem 3rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(to top, rgba(248, 250, 252, 0.9), rgba(248, 250, 252, 0));
}

.navigation-controls {
  display: none;
}

.progress-bar-container {
  width: 100%;
  max-width: 1550px;
  height: 4px;
  background: #e2e8f0;
  border-radius: 2px;
  overflow: hidden;
}

.progress-bar {
  height: 100%;
  width: 8.33%;
  background: #2563eb;
  transition: width 0.4s ease;
}
"""

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(light_css)

print("Updated styles.css to high-contrast Light Theme successfully.")
