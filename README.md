# exif-removal

一个轻量的 Python 命令行工具，用于批量清除图片和视频文件中的 EXIF 元数据（拍摄地点、设备信息、时间戳等），保护个人隐私。

## 功能

- 扫描指定文件夹（仅顶层，不递归子文件夹）中的图片和视频文件
- 执行前列出所有将被处理的文件，并要求用户确认
- 使用 `exiftool` 原地清除 EXIF 信息，不保留备份文件
- 无需安装额外 Python 依赖，仅需系统中已有 `exiftool`

## 支持格式

| 类型 | 格式 |
|------|------|
| 图片 | `.jpg` `.jpeg` `.png` `.heic` `.gif` `.tiff` `.tif` `.webp` |
| 视频 | `.mp4` `.mov` `.avi` `.mkv` |

## 前置依赖

需要安装 [ExifTool](https://exiftool.org/)：

```bash
brew install exiftool
```

## 使用方法

**方式一：直接传入文件夹路径**

```bash
python3 remove_exif.py /path/to/your/folder
```

**方式二：交互式输入**

```bash
python3 remove_exif.py
```

运行后程序会提示你输入文件夹路径。

## 示例

```
$ python3 remove_exif.py ~/Desktop/photos

找到 3 个文件：
  IMG_001.jpg
  IMG_002.heic
  video.mp4

即将删除以上 3 个文件的 EXIF 信息（不可撤销）。继续？[y/N] y

完成：已处理 3 个文件，EXIF 信息已全部清除。
```

## 注意事项

- **操作不可撤销**：清除后无法恢复原始 EXIF 数据，建议提前备份重要文件。
- 仅处理文件夹顶层文件，子文件夹内的文件不会被处理。
