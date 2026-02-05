# WebUI自动化框架3.0-基于POM设计模式

## 介绍
该仓库提供一个基于 POM + unittest 的 UI 自动化测试框架骨架，包含：
- Selenium 操作封装（`base_page`）
- 页面对象（`page_object`）
- 测试用例（`test_cases`）
- 测试数据（`test_data`）
- 日志模块（`utils/logger.py`）
- 报告生成模块（`utils/report.py`）

## 目录结构
```
UIFrameworkMK3/
├── base_page/
│   └── base_page.py
├── page_object/
│   └── login_page.py
├── test_cases/
│   └── test_login.py
├── test_data/
│   └── config.py
├── utils/
│   ├── logger.py
│   └── report.py
└── main.py
```

## 使用方式
1. 安装依赖
```bash
pip install selenium
```
2. 配置浏览器驱动（例如 ChromeDriver）并保证可执行文件在 PATH 中。
3. 运行测试（默认示例用例被 `RUN_UI_TESTS` 环境变量保护）：
```bash
RUN_UI_TESTS=1 python main.py
```

## 待改进
- 接入 CI、并行执行、失败截图等高级特性。
