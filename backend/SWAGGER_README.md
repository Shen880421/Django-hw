# Django Swagger API 文檔

這個專案已成功整合 Swagger/OpenAPI 文檔服務，提供完整的 API 文檔和測試界面。

## 🚀 快速開始

### 1. 安裝依賴套件
```bash
pip install -r requirements.txt
```

### 2. 啟動開發伺服器
```bash
python manage.py runserver
```

### 3. 訪問 API 文檔

- **Swagger UI**: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
- **Redoc**: [http://127.0.0.1:8000/api/redoc/](http://127.0.0.1:8000/api/redoc/)
- **OpenAPI Schema**: [http://127.0.0.1:8000/api/schema/](http://127.0.0.1:8000/api/schema/)

## 📋 API 端點

### 用戶相關 API
- `GET /api/users/` - 取得所有用戶
- `POST /api/users/` - 建立新用戶
- `GET /api/users/{id}/` - 取得特定用戶
- `PUT /api/users/{id}/` - 更新用戶資訊
- `DELETE /api/users/{id}/` - 刪除用戶
- `POST /api/users/register/` - 用戶註冊

### 課程相關 API
- `GET /api/courses/` - 取得所有課程
- `POST /api/courses/` - 建立新課程
- `GET /api/courses/{id}/` - 取得特定課程
- `PUT /api/courses/{id}/` - 更新課程資訊
- `DELETE /api/courses/{id}/` - 刪除課程

### 預約相關 API
- `GET /api/bookings/` - 取得所有預約
- `POST /api/bookings/` - 建立新預約
- `GET /api/bookings/{id}/` - 取得特定預約
- `PUT /api/bookings/{id}/` - 更新預約資訊
- `DELETE /api/bookings/{id}/` - 刪除預約

### 評價相關 API
- `GET /api/reviews/` - 取得所有評價
- `POST /api/reviews/` - 建立新評價
- `GET /api/reviews/{id}/` - 取得特定評價
- `PUT /api/reviews/{id}/` - 更新評價資訊
- `DELETE /api/reviews/{id}/` - 刪除評價

## 🔧 Swagger 設定

### 主要設定檔：`settings.py`

```python
# 在 INSTALLED_APPS 中加入
INSTALLED_APPS = [
    # ... 其他應用
    'drf_spectacular',
]

# REST Framework 設定
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# drf-spectacular 設定
SPECTACULAR_SETTINGS = {
    'TITLE': 'Django 家教媒合平台 API',
    'DESCRIPTION': '家教媒合平台的 REST API 文檔',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SCHEMA_PATH_PREFIX': '/api/',
    'COMPONENT_SPLIT_REQUEST': True,
    'SORT_OPERATIONS': False,
}
```

### URL 配置：`urls.py`

```python
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

urlpatterns = [
    # ... 其他 URL
    # Swagger 文檔相關路由
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
```

## 📖 如何使用 Swagger UI

1. **瀏覽 API**：在 Swagger UI 中可以看到所有可用的 API 端點
2. **測試 API**：點擊任何端點可以直接在瀏覽器中測試
3. **查看文檔**：每個端點都有詳細的參數說明和回應格式
4. **下載 Schema**：可以下載 OpenAPI 規格文件用於程式碼生成

## 📊 API 文檔特色

- ✅ **完整的 API 文檔**：自動生成完整的 API 文檔
- ✅ **互動式測試**：直接在瀏覽器中測試 API
- ✅ **參數驗證**：顯示所有必填和可選參數
- ✅ **錯誤回應**：展示可能的錯誤回應格式
- ✅ **多種格式**：支援 Swagger UI 和 Redoc 兩種風格
- ✅ **中文支援**：API 說明和錯誤訊息支援中文

## 🛠️ 自訂 API 文檔

### 為 ViewSet 添加文檔註解

```python
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(
        summary="取得所有用戶",
        description="取得系統中所有用戶的列表",
        tags=["Users"]
    ),
    create=extend_schema(
        summary="建立新用戶",
        description="建立一個新的用戶帳戶",
        tags=["Users"]
    ),
)
class UsersViewSet(viewsets.ModelViewSet):
    # ... ViewSet 實作
```

### 為自訂 Action 添加文檔

```python
@extend_schema(
    summary="用戶註冊",
    description="註冊新用戶，支援密碼確認驗證",
    tags=["Users"],
    request={
        'application/json': {
            'type': 'object',
            'properties': {
                'username': {'type': 'string'},
                'email': {'type': 'string'},
                'password': {'type': 'string'},
                'password2': {'type': 'string'},
                'role': {'type': 'string'},
            },
            'required': ['username', 'email', 'password', 'password2', 'role']
        }
    }
)
@action(detail=False, methods=["post"])
def register(self, request):
    # ... 實作
```

## 🔍 測試 Swagger 服務

執行測試腳本來驗證 Swagger 服務是否正常運作：

```bash
python test_swagger.py
```

## 📝 備註

- 確保 Django 開發伺服器正在運行
- 所有 API 端點都會自動出現在 Swagger 文檔中
- 可以根據需要自訂 API 文檔的外觀和內容
- 支援匯出 OpenAPI 規格文件用於前端程式碼生成

## 🤝 貢獻

如果您想要改進 API 文檔或添加新功能，請：

1. Fork 此專案
2. 創建功能分支
3. 提交您的修改
4. 建立 Pull Request

---

*此文檔由 Django Swagger 整合自動生成*
