# TAPD MCP Server

基于MCP Python SDK开发的TAPD服务器，实现TAPD平台的需求管理功能集成。

## 功能特点

- 需求查询与管理
  - 支持多条件查询（ID、标题、状态等）
  - 分页展示
  - 完整的需求详情获取

## 技术栈

- FastAPI
- Python 3.8+
- MCP Python SDK

## 安装

1. 克隆仓库：
```bash
git clone [repository-url]
cd tapd-mcp-server
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 配置环境变量：
创建`.env`文件并设置以下变量：
```
TAPD_API_USER=your_api_user
TAPD_API_PASSWORD=your_api_password
```

## 运行

```bash
uvicorn app.main:app --reload
```

## API文档

启动服务后访问：`http://localhost:8000/docs`

## 开发规范

- 遵循PEP 8编码规范
- 完整的异常处理
- 详细的日志记录

## 测试

```bash
pytest
```

## 安全说明

- 接口认证
- 敏感信息加密
- 并发请求处理