# AI 推荐系统

基于可编辑产品描述的智能推荐系统原型，用于研究用户自定义内容对 AI 推荐结果的影响。

[English](./README.md) | 中文

## 概述

本项目实现了一个交互式产品推荐系统，允许用户：
1. 编辑产品描述（主页和详情页均可）
2. 基于修改后的描述生成 AI 推荐
3. 观察描述变化对推荐结果的影响

**研究价值**：探索用户参与内容编辑如何影响推荐系统的输出质量和个性化程度。

## 快速开始

```bash
# 启动本地服务器
python -m http.server 5500

# 打开浏览器
http://127.0.0.1:5500/ai-selector-page.html
```

## 核心功能

### 1. 可编辑描述
- **主页**：点击产品 tooltip 编辑
- **详情页**：点击"关于此商品"或"产品描述"区域编辑
- 所有修改通过 localStorage 集中存储，跨页面同步

### 2. AI 推荐生成
- 点击"AI Generate"按钮调用 DeepSeek API
- 基于当前所有产品描述生成 Top 3 推荐
- 输出包含：分类、产品名、描述、优缺点

### 3. 数据持久化
- 集中式存储：`localStorage['airfryer_products_data']`
- 数据结构：
```javascript
[{
  "id": "product-id",
  "description": "完整描述",
  "lastModified": "timestamp"
}]
```

## 技术架构

```
前端: HTML5 + CSS3 + Vanilla JavaScript
存储: Browser localStorage (集中式)
AI: DeepSeek API (deepseek-chat model)
设计: Amazon-inspired UI
```

## 项目结构

```
├── google-homepage.html         #google页面
├── ai-selector-page.html          # 主页（产品列表 + AI 推荐）
└── products/                       # 10个产品详情页
    ├── product-chefman-6qt.html
    ├── product-chefman-multi.html
    └── ...
```

## 关键实现

### 编辑同步机制
```javascript
// 保存到集中存储
function updateCentralizedStorage(productId, newDescription) {
    const data = JSON.parse(localStorage.getItem('airfryer_products_data'));
    const product = data.find(p => p.id === productId);
    product.description = newDescription;
    localStorage.setItem('airfryer_products_data', JSON.stringify(data));
}
```

### AI API 调用
```javascript
// 收集所有产品描述 → 发送到 DeepSeek → 解析返回的排名
const rankings = await callDeepSeekAPI(products);
displayRankings(rankings);
```

## 配置

### API 设置
在 `ai-selector-page.html` 中修改：
```javascript
const DEEPSEEK_API_KEY = "your-api-key";
const API_URL = "https://api.probex.top/v1/chat/completions";
```

## 实验设置建议

### 对照实验
1. **基线组**：使用原始产品描述生成推荐
2. **实验组**：编辑描述后生成推荐
3. **观察指标**：推荐结果的变化、排名差异

### 数据收集
```javascript
// 导出实验数据
const data = localStorage.getItem('airfryer_products_data');
console.log(JSON.parse(data));
```

## 局限性

- localStorage 容量限制（~5MB）
- API 调用需要网络连接
- 仅支持文本编辑，不支持图片修改
- 推荐结果受 API 模型限制

## 故障排除

### AI Generate 不工作
```javascript
// 打开 Console (F12) 检查错误
// 常见问题：API key、CORS、网络连接
```

### 数据未同步
```javascript
// 清除并重置
localStorage.removeItem('airfryer_products_data');
location.reload();
```


---

**版本**: 1.0.0 | **状态**: Ready for Research