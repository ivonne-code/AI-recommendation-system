# AI Recommendation System
English | [中文](./readme_cn.md)

Research prototype for studying how user-edited product descriptions affect AI recommendation outcomes.

## ⚠️ Disclaimer
Experimental research prototype only. Not affiliated with Amazon. For academic use.

---

## Features

### 1. Editable Product Descriptions
- Hover over product names, click tooltip to edit
- Modal editing interface
- Auto-saved to localStorage
- Syncs across pages

### 2. Dual AI Recommendation System 🆕
- **Toggle Switch**: DeepSeek (left/blue) ↔️ OpenAI (right/green)
- Real-time ranking generation based on edited descriptions
- Results persist across sessions
- Automatic fallback on API failure

### 3. Data Persistence
- Centralized localStorage storage
- Edits and rankings survive page refresh
- API selection remembered

---

## Quick Start

### Method 1: Direct Open (Simple)

1. **Configure API Keys**
   
   Edit `ai-selection-updated.html` (line ~573):
   ```javascript
   const API_CONFIG = {
       openai: { key: 'YOUR_OPENAI_KEY', ... },
       deepseek: { key: 'YOUR_DEEPSEEK_KEY', ... }
   };
   ```

2. **Open File**
   - Double-click `ai-selection-updated.html`
   - Or: File → Open in browser

3. **Reset Data (Optional)**
   
   If starting fresh or encountering issues, open browser console (F12):
   ```javascript
   localStorage.clear()    // Clear all saved data
   location.reload()       // Refresh page
   ```

### Method 2: Local Server (Recommended)

Using a local server avoids browser extension conflicts and CORS issues:

```bash
# Start server with Python 3
python -m http.server 5500

# Or Python 2
python -m SimpleHTTPServer 5500

# Then open in browser
http://127.0.0.1:5500/ai-selection-updated.html
```

**Other server options:**
```bash
# Node.js (requires installation)
npx http-server -p 5500

# PHP
php -S localhost:5500
```

---

## Usage

### Edit Products
- **Tooltip**: Hover → click tooltip → edit in modal
- **Detail page**: Click product → Edit Description

### Generate Rankings
1. Toggle DeepSeek/OpenAI
2. Click "AI Generate"
3. View top 3 recommendations
4. Click "Clear" to reset

### API Toggle
```
DeepSeek  ⚪━━○  OpenAI
         (toggle)
```
- **Left (Blue)**: DeepSeek API - cost-effective
- **Right (Green)**: OpenAI GPT-4o - advanced reasoning

---

## Data Storage

```javascript
// Products with edits
'airfryer_products_data': [...]

// AI rankings  
'ai_rankings': { rankings: [...], timestamp: ... }

// Last used API
'lastUsedAPI': 'openai' | 'deepseek'
```

---

## Troubleshooting

**API fails?**
- Check API keys
- Verify quota/credits
- Check console for errors

**Edits not saving?**
- Enable localStorage
- Not in private/incognito mode
- **Clear localStorage**: Open browser console (F12) and run:
  ```javascript
  localStorage.clear()  // Clear everything
  location.reload()     // Refresh page
  ```

**Toggle not working?**
- Verify both API keys configured
- Check console: `document.getElementById('apiToggle')`

### 🗑️ Clearing Data

**To reset everything:**
```javascript
localStorage.clear();           // Remove all stored data
location.reload();             // Refresh to start fresh
```

**To clear specific data:**
```javascript
// Clear only AI rankings
localStorage.removeItem('ai_rankings');

// Clear only product edits
localStorage.removeItem('airfryer_products_data');

// Clear only API preference
localStorage.removeItem('lastUsedAPI');
```

**Check what's stored:**
```javascript
console.log(localStorage.length);  // Number of items
console.log(localStorage);         // View all data
```

---

## Research Use Cases

1. **Bias Testing**: Edit descriptions → observe AI response changes
2. **Provider Comparison**: DeepSeek vs OpenAI rankings
3. **Robustness**: Test AI sensitivity to description modifications
4. **Impact Analysis**: Track which edits affect rankings most

### Export Data
```javascript
// Export edits
console.log(JSON.stringify(
    JSON.parse(localStorage.getItem('airfryer_products_data')), 
    null, 2
));

// Export rankings
console.log(JSON.stringify(
    JSON.parse(localStorage.getItem('ai_rankings')), 
    null, 2
));
```

---

## Technical Notes

**API Flow:**
```
Toggle → Collect products+edits → Build prompt 
→ Call API → Parse JSON → Display → Save
```

**Prompt Format:**
```
Products: [name, description, price, rating, URL]
Task: Recommend top 3 with category, pros, cons
Output: JSON array
```

---

## Version History

**v2.0** (Current) - Dec 2025
- ✨ Dual AI support (DeepSeek + OpenAI)
- ✨ API toggle switch
- ✨ Persistent API preference
- 🐛 Enhanced error handling

**v1.0** - Dec 2025
- Initial release

---

## Security

⚠️ **Not production-ready**
- API keys in client-side code (research only)
- No authentication
- Local storage only
- For controlled research environments

---

*Research prototype • Academic use only • December 2025*