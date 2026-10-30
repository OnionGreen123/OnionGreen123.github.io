# Shaoyang Zhang · Research & Notes

个人网站完整源码与可直接部署的静态文件。

正式地址：https://oniongreen123.github.io/
仓库：https://github.com/OnionGreen123/OnionGreen123.github.io

## 本包包含的最新改动

- 已删除网站 CV 的 Technical Skills 和 About 页的工具技能板块。
- Miku 隐藏页面 `/39/` 的地图本体纵向高度从 340 增至 600，画布增至 1280，上海演出卡片下移。
- `assets/Shaoyang_Zhang_CV.pdf` 已删除 Technical Skills，并包含可点击的网站链接。这是隐去未发表研究方法细节的公开版。
- 地图加高和 PDF 替换尚未上传线上；本压缩包包含这两项最新修改。

## 最快更新 GitHub 网站

1. 解压 ZIP，进入 `shaoyang-personal-site` 文件夹。
2. 打开上述 GitHub 仓库，选择 **Add file → Upload files**。
3. 把文件夹里面的文件和子文件夹拖入上传区，保持原有相对路径；不要上传 ZIP 本身，也不要把外层 `shaoyang-personal-site` 文件夹作为一层目录上传。
4. 提交到 `main`。现有 GitHub Actions 会检查并发布，等待 Actions 显示成功。

现有仓库已经有 `.github/workflows/pages.yml`，无需更改部署设置。若系统隐藏了以点开头的文件，也不影响更新已有仓库；请保留仓库现有工作流和 `.nojekyll`。

## 本地预览

安装 Python 3，在本文件所在目录运行：

```sh
python -m http.server 8000
```

打开 http://localhost:8000/ 。隐藏页为 http://localhost:8000/39/ 。
请通过本地 HTTP 服务预览，不要直接双击 HTML 文件，因为站内资源使用根路径。

## 修改与重新生成

- `content/site.json`：站点信息、研究与出版物。
- `content/notes/`：笔记 Markdown；`content/note-dates.json`：历史日期信息。
- `scripts/build.py`：普通页面模板与 HTML 生成。
- `scripts/miku_page.py`：演出记录、地图坐标和隐藏页面。
- `assets/style.css`：主站样式；`assets/miku.css`：隐藏页面样式。
- `scripts/make_cv.py`：公开 PDF 简历生成器。

```sh
python scripts/build.py
python scripts/check.py
```

重新生成 PDF 时先安装依赖：

```sh
python -m pip install reportlab
python scripts/make_cv.py
```

可选安装 PyMuPDF，以启用检查脚本中的 PDF 检查：`python -m pip install pymupdf`。

提交重新生成后的 HTML 和 PDF。部署工作流发布已生成文件，不会自动执行页面/PDF 生成器。

## 文件范围

本包包含完整页面、图片、字体配置、地图数据、公开 CV、内容源文件、Python 生成脚本和当前 GitHub Pages 工作流。
不包含私人研究门户凭据、未公开论文、Git 登录信息或浏览器会话。
