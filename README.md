---

# 表情包仓库概述

欢迎来到表情包仓库！这里是一个收集各种精美表情包的聚集地，为您的聊天、社交和表达情感提供了丰富多彩的选择。无论您需要表达的是开心、难过、惊讶还是其他情感，这里都有一个适合的表情等待着您。

## 介绍

- [源仓库](https://github.com/willow-god/owo)，适当删减，达到个人需求！

## 表情包列表

以下是本仓库目前收集的一些表情包，共 9 个系列、424 个表情，欢迎随时查看和使用：

- **Blobcat 动态表情包**（可爱猫）：多种生动有趣的 Blobcat 动态表情，每一种都展现了 Blobcat 的可爱和俏皮。无论是表达情感、分享心情，还是幽默地传递讯息，都是绝佳的选择。共 54 种。
  - [点击查看详情](./blobcat/)
- **Bilibili 小电视**（小电视）：Bilibili 小电视系列表情，生动展现各种常见情绪，共 21 种。
  - [点击查看详情](./bilibili/)
- **Catbug 猫猫虫**（猫猫虫）：软萌的猫猫虫系列动态表情，可爱又治愈，共 32 种。
  - [点击查看详情](./catbug/)
- **Heybox 方块脸**（方块脸）：源自游戏社区的方块脸 Heybox 系列表情，诙谐有趣，共 36 种。
  - [点击查看详情](./heybox/)
- **明日方舟**：明日方舟系列表情，角色日常与吐槽一应俱全，共 81 种。
  - [点击查看详情](./Arknights/)
- **孤独摇滚**：孤独摇滚（Bocchi the Rock!）系列表情，社恐日常生动还原，共 25 种。
  - [点击查看详情](./GuduYaoGun/)
- **卡拉彼丘**：卡拉彼丘（Strinova）系列表情，游戏梗与吐槽拉满，共 101 种。
  - [点击查看详情](./KaLaBiQiu/)
- **千恋万花**：千恋万花系列表情，来自可爱的女主角们，共 25 种。
  - [点击查看详情](./QianLianWanHua/)
- **塔菲**：永雏塔菲系列表情，雏草姬，共 49 种。
  - [点击查看详情](./Taffy/)

## 如何使用

您可以通过以下方式使用本仓库中的表情包：

1. **浏览表情包列表**：在本仓库中查看表情包列表，选择您喜欢的表情。
2. **复制表情链接**：复制您喜欢的表情的链接地址，并在需要的地方粘贴使用。
3. **引导他人使用**：将本仓库链接分享给朋友，让更多人分享表情的乐趣。

您也可以在 twikoo 中直接调用 owo.json 进行使用，本仓库提供两个版本：

- **owo.json（GitHub）**：icon 使用 raw.githubusercontent.com 直链：

```
https://raw.githubusercontent.com/mrmiaomrzh/owo/main/owo.json
```

- **owo-cfbed.json（图床）**：icon 使用 CloudFlare ImgBed 图床（cfbed.lyxzmiao.cc）链接，已上传至 `stickers/` 目录：

```
https://fastly.jsdelivr.net/gh/mrmiaomrzh/owo/owo-cfbed.json
```

## 自动更新

新增表情到对应系列文件夹后，按下面的方式自动上传到图床并重新生成两个 `owo.json`。

### GitHub Action（推荐，全自动）

仓库自带自包含的 `.github/workflows/upload.yml`（逻辑内嵌，不依赖本地脚本）。推送 main 时只要改了表情文件，就会自动：增量上传新增/变更的表情到图床（默认 **Telegram** 存储）→ 重新生成 `owo.json` / `owo-cfbed.json` → 提交回仓库。也可在 Actions 页手动触发。

> `owo-cfbed-cache.json` 是「文件名 → 图床 URL」的增量缓存，**请随仓库一起提交**；它只含公开的图床 URL，不含任何密钥。

首次配置（一次性）：

1. 图床后台获取 API token。
2. 仓库 `Settings → Secrets and variables → Actions` 添加：
   - `CFBED_AUTH_CODE` = 图床 API token（必需）
   - `CFBED_BASE_URL` = 图床地址（必需）

### 本地脚本（可选）

- `python _upload_cfbed.py`：增量上传本地表情到图床 `stickers/<系列>/`（默认 **Telegram** 通道），URL 记录在 `owo-cfbed-cache.json`（只上传新增/变更的图片）。运行时逐条显示 `[i/N] Uploading <文件名> ...` 进度。
  - 可选参数：`--dry-run`（预览不实际上传）、`--subset <系列>`、`--force`（忽略缓存全量重传）、`--auth <码>`、`--base <url>`、`--channel <通道>`。
- `python _gen_owo.py`：从本地文件夹重新生成 `owo.json` 与 `owo-cfbed.json`（UTF-8、CRLF，与 twikoo 兼容）。
- `python _delete_stickers.py`：上传前先**递归删除图床上整个 `stickers/` 文件夹**（`GET /api/manage/delete/stickers?folder=true`），清除仓库中已移除表情的残留图片；默认同时重置 `owo-cfbed-cache.json`，让下次上传从零开始全量重建。可选参数：`--dry-run`（预览不实际删除）、`--folder <路径>`（删除指定目录）、`--keep-cache`（不重置缓存）、`--auth <码>`、`--base <url>`。

## 贡献

如果您有自己制作或发现的精美表情包，并愿意分享给大家，欢迎提交 Pull Request 或者提出 Issue。我们欢迎各种形式的贡献，一起让这个仓库变得更加丰富和有趣！

## 致谢

感谢所有为本仓库贡献过表情包的创作者和贡献者，也感谢所有使用和支持本仓库的用户！

---