<template>
    <div class="login-page">
        <div class="login-content">
            <!-- 左側區塊：Logo 與平台名稱 -->
            <div class="left-panel">
                <img src="#" alt="平台 Logo" class="logo" />
                <h2>家教媒合平台</h2>
            </div>
            <!-- 右側區塊：登入表單 -->
            <div class="right-panel">
                <div class="login-box">
                    <h2>歡迎回來！</h2>
                    <p class="subtitle">請輸入帳號與密碼</p>

                    <form @submit.prevent>
                        <!-- 信箱欄位 -->
                        <div class="form-group">
                            <label for="email">信箱</label>
                            <input
                                id="email"
                                type="email"
                                placeholder="請輸入信箱"
                            />
                        </div>

                        <!-- 密碼欄位 -->
                        <div class="form-group">
                            <label for="password">密碼</label>
                            <input
                                id="password"
                                type="password"
                                placeholder="請輸入密碼"
                            />
                        </div>

                        <!-- 記住我 / 忘記密碼 -->
                        <div class="form-extra">
                            <label><input type="checkbox" /> 記得我</label>
                            <a href="#">忘記帳號或密碼</a>
                        </div>

                        <!-- 登入按鈕 -->
                        <button class="login-button" type="submit">登入</button>

                        <!-- 分隔線 -->
                        <div class="divider">或</div>

                        <!-- Google 登入 -->
                        <button
                            class="google-button"
                            type="button"
                            style="color: black"
                        >
                            <img
                                src="https://www.svgrepo.com/show/475656/google-color.svg"
                                alt="Google icon"
                            />
                            使用 Google 登入
                        </button>

                        <!-- 註冊連結 -->
                        <p class="signup-text">
                            還沒有帳戶？ <a href="#">註冊一個吧！</a>
                        </p>
                    </form>
                </div>
            </div>
        </div>
        <!-- 頁尾 -->
        <footer class="footer">
            <a href="#">關於我們</a>
            <a href="#">幫助中心</a>
            <a href="#">常見問題</a>
            <a href="#">服務條款</a>
            <a href="#">隱私權政策</a>
            <a href="#">Cookie 使用政策</a>
            <a href="#">無障礙瀏覽</a>
            <a href="#">申請成為老師</a>
            <a href="#">設定</a>
            <a href="#">帳戶設定</a>
        </footer>
    </div>
</template>

<script scoped>
// 僅畫面無功能，無需邏輯處理
export default {};
</script>

<style scoped>
/* 整體頁面排版 */
.login-page {
    display: flex;
    flex-direction: column; /* 改為 column */
    min-height: 100vh;
    font-family: "Arial", sans-serif;
}

/* 登入內容區塊 */
.login-content {
    flex: 1;
    display: flex;
    flex-direction: row;
}

/* 左側區塊 */
.left-panel {
    width: 35%;
    background: #e5f0e5;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 40px;
}

.left-panel .logo {
    width: 80px;
    margin-bottom: 20px;
}

.left-panel h2 {
    font-size: 24px;
    color: #111;
}

/* 右側區塊：表單區域 */
.right-panel {
    width: 65%;
    background: url("/login-bg.jpg") no-repeat center/cover;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 60px 40px;
}

.login-box {
    background-color: #f5f5f9;
    padding: 40px;
    border-radius: 10px;
    width: 100%;
    max-width: 420px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    color: #111;
}

.login-box h2 {
    margin-bottom: 8px;
}

.subtitle {
    font-size: 14px;
    color: #666;
    margin-bottom: 24px;
}

.form-group {
    margin-bottom: 16px;
}

.form-group label {
    font-weight: bold;
    display: block;
    margin-bottom: 6px;
}

.form-group input {
    width: 100%;
    padding: 12px;
    border: 1px solid #aaaaff;
    border-radius: 8px;
    font-size: 14px;
}

/* 記得我與忘記密碼區 */
.form-extra {
    display: flex;
    justify-content: space-between;
    font-size: 13px;
    margin-bottom: 16px;
}

.login-button {
    width: 100%;
    padding: 12px;
    background-color: #6d58c4;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    cursor: pointer;
    margin-bottom: 16px;
}

.divider {
    text-align: center;
    color: #aaa;
    margin-bottom: 16px;
}

.google-button {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    width: 100%;
    padding: 12px;
    border: 1px solid #ccc;
    background: white;
    border-radius: 8px;
    cursor: pointer;
}

.google-button img {
    width: 18px;
    height: 18px;
}

/* 註冊提示文字 */
.signup-text {
    font-size: 14px;
    text-align: center;
    margin-top: 20px;
}

/* 頁尾連結 */
.footer {
    background-color: #6d58c4;
    color: white;
    font-size: 12px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 16px;
    padding: 12px 16px;
    /* 移除 position: absolute, bottom, left, right */
}

.footer a {
    color: white;
    text-decoration: none;
}
</style>
