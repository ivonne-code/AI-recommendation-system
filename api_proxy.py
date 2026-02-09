#!/usr/bin/env python3
"""
API Proxy Server - 解决 CORS 跨域问题
运行：python api_proxy.py
前端请求：http://127.0.0.1:5000/openai 或 /deepseek
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import sys

app = Flask(__name__)
CORS(app)  # 允许所有跨域请求

OPENAI_URL = "https://api.openai.com/v1/chat/completions"
DEEPSEEK_URL = "https://api.probex.top/v1/chat/completions"

@app.route('/openai', methods=['POST'])
def proxy_openai():
    try:
        data = request.get_json(silent=True) or {}
        api_key = request.headers.get('Authorization', '').replace('Bearer ', '').strip()

        if not api_key:
            return jsonify({'error': 'Missing API key'}), 401

        print("📤 Proxying OpenAI request...")
        print(f"   Model: {data.get('model', 'unknown')}")
        print(f"   API Key: {api_key[:12]}...{api_key[-4:]}")

        response = requests.post(
            OPENAI_URL,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {api_key}'
            },
            json=data,
            timeout=60
        )

        print(f"📥 OpenAI response: {response.status_code}")

        # 直接透传返回（保持 OpenAI 的错误信息）
        return (response.text, response.status_code, {'Content-Type': 'application/json'})

    except Exception as e:
        print(f"❌ Proxy error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/deepseek', methods=['POST'])
def proxy_deepseek():
    try:
        data = request.get_json(silent=True) or {}
        api_key = request.headers.get('Authorization', '').replace('Bearer ', '').strip()

        if not api_key:
            return jsonify({'error': 'Missing API key'}), 401

        print("📤 Proxying DeepSeek request...")

        response = requests.post(
            DEEPSEEK_URL,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {api_key}'
            },
            json=data,
            timeout=60
        )

        print(f"📥 DeepSeek response: {response.status_code}")
        return (response.text, response.status_code, {'Content-Type': 'application/json'})

    except Exception as e:
        print(f"❌ Proxy error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'message': 'Proxy server is running'}), 200

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 API Proxy Server Starting...")
    print("=" * 60)
    print("📍 Proxy URLs:")
    print("   OpenAI:   http://127.0.0.1:5000/openai")
    print("   DeepSeek: http://127.0.0.1:5000/deepseek")
    print("   Health:   http://127.0.0.1:5000/health")
    print("=" * 60)

    try:
        app.run(host='127.0.0.1', port=5000, debug=True)
    except KeyboardInterrupt:
        print("\n👋 Server stopped")
        sys.exit(0)
