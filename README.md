# 概要
- 個人的に副業を探すためのcrawlerです
- 個人で探すためのものなので、条件設定部分を汎用的に作るとかはあんまり考えてないです

# 詳細
- Scrapyを使用する
- Crawling (対象のhtmlファイルをダウンロード) -> Scraping (ダウンロードしたHTMLを解析)の順に処理する
  - 先方のサーバに迷惑かけるのはNGなので、詳細ページまで再起的に辿ることはせず、一覧画面の情報だけを取得する
  - 収集間隔は3秒とする
    - 基本は1つの対象に月１ページ分しか見ない想定
    - ページングするほど案件があった場合は、3秒ごとに次のページをダウンロードしてくる(未実装)
- 情報抽出した結果を、resultファイルに吐く
  - 詳細未決定

# 対象
- doocy job
  - https://doocy.jp/fukugyo
- findy freelance
  - https://freelance.findy-code.io/works
- ITPRO PERTNERS
  - https://itpropartners.com/job/search

# 条件
- 週１〜2日勤務想定
- 使用言語はJava / Python
- 職種はエンジニア

# 環境構築手順
- pipが入っていることが前提
  - 入っていない場合は[こちら](https://qiita.com/suzuki_y/items/3261ffa9b67410803443)を参照
- git clone後、以下コマンドを打つ
  - pip install scrapy
  - scrapy --version
- scrapyコマンドが見つからない場合は以下を実行
  - pip show -f Scrapy | grep -e "/bin" -e "Location"
  - 出力されたLocationのディレクトリから、同じく出力されたbinの相対パスの場所に、パスを通す
    - vi ~/.bash_profile
    - export PATH=\${PATH}:(出力されたパスの絶対パスを入力) を追加
      - 例：export PATH=\${PATH}:\${HOME}/Library/Python/2.7/bin
    - source .bash_profile
    - scrapy --version

# (参考用)初期構築時実行コマンド
- scrapy startproject crawler_side_business
- scrapy genspider -t crawl doocy doocy.jp/fukugyo
- scrapy genspider -t crawl findy-freelance freelance.findy-code.io/works
- scrapy genspider -t crawl itpro-partners itpropartners.com/job/search

# リンク
- [Python製クローラー「Scrapy」の始め方メモ](https://sechiro.hatenablog.com/entry/2016/04/02/Python%E8%A3%BD%E3%82%AF%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%E3%80%8CScrapy%E3%80%8D%E3%81%AE%E5%A7%8B%E3%82%81%E6%96%B9%E3%83%A1%E3%83%A2)