@echo off
chcp 65001 >nul
title 梅花易数占卜系统

echo.
echo ═══════════════════════════════════════
echo     🌸 梅花易数占卜系统启动器
echo ═══════════════════════════════════════
echo.

:: 检查Python是否可用
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误: 未找到Python
    echo 请安装Python 3.7+
    pause
    exit /b 1
)

echo ✅ Python环境检测通过

:: 切换到脚本所在目录
cd /d "%~dp0"

echo 📦 检查依赖包...
python -c "import fastapi, uvicorn; print('✅ 依赖包检查通过')" 2>nul
if errorlevel 1 (
    echo ⚠️  正在安装依赖包...
    pip install fastapi uvicorn pydantic python-multipart
    if errorlevel 1 (
        echo ❌ 依赖安装失败
        pause
        exit /b 1
    )
)

echo.
echo 🚀 启动服务器...
echo 📍 访问地址: http://localhost:4949
echo 📚 API文档: http://localhost:4949/docs
echo ⏹️  按 Ctrl+C 停止服务
echo.

:: 启动应用
python app.py

pause