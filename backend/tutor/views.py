from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, extend_schema_view
from tutor.models import Users, Courses, Bookings, Reviews
from tutor.serializers import (
    UsersSerializer,
    CoursesSerializer,
    BookingsSerializer,
    ReviewsSerializer,
)

# 取得自訂 User model
User = get_user_model()


@extend_schema_view(
    list=extend_schema(
        summary="取得所有用戶", description="取得系統中所有用戶的列表", tags=["Users"]
    ),
    create=extend_schema(
        summary="建立新用戶", description="建立一個新的用戶帳戶", tags=["Users"]
    ),
    retrieve=extend_schema(
        summary="取得單一用戶",
        description="根據 ID 取得特定用戶的詳細資訊",
        tags=["Users"],
    ),
    update=extend_schema(
        summary="更新用戶資訊", description="更新特定用戶的完整資訊", tags=["Users"]
    ),
    partial_update=extend_schema(
        summary="部分更新用戶資訊", description="部分更新特定用戶的資訊", tags=["Users"]
    ),
    destroy=extend_schema(
        summary="刪除用戶", description="刪除特定用戶", tags=["Users"]
    ),
)
@method_decorator(csrf_exempt, name="dispatch")
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def get_permissions(self):
        """
        註冊功能允許匿名訪問
        """
        if self.action == "register":
            permission_classes = [AllowAny]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]

    @extend_schema(
        summary="用戶註冊",
        description="註冊新用戶，支援密碼確認驗證",
        tags=["Users"],
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "username": {"type": "string", "description": "用戶名"},
                    "email": {
                        "type": "string",
                        "format": "email",
                        "description": "電子郵件",
                    },
                    "password": {
                        "type": "string",
                        "minLength": 6,
                        "description": "密碼",
                    },
                    "password2": {
                        "type": "string",
                        "minLength": 6,
                        "description": "確認密碼",
                    },
                    "role": {
                        "type": "string",
                        "enum": ["teacher", "student", "both"],
                        "description": "用戶角色",
                    },
                    "first_name": {"type": "string", "description": "名字"},
                    "last_name": {"type": "string", "description": "姓氏"},
                },
                "required": ["username", "email", "password", "password2", "role"],
            }
        },
    )
    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def register(self, request):
        """
        用戶註冊 API - 使用 Django auth 模組，支援 password2 驗證
        POST /api/users/register/
        """
        # 取得表單資料
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        password2 = request.data.get("password2")  # 前端傳入的 password2
        role = request.data.get("role")
        first_name = request.data.get("first_name", "")
        last_name = request.data.get("last_name", "")

        # 基本驗證
        if not all([username, email, password, password2, role]):
            return Response(
                {"error": "用戶名、email、密碼和身分都是必填的"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 檢查密碼是否一致 (password2 驗證)
        if password != password2:
            return Response(
                {"password": ["密碼不一致"]}, status=status.HTTP_400_BAD_REQUEST
            )

        # 檢查密碼長度
        if len(password) < 6:
            return Response(
                {"password": ["密碼至少需要6個字元"]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 檢查 role 是否有效（禁止一般用戶註冊為 superuser）
        valid_roles = ["teacher", "student", "both"]
        if role not in valid_roles:
            return Response(
                {"role": ["身分必須是 teacher, student 或 both"]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 檢查 username 是否已存在
        if User.objects.filter(username=username).exists():
            return Response(
                {"username": ["此用戶名已被使用"]}, status=status.HTTP_400_BAD_REQUEST
            )

        # 檢查 email 是否已存在
        if User.objects.filter(email=email).exists():
            return Response(
                {"email": ["此 email 已被註冊"]}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # 使用 Django auth 的 create_user 方法建立用戶
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,  # create_user 會自動雜湊密碼
                first_name=first_name,
                last_name=last_name,
                role=role,  # 我們的自訂欄位
            )

            # 回傳成功訊息和用戶資料（不包含密碼）
            return Response(
                {
                    "message": "註冊成功！",
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "name": user.name,  # 使用我們的 property
                        "email": user.email,
                        "role": user.role,
                        "date_joined": user.date_joined,
                    },
                },
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            return Response(
                {"error": f"註冊失敗：{str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


@extend_schema_view(
    list=extend_schema(
        summary="取得所有課程", description="取得系統中所有課程的列表", tags=["Courses"]
    ),
    create=extend_schema(
        summary="建立新課程", description="建立一個新的課程", tags=["Courses"]
    ),
    retrieve=extend_schema(
        summary="取得單一課程",
        description="根據 ID 取得特定課程的詳細資訊",
        tags=["Courses"],
    ),
    update=extend_schema(
        summary="更新課程資訊", description="更新特定課程的完整資訊", tags=["Courses"]
    ),
    partial_update=extend_schema(
        summary="部分更新課程資訊",
        description="部分更新特定課程的資訊",
        tags=["Courses"],
    ),
    destroy=extend_schema(
        summary="刪除課程", description="刪除特定課程", tags=["Courses"]
    ),
)
@method_decorator(csrf_exempt, name="dispatch")
class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


@extend_schema_view(
    list=extend_schema(
        summary="取得所有預約",
        description="取得系統中所有預約的列表",
        tags=["Bookings"],
    ),
    create=extend_schema(
        summary="建立新預約", description="建立一個新的預約", tags=["Bookings"]
    ),
    retrieve=extend_schema(
        summary="取得單一預約",
        description="根據 ID 取得特定預約的詳細資訊",
        tags=["Bookings"],
    ),
    update=extend_schema(
        summary="更新預約資訊", description="更新特定預約的完整資訊", tags=["Bookings"]
    ),
    partial_update=extend_schema(
        summary="部分更新預約資訊",
        description="部分更新特定預約的資訊",
        tags=["Bookings"],
    ),
    destroy=extend_schema(
        summary="刪除預約", description="刪除特定預約", tags=["Bookings"]
    ),
)
@method_decorator(csrf_exempt, name="dispatch")
class BookingsViewSet(viewsets.ModelViewSet):
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer


@extend_schema_view(
    list=extend_schema(
        summary="取得所有評價", description="取得系統中所有評價的列表", tags=["Reviews"]
    ),
    create=extend_schema(
        summary="建立新評價", description="建立一個新的評價", tags=["Reviews"]
    ),
    retrieve=extend_schema(
        summary="取得單一評價",
        description="根據 ID 取得特定評價的詳細資訊",
        tags=["Reviews"],
    ),
    update=extend_schema(
        summary="更新評價資訊", description="更新特定評價的完整資訊", tags=["Reviews"]
    ),
    partial_update=extend_schema(
        summary="部分更新評價資訊",
        description="部分更新特定評價的資訊",
        tags=["Reviews"],
    ),
    destroy=extend_schema(
        summary="刪除評價", description="刪除特定評價", tags=["Reviews"]
    ),
)
@method_decorator(csrf_exempt, name="dispatch")
class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
