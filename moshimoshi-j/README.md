# moshimoshi-J

[LLM-jp-Moshi-v1](https://huggingface.co/llm-jp/llm-jp-moshi-v1) の実行環境です。  
日本語フルデュプレックス音声対話モデルをuvで簡単に起動できます。

## 必要環境

- Linux（macOS非対応）
- GPU VRAM 24GB以上
- Python 3.10〜3.14
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## セットアップ

```bash
git clone https://github.com/tsukagoshi56/moshimoshi-J.git
cd moshimoshi-J/moshimoshi-j
make setup
```

## 起動

```bash
# localhost:8998 で起動
make run

# 外部公開（0.0.0.0:8998）
make run-public
```

または直接：

```bash
uv run python run.py --host localhost --port 8998
```

ブラウザで `http://localhost:8998` を開くと音声対話UIが表示されます。  
**ヘッドホン・イヤホン推奨**（スピーカー使用時はエコーが発生します）

## オプション

| オプション | デフォルト | 説明 |
|---|---|---|
| `--hf-repo` | `llm-jp/llm-jp-moshi-v1` | HuggingFaceリポジトリ |
| `--host` | `localhost` | バインドホスト |
| `--port` | `8998` | ポート番号 |

## 依存パッケージ

- [moshi](https://pypi.org/project/moshi/) <=0.2.2

## ライセンス

LLM-jp-Moshi-v1 は Apache License 2.0 で公開されています。  
詳細は [llm-jp/llm-jp-moshi](https://github.com/llm-jp/llm-jp-moshi) を参照してください。
