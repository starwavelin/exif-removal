#!/usr/bin/env python3
import sys
import subprocess
from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".heic", ".gif", ".tiff", ".tif", ".webp",
    ".mp4", ".mov", ".avi", ".mkv",
}


def check_exiftool():
    result = subprocess.run(["which", "exiftool"], capture_output=True)
    if result.returncode != 0:
        print("错误：未找到 exiftool，请先安装：brew install exiftool")
        sys.exit(1)


def get_folder():
    if len(sys.argv) > 1:
        return Path(sys.argv[1])
    path = input("请输入图片/视频文件夹路径：").strip()
    return Path(path)


def scan_files(folder: Path) -> list[Path]:
    return [
        f for f in folder.iterdir()
        if f.is_file() and f.suffix.lower() in SUPPORTED_EXTENSIONS
    ]


def main():
    check_exiftool()

    folder = get_folder()
    if not folder.exists() or not folder.is_dir():
        print(f"错误：路径不存在或不是文件夹：{folder}")
        sys.exit(1)

    files = scan_files(folder)
    if not files:
        print("未找到支持的图片或视频文件。")
        sys.exit(0)

    print(f"\n找到 {len(files)} 个文件：")
    for f in sorted(files):
        print(f"  {f.name}")

    confirm = input(f"\n即将删除以上 {len(files)} 个文件的 EXIF 信息（不可撤销）。继续？[y/N] ").strip().lower()
    if confirm != "y":
        print("已取消。")
        sys.exit(0)

    result = subprocess.run(
        ["exiftool", "-all=", "-overwrite_original"] + [str(f) for f in files]
    )

    if result.returncode == 0:
        print(f"\n完成：已处理 {len(files)} 个文件，EXIF 信息已全部清除。")
    else:
        print("\n警告：部分文件处理失败，请检查上方 exiftool 输出。")
        sys.exit(1)


if __name__ == "__main__":
    main()
