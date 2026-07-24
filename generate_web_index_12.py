import os

html_content = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Seibi - 設備点検・不具合管理アプリのご紹介</title>

  <!-- Google Fonts: Outfit & Noto Sans JP -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <!-- Main Stylesheet -->
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Background Glow Elements -->
  <div class="bg-glow bg-glow-1"></div>
  <div class="bg-glow bg-glow-2"></div>

  <!-- Global Header -->
  <header class="global-header">
    <div class="brand">
      <i class="fa-solid fa-briefcase brand-icon"></i>
      <span class="brand-text">Seibi</span>
    </div>
    <div class="slide-indicator">
      <span id="current-slide-num">1</span> / <span id="total-slides-num">12</span>
    </div>
  </header>

  <!-- Presentation Main Container -->
  <main class="presentation-container" id="presentation-container">

    <!-- SLIDE 1: タイトル (Title) -->
    <section class="slide active" id="slide-1" data-slide="1">
      <div class="slide-content title-layout">
        <div class="title-badge"><i class="fa-solid fa-industry"></i> 現場改善プロジェクト報告</div>
        <h1 class="main-title">Seibi</h1>
        <p class="main-subtitle">設備点検・不具合管理アプリのご紹介</p>
        <div class="title-divider"></div>
        <p class="presenter-tag"><i class="fa-solid fa-user-gear"></i> 溶接ラインチーム</p>
      </div>
    </section>

    <!-- SLIDE 2: 背景と課題 (Background) -->
    <section class="slide" id="slide-2" data-slide="2">
      <div class="slide-content problem-layout">
        <h2 class="slide-title"><i class="fa-solid fa-triangle-exclamation"></i> 背景と課題</h2>
        <p class="slide-subtitle">紙の点検表運用による3つの現場課題</p>
        
        <div class="problem-cards-grid">
          <!-- Problem 1 -->
          <div class="problem-card">
            <div class="card-icon"><i class="fa-solid fa-file-circle-xmark"></i></div>
            <h3>履歴の散逸</h3>
            <p>手書きの点検表は提出後に保管または破棄され、検索可能なデジタル記録が残らない状態でした。</p>
          </div>

          <!-- Problem 2 -->
          <div class="problem-card">
            <div class="card-icon"><i class="fa-solid fa-rotate-left"></i></div>
            <h3>追跡の困難</h3>
            <p>同じトラブルが繰り返し発生しても記憶に頼るしかなく、発見された異常が確実に修理されたか確認できませんでした。</p>
          </div>

          <!-- Problem 3 -->
          <div class="problem-card">
            <div class="card-icon"><i class="fa-solid fa-book-open-reader"></i></div>
            <h3>作業の非効率</h3>
            <p>トラブル対応時に紙のマニュアルを探してめくるか、特定の人に質問するしか選択肢がありませんでした。</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 3: 解決策と取り組み (Solutions Intro) -->
    <section class="slide" id="slide-3" data-slide="3">
      <div class="slide-content section-intro-layout">
        <h2 class="section-intro-title">解決策と取り組み</h2>
        <div class="section-intro-list">
          <div class="section-intro-item">
            <span class="section-intro-index">1</span>
            <span class="section-intro-text">点検業務のデジタル化と履歴保存</span>
          </div>
          <div class="section-intro-item">
            <span class="section-intro-index">2</span>
            <span class="section-intro-text">レイアウトマップによる視覚管理</span>
          </div>
          <div class="section-intro-item">
            <span class="section-intro-index">3</span>
            <span class="section-intro-text">リアルタイムの状況共有とタスク管理</span>
          </div>
          <div class="section-intro-item">
            <span class="section-intro-index">4</span>
            <span class="section-intro-text">AI搭載の修理サポート機能</span>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 4: 解決策(1) 点検業務のデジタル化 -->
    <section class="slide" id="slide-4" data-slide="4">
      <div class="slide-content split-layout">
        <div class="text-col">
          <h2 class="slide-title"><i class="fa-solid fa-tablet-screen-button"></i> 解決策：点検業務のデジタル化</h2>
          <p class="slide-subtitle">モバイル端末でその場入力・ペーパーレス化</p>
          
          <ul class="bullet-list">
            <li>
              <div class="list-num">01</div>
              <div class="list-text">
                <strong>現場でのモバイル入力</strong>
                <span>スマホやタブレットから直接点検表を入力。転記ミスや紛失を防止します。</span>
              </div>
            </li>
            <li>
              <div class="list-num">02</div>
              <div class="list-text">
                <strong>検索可能な履歴の蓄積</strong>
                <span>点検データや過去の不具合履歴がクラウドへ保存され、いつでも検索可能です。</span>
              </div>
            </li>
          </ul>
        </div>
        
        <div class="visual-col">
          <div class="video-frame">
            <video autoplay loop muted playsinline class="app-video">
              <source src="videos/dashboard.webm" type="video/webm">
              お使いのブラウザは動画タグに対応していません。
            </video>
            <div class="video-caption"><i class="fa-solid fa-circle-play"></i> 点検ダッシュボード画面</div>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 5: 解決策(1-追加) 検索可能な履歴ログ -->
    <section class="slide" id="slide-5" data-slide="5">
      <div class="slide-content split-layout">
        <div class="text-col">
          <h2 class="slide-title"><i class="fa-solid fa-database"></i> 解決策：検索可能な履歴ログ</h2>
          <p class="slide-subtitle">過去の不具合や修理記録を瞬時に検索</p>
          
          <ul class="bullet-list">
            <li>
              <div class="list-num">01</div>
              <div class="list-text">
                <strong>即座のキーワード検索</strong>
                <span>日付や設備名、症状を入力するだけで、過去の修理履歴をその場で参照できます。</span>
              </div>
            </li>
            <li>
              <div class="list-num">02</div>
              <div class="list-text">
                <strong>再発トラブルの把握</strong>
                <span>過去にどんな対応をしたかが可視化され、熟練者に頼らず迅速な対応を可能にします。</span>
              </div>
            </li>
          </ul>
        </div>
        
        <div class="visual-col">
          <div class="video-frame">
            <video autoplay loop muted playsinline class="app-video">
              <source src="videos/history.webm" type="video/webm">
              お使いのブラウザは動画タグに対応していません。
            </video>
            <div class="video-caption"><i class="fa-solid fa-circle-play"></i> 履歴検索ログ画面</div>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 6: 解決策(2) レイアウトマップによる視覚管理 [RESTORED] -->
    <section class="slide" id="slide-6" data-slide="6">
      <div class="slide-content split-layout">
        <div class="text-col">
          <h2 class="slide-title"><i class="fa-solid fa-map-location-dot"></i> 解決策：レイアウトマップによる視覚管理</h2>
          <p class="slide-subtitle">平面図上で設備配置と配線ルートを直感的に把握</p>
          
          <ul class="bullet-list">
            <li>
              <div class="list-num">01</div>
              <div class="list-text">
                <strong>インタラクティブレイアウトマップ</strong>
                <span>ロボットやレギュレーター等の配置や異常ステータスを、マップ上で一目に視認可能。</span>
              </div>
            </li>
            <li>
              <div class="list-num">02</div>
              <div class="list-text">
                <strong>配線ルートの可視化</strong>
                <span>機器をタップするだけで配線系統を表示し、トラブル箇所の特定をスピード化。</span>
              </div>
            </li>
          </ul>
        </div>
        
        <div class="visual-col">
          <div class="video-frame">
            <video autoplay loop muted playsinline class="app-video">
              <source src="videos/wire_map.webm" type="video/webm">
              お使いのブラウザは動画タグに対応していません。
            </video>
            <div class="video-caption"><i class="fa-solid fa-circle-play"></i> レイアウトマップ画面</div>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 7: 解決策(3) リアルタイムの状況共有と管理 -->
    <section class="slide" id="slide-7" data-slide="7">
      <div class="slide-content split-layout">
        <div class="text-col">
          <h2 class="slide-title"><i class="fa-solid fa-comments"></i> 解決策：状況共有と管理</h2>
          <p class="slide-subtitle">自動タスク登録とLINE WORKS通知で連絡漏れを防止</p>
          
          <ul class="bullet-list">
            <li>
              <div class="list-num">01</div>
              <div class="list-text">
                <strong>自動タスク化＆通知</strong>
                <span>異常「あり」と回答されると自動で修理タスクが登録され、LINE WORKSへ即座に緊急通知されます。</span>
              </div>
            </li>
            <li>
              <div class="list-num">02</div>
              <div class="list-text">
                <strong>全デバイス同期</strong>
                <span>修理の進捗状況や掲示板の内容が、すべてのデバイス（モバイル・PC）へリアルタイムに同期されます。</span>
              </div>
            </li>
          </ul>
        </div>
        
        <div class="visual-col">
          <div class="video-frame">
            <video autoplay loop muted playsinline class="app-video">
              <source src="videos/bulletin.webm" type="video/webm">
              お使いのブラウザは動画タグに対応していません。
            </video>
            <div class="video-caption"><i class="fa-solid fa-circle-play"></i> 掲示板＆タスク同期画面</div>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 8: 解決策(4) AI搭載の修理サポート機能 -->
    <section class="slide" id="slide-8" data-slide="8">
      <div class="slide-content split-layout">
        <div class="text-col">
          <h2 class="slide-title"><i class="fa-solid fa-brain"></i> 解決策：AI修理サポート</h2>
          <p class="slide-subtitle">現場ですぐに頼れるAIアドバイザー機能</p>
          
          <ul class="bullet-list">
            <li>
              <div class="list-num">01</div>
              <div class="list-text">
                <strong>普段の言葉で質問応答</strong>
                <span>マニュアルをめくる代わりに、自然な言葉でトラブル症状を質問できます。</span>
              </div>
            </li>
            <li>
              <div class="list-num">02</div>
              <div class="list-text">
                <strong>明確な引用元ページ提示</strong>
                <span>AIは取り込んだマニュアルを参照し、根拠となるページや項番を示して回答します。</span>
              </div>
            </li>
          </ul>
        </div>
        
        <div class="visual-col">
          <div class="video-frame">
            <video autoplay loop muted playsinline class="app-video">
              <source src="videos/manuals.webm" type="video/webm">
              お使いのブラウザは動画タグに対応していません。
            </video>
            <div class="video-caption"><i class="fa-solid fa-circle-play"></i> AIチャットサポート画面</div>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 9: 成果と今後の展望 (Outlook Intro) -->
    <section class="slide" id="slide-9" data-slide="9">
      <div class="slide-content section-intro-layout">
        <h2 class="section-intro-title">成果と今後の展望</h2>
        <div class="section-intro-list">
          <div class="section-intro-item">
            <span class="section-intro-index">1</span>
            <span class="section-intro-text">データ主導の予防保全</span>
          </div>
          <div class="section-intro-item">
            <span class="section-intro-index">2</span>
            <span class="section-intro-text">AI対応マニュアルの拡大</span>
          </div>
          <div class="section-intro-item">
            <span class="section-intro-index">3</span>
            <span class="section-intro-text">使うほど賢くなるAI学習ループ</span>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 10: 今後の展望：データ主導の保全 -->
    <section class="slide" id="slide-10" data-slide="10">
      <div class="slide-content split-layout">
        <div class="text-col">
          <h2 class="slide-title"><i class="fa-solid fa-chart-line"></i> 今後の展望：データ主導の保全</h2>
          <p class="slide-subtitle">点検ログの傾向から故障を予測し未然防止</p>
          
          <ul class="bullet-list">
            <li>
              <div class="list-num">01</div>
              <div class="list-text">
                <strong>溶接機ログの予兆検知</strong>
                <span>点検表の「ワイヤ送給のもたつき」や「滑り」の頻度から、ライン停止のサインを検知。</span>
              </div>
            </li>
            <li>
              <div class="list-num">02</div>
              <div class="list-text">
                <strong>予測交換によるダウンタイムゼロ</strong>
                <span>ライナーの詰まりや駆動部の摩耗期を特定し、次回段取り時に交換してトラブルを防止。</span>
              </div>
            </li>
          </ul>
        </div>
        
        <div class="visual-col">
          <div class="predictive-card">
            <div class="card-header-predictive">
              <i class="fa-solid fa-microchip"></i>
              <span>溶接機 状態モニター（過去5ヶ月間）</span>
            </div>
            
            <div class="stat-body">
              <div class="stat-row">
                <span class="stat-label">ワイヤ送給のもたつき:</span>
                <span class="stat-val val-danger">3回検出 (警告値 2回)</span>
              </div>
              <div class="progress-bar-light"><div class="progress-fill-light fill-danger" style="width: 100%"></div></div>
              
              <div class="stat-row" style="margin-top: 1rem;">
                <span class="stat-label">ワイヤの滑り:</span>
                <span class="stat-val val-warning">2回検出 (注意値 1回)</span>
              </div>
              <div class="progress-bar-light"><div class="progress-fill-light fill-warning" style="width: 66%"></div></div>

              <div class="predictive-action">
                <div class="action-title"><i class="fa-solid fa-wrench"></i> 推奨アクション:</div>
                <p>点検記録より「もたつき」「滑り」の再発傾向を検知。金属粉による詰まりを防ぐため、次回段取り替え時にコンジットライナー交換を推奨します。</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 11: 今後の展望：AI機能の高度化 -->
    <section class="slide" id="slide-11" data-slide="11">
      <div class="slide-content value-layout">
        <h2 class="slide-title value-title"><i class="fa-solid fa-circle-nodes"></i> 今後の展望：AI機能の高度化</h2>
        <p class="slide-subtitle value-subtitle">全設備のカバーとAI自律学習の確立</p>
        
        <div class="value-grid">
          <div class="value-card">
            <div class="value-card-icon accent-color-blue"><i class="fa-solid fa-file-medical"></i></div>
            <h3>AI対応マニュアルの拡大</h3>
            <p>工場内のすべての主要設備の手順書・図面データをAIへ順次取り込み、全域をサポート可能にします。</p>
          </div>
          
          <div class="value-card">
            <div class="value-card-icon accent-color-green"><i class="fa-solid fa-rotate"></i></div>
            <h3>使うほど賢くなるAI学習ループ</h3>
            <p>質問ログとフィードバック（役に立ったか）を分析。良回答を保存・学習し、精度を向上させます。</p>
          </div>
        </div>
        
        <div class="closing-statement">
          <p>Seibi: 製造現場のダウンタイムをゼロにし、組織の保全力と稼働率を最大化するソリューション</p>
        </div>
      </div>
    </section>

    <!-- SLIDE 12: 閉会 (Closing) -->
    <section class="slide" id="slide-12" data-slide="12">
      <div class="slide-content section-intro-layout">
        <h2 class="section-intro-title" style="font-size: 3.5rem; color: #059669; margin-bottom: 1.5rem;">ご清聴ありがとうございました</h2>
        <p class="slide-subtitle" style="font-size: 1.5rem; color: #64748b;">設備管理システム — Seibi</p>
      </div>
    </section>

  </main>

  <!-- Global Footer Controls -->
  <footer class="global-footer">
    <div class="navigation-controls">
      <button class="nav-btn" id="prev-btn"><i class="fa-solid fa-chevron-left"></i> 前へ</button>
      <div class="slide-bullets" id="slide-bullets-container"></div>
      <button class="nav-btn" id="next-btn">次へ <i class="fa-solid fa-chevron-right"></i></button>
    </div>
    <div class="progress-bar-container">
      <div class="progress-bar" id="progress-bar-fill"></div>
    </div>
  </footer>

  <!-- JavaScript logic -->
  <script src="slides.js"></script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated 12-slide index.html successfully.")
