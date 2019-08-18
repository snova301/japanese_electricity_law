# japanese_electricity_law

## 概要
日本の電気に関する法令をまとめます。
コードや内容は随時更新していきます。

各ファイル、フォルダの説明

```yaml
get_law.py : e-Govから法令を取得
lawlist.xml : 法令の一覧(2019/08/17取得)
law_xml : e-Govから取得された法令のxmlファイル置き場
```

## 仕様

- 法律の改正があったときに更新履歴がわかる
- 二次利用できるようにxml, json等に保存できる
- 著作権保護されている規格は本文を記載せず、リンクを貼る


## 法令の収集

法令とは、法律や省令などを総称した表現です。
電気設備や工事等に関係する法令を以下にまとめます。

- 電気事業法(施行令、施行規則含む)
- 電気設備に関する技術基準を定める省令(電技)
- 電気設備の技術基準の解釈
- 電気関係報告規則
- 電気工事士法(施行令、施行規則含む)
- 電気工事業の業務の適正化に関する法律(施行令、施行規則含む)
- 電気用品安全法(施行令、施行規則含む)
- 労働安全衛生法(施行令含む)
- 消防法(施行令、施行規則含む)

上記の法令をe-Govから取得します。
取得方法は[公式のPDFマニュアル](https://www.e-gov.go.jp/elaws/pdf/houreiapi_shiyosyo.pdf)を参考にしました。

コードの使い方はこちらを参照してください。


## 規格の収集

電気設備に関係する規格を以下にまとめました。

- JIS規格(日本産業規格)
- JEC規格(電気規格調査会規格)
- 内線規定(需要設備における電気設備設計の規格)

※JISは日本工業規格の略でしたが、2019/07/01に日本語名が日本産業規格となりました。今後、データ等の標準化も進んでいきます。詳しくは[経産省のHP](https://www.meti.go.jp/policy/economy/hyojun-kijun/jisho/jis.html)で。

なお、多くの規格が民間規格なので、著作権のためGithubに上げることはできませんでした。


### JIS規格

[国立国会図書館のHP](https://rnavi.ndl.go.jp/research_guide/entry/theme-honbun-400392.php)を見てみると、JIS規格は規格表と呼ばれる冊子を[検索](https://ndlonline.ndl.go.jp/#!/)、閲覧するか、[JISCのHP](https://www.jisc.go.jp/app/jis/general/GnrDataBaseSearch.html)から調べることができます。

また、個人や法人が運営するサイトでも一部公開や規格の解説されています。

- [kikakurui.com](https://kikakurui.com/)


### JEC規格

[電気学会　電気規格調査会](http://www.iee.or.jp/honbu/jec/index.htm)が作成している規格です。

規格の内容は公開していません。
中身を知りたい場合は[電気学会のHP](https://www.iee.jp/pub/jec/)で冊子または電子版を購入してください。


### 内線規定

電気需要場所における電気設備の保安を確保するための民間規格です。
電力会社によって付録が違います。

規格の内容は公開していません。
内容を知りたい場合は[電気協会のHP](https://store.denki.or.jp/products/detail/301)で購入してください。


## 今後の展開
- データ形式の追加(json, yaml等)
- HTML、CSSなどを使ってレイアウトを整える
- 法律改正後自動取得
- 電気設備に関連した新規の法律の自動取得
- 法律名の部分検索に対応した
- 情報システムに関連する法律(サイバーセキュリティ基本法、不正アクセス禁止法等)への展開
- 電気通信法規(電気通信事業法、電波法等)への展開
- 機械、建築に関連する法律(高圧ガス保安法、建築基準法等)への展開
- 法令から遮断容量等を計算するツールの開発


## おわりに
ミスや法令のまとめ方についてご意見ありましたら、ご連絡ください。
