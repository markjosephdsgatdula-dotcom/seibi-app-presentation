# 設備点検アプリ プレゼンテーション原稿（日本語・ローマ字）

## 🎤 Opening (オープニング)

### 🇯🇵 Japanese:
皆様、おはようございます。溶接ラインのマークです。
本日、私たちが開発・導入した「設備点検アプリ (Seibi)」の取り組みについてご報告いたします。

### 🔤 Romaji:
Minasama, ohayou gozaimasu. Yousetsu rain no Maaku desu.
Honjitsu, watashitachi ga kaihatsu・dounyuu shita "Setsubi Tenken Apuri (Seibi)" no torikumi ni tsuite go-houkoku itashimasu.

---

## 1. Background & Challenges (背景と課題)

### 🇯🇵 Japanese:
これまで、私たちの現場では設備点検をすべて「紙の点検表」で行っていました。手書きの紙は提出後にファイル保管されるか破棄され、後から検索できる記録が残らない状態でした。

その結果、主に3つの課題が生じていました：
1. **履歴の散逸**: 同じトラブルが繰り返されても記憶に頼るしかなかったこと。
2. **追跡の困難**: 発見された異常が本当に修理されたか確認できなかったこと。
3. **作業の非効率**: 修理中に紙のマニュアルを探してめくるか、人に聞くしかなかったこと。

### 🔤 Romaji:
Kore made, watashitachi no genba dewa setsubi tenken wo subete "kami no tenken-hyou" de okonatte imashita. Tegaki no kami wa teishutsu-go ni fairu hokan sareru ka haki sare, ato kara kensaku dekiru kiroku ga nokoranai joutai deshita.

Sono kekka, omo ni mittsu no kadai ga shoujite imashita:
1. **Rireki no san-itsu**: Onaji toraburu ga kurikaesarete mo kioku ni tayoru shika nakatta koto.
2. **Tsuiseki no konnan**: Hakken sareta ijou ga hontou ni shuuri sareta ka kakunin dekina katta koto.
3. **Sagyou no hi-kouritsu**: Shuuri-chuu ni kami no manyuaru wo sagashite mekuru ka, hito ni kiku shika nakatta koto.

---

## 2. Solutions & Key Features (解決策と取り組み)

### 🇯🇵 Japanese:
これらの課題を解決するため、現場の安全・品質・稼働率向上を目指してアプリを構築しました。主なポイントは以下の4つです。

1. **点検業務のデジタル化と履歴保存**: スマホやタブレットからその場で入力。不具合や点検の履歴がデジタルデータとして蓄積され、いつでも検索可能になりました。
2. **レイアウトマップによる視覚管理**: ロボットやレギュレーター等の配置と状態を、平面図（マップ）上で直感的に把握できるようにしました。配線ルートや異常箇所が一目でわかります。
3. **リアルタイムの状況共有とタスク管理**: 異常が入力されると自動で修理タスク化され、全デバイスや（田中さんのご協力により連携した）LINE WORKSへ即座に通知。報告漏れや未修理を防ぎます。
4. **AI搭載の修理サポート機能**: 紙のマニュアルをめくる代わりに、普段の言葉でAIに質問できます。AIが取り込んだマニュアルと知識ベースを参照し、該当ページを示して即座に回答します。

### 🔤 Romaji:
Kore-ra no kadai wo kaiketsu suru tame, genba no anzen・hinstu・kadouritsu koujou wo mezashite apuri wo kouchiku shimashita. Omo na pointo wa ika no yottsu desu.

1. **Tenken gyoumu no dejitaru-ka to rireki hokan**: Sumaho ya taburetto kara sono ba de nyuuryoku. Fuguai ya tenken no rireki ga dejitaru deeta to shite chukuseki sare, itsu demo kensaku kanou ni narimashita.
2. **Reiauto mappu ni yoru shikaku kanri**: Robotto ya regyureetaa nado no haichi to joutai wo, heimenzu (mappu) jou de chokkan-teki ni haaku dekiru you ni shimashita. Haisen ruuto ya ijou kasho ga hitome de wakarimasu.
3. **Riaru-taimu no joukyou kyouyuu to tasuku kanri**: Ijou ga nyuuryoku sareru to jidou de shuuri tasuku-ka sare, zen devaisu ya (Tanaka-san no go-kyouryoku ni yori renkei shita) LINE WORKS he sokuza ni tsuuchi. Houkoku-mori ya mi-shuuri wo fusagimasu.
4. **AI tousai no shuuri sapooto kinou**: Kami no manyuaru wo mekuru kawari ni, fudan no kotoba de AI ni shitsumon dekimasu. AI ga torikonda manyuaru to chishiki beeshi wo sanshou shi, gaitou peeji wo shimeshite sokuza ni kaitou shimasu.

---

## 3. Results & Future Outlook (成果と今後の展望)

### 🇯🇵 Japanese:
今月から運用を開始し、点検履歴の共有、自動通知による迅速な対応、マニュアル検索時間の削減などの効果を期待しております。

今後はさらに以下の3点に取り組みます：
1. **データ主導の予防保全**: 点検ログ（「ワイヤ送給のもたつき」や「滑り」など）の発生傾向を分析し、トラブルが起きる前にコンジットライナーの交換時期を予測。アーク切れやライン停止を未然に防ぎます。
2. **AI対応マニュアルの拡大**: 工場内のすべての主要設備の手順書や図面をAIへ順次取り込み、サポート範囲を全域へ拡大します。
3. **使うほど賢くなるAI学習ループ**: 現場からの質問とフィードバックを蓄積し、AIの回答精度を自律的に向上させます。

### 🔤 Romaji:
Kon-getsukara un'you wo kaishi shi, tenken rireki no kyouyuu, jidou tsuuchi ni yoru jinsoku na taiou, manyuaru kensaku jikan no sakugen nado no kouka wo kitai shite orimasu.

Kongo wa sara ni ika no san-ten ni torikumimasu:
1. **Deeta shudou no yobou hozen**: Tenken rogu ("waiya soukyuu no motatsuki" ya "suberi" nado) no hassei keikou wo bunseki shi, toraburu ga okiru mae ni konjitto rainaa no koukan shiki wo yosoku. Aaku-kire ya rain teishi wo mizen ni fusagimasu.
2. **AI taiou manyuaru no kakudai**: Koujou-nai no subete no shuyou setsubi no tejun-sho ya zumen wo AI he junji torikomi, sapooto han-i wo zen-iki he kakudai shimasu.
3. **Tsukau hodo kashikoku naru AI gakushuu ruupu**: Genba kara no shitsumon to fiidobakku wo chukuseki shi, AI no kaitou seido wo jiritsu-teki ni koujou sasemasu.

---

## 🎤 Closing (クロージング)

### 🇯🇵 Japanese:
このアプリは、単なる紙のデジタル化ではありません。
現場のダウンタイムをゼロにし、全員が安全に、最高の状態で設備を動かし続けるためのツールです。

ご清聴ありがとうございました。

### 🔤 Romaji:
Kono apuri wa, tannaru kami no dejitaru-ka dewa arimasen.
Genba no daun-taimu wo zero ni shi, zen'in ga anzen ni, saikou no joutai de setsubi wo ugokashi tsuzukeru tame no tsuuru desu.

Go-seichou arigatou gozaimashita.
