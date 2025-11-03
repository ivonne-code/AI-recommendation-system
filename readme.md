# AI Recommendation System

An intelligent recommendation system prototype based on editable product descriptions, designed to study how user-customized content affects AI recommendation outcomes.

English | [中文](./readme_cn.md)

## Overview

This project implements an interactive product recommendation system that allows users to:
1. Edit product descriptions (on both main page and detail pages)
2. Generate AI recommendations based on modified descriptions
3. Observe how description changes impact recommendation results

**Research Value**: Explores how user participation in content editing influences the output quality and personalization level of recommendation systems.

## Quick Start

```bash
# Start local server
python -m http.server 5500

# Open in browser
http://127.0.0.1:5500/ai-selector-page.html
```

## Core Features

### 1. Editable Descriptions
- **Main Page**: Click product tooltip to edit
- **Detail Pages**: Click "About this item" or "Product Description" sections to edit
- All modifications synchronized across pages via centralized localStorage

### 2. AI Recommendation Generation
- Click "AI Generate" button to invoke DeepSeek API
- Generates Top 3 recommendations based on current product descriptions
- Output includes: category, product name, description, pros/cons

### 3. Data Persistence
- Centralized storage: `localStorage['airfryer_products_data']`
- Data structure:
```javascript
[{
  "id": "product-id",
  "description": "full description",
  "lastModified": "timestamp"
}]
```

## Technical Architecture

```
Frontend: HTML5 + CSS3 + Vanilla JavaScript
Storage: Browser localStorage (centralized)
AI: DeepSeek API (deepseek-chat model)
Design: Amazon-inspired UI
```

## Project Structure

```
├── google-homepage.html            # Google search page
├── ai-selector-page.html           # Main page (product list + AI recommendations)
└── products/                       # 10 product detail pages
    ├── product-chefman-6qt.html
    ├── product-chefman-multi.html
    └── ...
```

## Key Implementation

### Edit Synchronization Mechanism
```javascript
// Save to centralized storage
function updateCentralizedStorage(productId, newDescription) {
    const data = JSON.parse(localStorage.getItem('airfryer_products_data'));
    const product = data.find(p => p.id === productId);
    product.description = newDescription;
    localStorage.setItem('airfryer_products_data', JSON.stringify(data));
}
```

### AI API Call
```javascript
// Collect all product descriptions → Send to DeepSeek → Parse returned rankings
const rankings = await callDeepSeekAPI(products);
displayRankings(rankings);
```

## Configuration

### API Settings
Modify in `ai-selector-page.html`:
```javascript
const DEEPSEEK_API_KEY = "your-api-key";
const API_URL = "https://api.probex.top/v1/chat/completions";
```

## Experimental Setup Recommendations

### Controlled Experiment
1. **Baseline Group**: Generate recommendations using original product descriptions
2. **Experimental Group**: Generate recommendations after editing descriptions
3. **Metrics to Observe**: Changes in recommendation results, ranking differences

### Data Collection
```javascript
// Export experimental data
const data = localStorage.getItem('airfryer_products_data');
console.log(JSON.parse(data));
```

## Limitations

- localStorage capacity limit (~5MB)
- API calls require network connection
- Only supports text editing, not image modification
- Recommendation results limited by API model constraints

## Troubleshooting

### AI Generate Not Working
```javascript
// Open Console (F12) to check errors
// Common issues: API key, CORS, network connection
```

### Data Not Syncing
```javascript
// Clear and reset
localStorage.removeItem('airfryer_products_data');
location.reload();
```

---

**Version**: 1.0.0 | **Status**: Ready for Research