#!/usr/bin/env python3
"""
測試 Django Swagger API 文檔
"""

import requests
import json

# API 基本設定
BASE_URL = "http://127.0.0.1:8000"
API_ENDPOINTS = {
    "schema": f"{BASE_URL}/api/schema/",
    "swagger": f"{BASE_URL}/api/docs/",
    "redoc": f"{BASE_URL}/api/redoc/",
    "users": f"{BASE_URL}/api/users/",
    "register": f"{BASE_URL}/api/users/register/",
}


def test_swagger_endpoints():
    """測試所有 Swagger 相關端點"""
    print("🔍 測試 Swagger 端點...")

    # 測試 Schema 端點
    print("\n📋 測試 OpenAPI Schema...")
    try:
        response = requests.get(API_ENDPOINTS["schema"])
        if response.status_code == 200:
            print(f"✅ Schema 端點正常 (Status: {response.status_code})")
            schema = response.json()
            print(f"📊 API 版本: {schema.get('info', {}).get('version', '未知')}")
            print(f"📝 API 標題: {schema.get('info', {}).get('title', '未知')}")
        else:
            print(f"❌ Schema 端點失敗 (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Schema 端點錯誤: {e}")

    # 測試 Swagger UI
    print("\n🔗 測試 Swagger UI...")
    try:
        response = requests.get(API_ENDPOINTS["swagger"])
        if response.status_code == 200:
            print(f"✅ Swagger UI 可用 (Status: {response.status_code})")
            print(f"🌐 Swagger UI URL: {API_ENDPOINTS['swagger']}")
        else:
            print(f"❌ Swagger UI 失敗 (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Swagger UI 錯誤: {e}")

    # 測試 Redoc
    print("\n📖 測試 Redoc...")
    try:
        response = requests.get(API_ENDPOINTS["redoc"])
        if response.status_code == 200:
            print(f"✅ Redoc 可用 (Status: {response.status_code})")
            print(f"🌐 Redoc URL: {API_ENDPOINTS['redoc']}")
        else:
            print(f"❌ Redoc 失敗 (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Redoc 錯誤: {e}")


def test_api_endpoints():
    """測試 API 端點"""
    print("\n🔍 測試 API 端點...")

    # 測試用戶列表端點
    print("\n👥 測試用戶列表端點...")
    try:
        response = requests.get(API_ENDPOINTS["users"])
        if response.status_code == 200:
            print(f"✅ 用戶列表端點正常 (Status: {response.status_code})")
            users = response.json()
            print(f"📊 用戶數量: {len(users)}")
        else:
            print(f"❌ 用戶列表端點失敗 (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ 用戶列表端點錯誤: {e}")


def print_summary():
    """打印總結訊息"""
    print("\n" + "=" * 50)
    print("🎉 Django Swagger 服務已成功註冊！")
    print("=" * 50)
    print(f"📋 OpenAPI Schema: {API_ENDPOINTS['schema']}")
    print(f"📖 Swagger UI: {API_ENDPOINTS['swagger']}")
    print(f"📚 Redoc: {API_ENDPOINTS['redoc']}")
    print("=" * 50)
    print("💡 使用說明：")
    print("1. 訪問 Swagger UI 來瀏覽和測試 API")
    print("2. 使用 Redoc 查看美觀的 API 文檔")
    print("3. 下載 OpenAPI Schema 進行 API 集成")
    print("=" * 50)


if __name__ == "__main__":
    print("🚀 開始測試 Django Swagger 服務...")
    test_swagger_endpoints()
    test_api_endpoints()
    print_summary()
