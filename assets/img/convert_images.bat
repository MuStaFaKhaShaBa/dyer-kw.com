@echo off
setlocal enabledelayedexpansion

:: Create output folder
mkdir webp 2>nul

:: Loop through all image files (JPG, PNG, BMP, TIFF)
for %%i in (*.jpg *.jpeg *.png *.bmp *.tiff) do (
    echo Converting %%i to WebP...
    magick "%%i" -quality 80 "webp/%%~ni.webp"
    echo Done!
)

echo All images converted to WebP!
pause
