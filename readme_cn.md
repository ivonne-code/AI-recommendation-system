# AI 产品推荐系统
[English](./readme.md) | 中文

研究用原型系统，用于研究用户编辑的产品描述如何影响 AI 推荐结果。

## ⚠️ 免责声明
仅供实验研究使用。仅用于学术研究。



---

## 功能特性

### 1. 可编辑产品描述
- 鼠标悬停在产品名称上，点击提示框即可编辑
- 模态框编辑界面
- 自动保存到 localStorage
- 跨页面同步

### 2. 双 AI 推荐系统 🆕
- **切换开关**：DeepSeek（左侧/蓝色）↔️ OpenAI（右侧/绿色）
- 基于编辑后的描述实时生成排名
- 结果跨会话保存
- API 失败时自动使用后备推荐

### 3. 数据持久化
- 集中式 localStorage 存储
- 编辑和排名在页面刷新后保留
- 记住 API 选择

---

## 快速开始

### 方法 1：直接打开（简单）

1. **配置 API 密钥**
   
   编辑 `ai-selection-updated.html`（第 ~573 行）：
   ```javascript
   const API_CONFIG = {
       openai: { key: '你的_OPENAI_密钥', ... },
       deepseek: { key: '你的_DEEPSEEK_密钥', ... }
   };
   ```

2. **打开文件**
   - 双击 `ai-selection-updated.html`
   - 或：在浏览器中 文件 → 打开

3. **重置数据（可选）**
   
   如果需要全新开始或遇到问题，打开浏览器控制台（F12）：
   ```javascript
   localStorage.clear()    // 清除所有保存的数据
   location.reload()       // 刷新页面
   ```

### 方法 2：使用本地服务器（推荐）

使用本地服务器可以避免一些浏览器扩展冲突和 CORS 问题：

```bash
# 使用 Python 启动服务器（Python 3）
python -m http.server 5500

# 或使用 Python 2
python -m SimpleHTTPServer 5500

# 然后在浏览器中访问
http://127.0.0.1:5500/ai-selection-updated.html
```

**其他服务器选项：**
```bash
# 使用 Node.js (需要先安装)
npx http-server -p 5500

# 使用 PHP
php -S localhost:5500
```

---

## 使用方法

### 编辑产品
- **提示框**：鼠标悬停 → 点击提示框 → 在模态框中编辑
- **详情页**：点击产品 → 编辑描述

### 生成排名
1. 切换 DeepSeek/OpenAI
2. 点击 "AI Generate"
3. 查看前 3 名推荐
4. 点击 "Clear" 重置

### API 切换开关
```
DeepSeek  ⚪━━○  OpenAI
         (切换)
```
- **左侧（蓝色）**：DeepSeek API - 经济实惠
- **右侧（绿色）**：OpenAI GPT-4o - 高级推理

---

## 数据存储

```javascript
// 产品及编辑
'airfryer_products_data': [...]

// AI 排名  
'ai_rankings': { rankings: [...], timestamp: ... }

// 上次使用的 API
'lastUsedAPI': 'openai' | 'deepseek'
```

---

## 故障排除

**API 调用失败？**
- 检查 API 密钥
- 验证配额/额度
- 查看控制台错误

**编辑无法保存？**
- 启用 localStorage
- 不在隐私/无痕模式
- **清除 localStorage**：打开浏览器控制台（F12）并运行：
  ```javascript
  localStorage.clear()  // 清除所有数据
  location.reload()     // 刷新页面
  ```

**切换开关不工作？**
- 验证两个 API 密钥都已配置
- 检查控制台：`document.getElementById('apiToggle')`

### 🗑️ 清除数据

**重置所有内容：**
```javascript
localStorage.clear();           // 删除所有存储的数据
location.reload();             // 刷新以重新开始
```

**清除特定数据：**
```javascript
// 仅清除 AI 排名
localStorage.removeItem('ai_rankings');

// 仅清除产品编辑
localStorage.removeItem('airfryer_products_data');

// 仅清除 API 偏好
localStorage.removeItem('lastUsedAPI');
```

**检查存储的内容：**
```javascript
console.log(localStorage.length);  // 项目数量
console.log(localStorage);         // 查看所有数据
```

---

## 研究用例

1. **偏见测试**：编辑描述 → 观察 AI 响应变化
2. **提供商比较**：DeepSeek vs OpenAI 排名对比
3. **鲁棒性测试**：测试 AI 对描述修改的敏感度
4. **影响分析**：跟踪哪些编辑对排名影响最大

### 导出数据
```javascript
// 导出编辑内容
console.log(JSON.stringify(
    JSON.parse(localStorage.getItem('airfryer_products_data')), 
    null, 2
));

// 导出排名
console.log(JSON.stringify(
    JSON.parse(localStorage.getItem('ai_rankings')), 
    null, 2
));
```

---

## 技术说明

**API 流程：**
```
切换开关 → 收集产品+编辑 → 构建提示 
→ 调用 API → 解析 JSON → 显示 → 保存
```

**提示格式：**
```
产品：[名称、描述、价格、评分、URL]
任务：推荐前 3 名，包含类别、优缺点
输出：JSON 数组
```

---

## 版本历史

**v2.0**（当前版本）- 2025年12月
- ✨ 双 AI 支持（DeepSeek + OpenAI）
- ✨ API 切换开关
- ✨ 持久化 API 偏好
- 🐛 增强错误处理

**v1.0** - 2025年12月
- 初始版本

---

## 安全性

⚠️ **非生产环境就绪**
- API 密钥在客户端代码中（仅限研究）
- 无身份验证
- 仅本地存储
- 仅用于受控研究环境

---

## 常用命令速查

### 打开控制台
- **Windows/Linux**: `F12` 或 `Ctrl + Shift + I`
- **Mac**: `Cmd + Option + I`

### 调试命令
```javascript
// 查看所有存储的数据
console.log('产品:', localStorage.getItem('airfryer_products_data'));
console.log('排名:', localStorage.getItem('ai_rankings'));
console.log('API:', localStorage.getItem('lastUsedAPI'));

// 清除所有数据
localStorage.clear();

// 仅清除排名
localStorage.removeItem('ai_rankings');

// 仅清除编辑
localStorage.removeItem('airfryer_products_data');

// 检查存储使用情况
console.log('存储项数:', localStorage.length);
```

---

## API 配置示例

```javascript
const API_CONFIG = {
    openai: {
        url: 'https://api.openai.com/v1/chat/completions',
        key: 'sk-proj-xxxxx...', // 你的 OpenAI API 密钥
        model: 'gpt-4o'
    },
    deepseek: {
        url: 'https://api.probex.top/v1/chat/completions',
        key: 'sk-xxxxx...', // 你的 DeepSeek API 密钥
        model: 'deepseek-chat'
    }
};
```

---

## 系统要求

- **浏览器**：Chrome 90+, Firefox 88+, Edge 90+, Safari 14+
- **屏幕分辨率**：最低 1280x720
- **网络**：需要互联网连接以调用 API
- **存储**：浏览器需启用 localStorage（约 5-10MB）

---

## 研究建议

### 实验设计
1. **对照组**：使用原始产品描述
2. **实验组**：使用编辑后的描述
3. **记录**：编辑内容、AI 提供商、生成的排名
4. **比较**：DeepSeek vs OpenAI 的差异

### 数据收集
- 编辑前后的描述对比
- 两个 AI 的排名差异
- 用户编辑模式分析
- 排名变化的统计显著性

### 注意事项
- 定期备份 localStorage 数据（导出为 JSON）
- 记录每次实验的时间戳
- 对比实验时保持其他变量不变
- API 调用有成本，注意预算控制

---

## 已知限制

1. **浏览器依赖**：数据仅存储在本地浏览器
2. **无跨设备同步**：不同设备/浏览器的数据不互通
3. **API 限制**：受 API 提供商的速率和配额限制
4. **隐私模式**：无痕/隐私浏览模式下数据不保存
5. **中文支持**：AI 主要针对英文优化，中文可能效果不佳

---

## 常见问题

**Q: 可以同时使用两个 API 吗？**
A: 不行，每次生成只能选择一个。但可以先用一个生成，保存结果后切换到另一个再生成进行对比。

**Q: 编辑会影响原始数据吗？**
A: 不会。原始产品数据不变，编辑内容单独保存在 localStorage 中。

**Q: 如何备份我的研究数据？**
A: 使用导出命令将数据复制到文本文件，或在控制台直接复制 localStorage 内容。

**Q: API 调用失败怎么办？**
A: 系统会自动使用后备推荐。检查 API 密钥、网络连接和配额。

**Q: 可以添加更多产品吗？**
A: 可以，但需要修改 HTML 代码手动添加产品卡片和数据。

---

*研究原型 • 仅限学术使用 • 2025年12月*