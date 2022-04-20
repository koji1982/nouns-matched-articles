# nouns-matched-article

語句の一致率による記事選出サイト
https://www.selected-article-2021.info/


### 概要
スクレイピングで集めたYahooニュースの記事に対して評価（「いいね」、「興味なし」）を行ってもらい、
その評価をもとにして評価者への推奨候補、除去候補となる記事を提示するサイトです。


---


・システムの構成
AWS EC2上にDocker Composeでコンテナを立て、コンテナ上のApacheでサーバー通信を行っています。
バックエンドではDjangoを使用し、データベースはDjangoモデル経由でDocker ComposeコンテナのMySQLを
使用しています。


・記事の収集、スクレイピングツール
Scrapyのspiderをクローラーとして使い、spiderの処理の中でBeautifulSoupを使用して
スクレイピングを行っています。Scrapyの定期クローリングをcronで行っています。
その他ブラウザテストでSeleniumを使用しています。


・記事の選出方法
それぞれの記事から語句（名詞）を抽出しておき、評価された記事の語句（名詞群）を基準として、
その基準に対してそれぞれの記事がどれだけそれらの語句と一致するかを判定し、
「いいね」の語句に対しては推奨候補、「興味なし」の語句に対しては除去候補として、
一致した割合が高い順に並べています。


・開発環境
使用PCはUbuntu16.04、エディタはローカルもリモートもVSCodeを使用しています。
VCSはGitHubで、CI/CDはCircleCIを使用しています。
