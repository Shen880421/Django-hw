<template>
    <div class="container">
        <!-- 導覽列 -->
        <header class="navbar">
            <div class="logo">
                <!-- <img src="/images/headset-icon.png" alt="Logo" /> -->
                <span>家教媒合平台</span>
            </div>
            <nav class="menu">
                <a href="/">主頁</a>
                <a href="/teachers">老師們</a>
                <select class="lang">
                    <option selected>繁體中文</option>
                    <option>English</option>
                </select>
                <a href="/login" class="btn-login">登入</a>
                <button class="btn-logout">登出</button>
            </nav>
        </header>

        <!-- Hero 區塊 -->
        <section class="hero">
            <h1>「引導學生，成就未來。」</h1>
        </section>

        <!-- 評論區塊 -->
        <section class="testimonials">
            <div class="card">
                <h3>非常完美！</h3>
                <p>
                    「這個平台幫我找到超合適的數學家教，<br />
                    才幾個禮拜，我的成績就大大進步了！」<br />
                    — Cody, 同學
                </p>
            </div>
            <div class="card">
                <h3>精準媒合！！</h3>
                <p>
                    「作為一位家教老師，我非常欣賞這個平台的便利性，<br />
                    能輕鬆與學生互動並追蹤他們的學習成果，值得推薦！」<br />
                    — Shen, 家教
                </p>
            </div>
            <div class="card">
                <h3>有許多人受惠！</h3>
                <p>
                    「互動式工具加上量身打造的課程，讓學習變得超有趣，<br />
                    真的是我做過最棒的決定！」<br />
                    — Alex, 同學
                </p>
            </div>
        </section>

        <!-- 行動按鈕 -->
        <section class="cta">
            <a href="/login" class="cta-button">
                🧑‍🏫 立即開始，與你的理想學生見面！
            </a>
        </section>

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

<script setup>
// 無需 JS
</script>

<style scoped>
* {
    box-sizing: border-box;
}

.container {
    font-family: "Segoe UI", sans-serif;
    background-color: #ffffff;
    min-height: 100vh;
}

/* 導覽列 */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #4f46e5;
    color: white;
    padding: 16px 32px;
}

.logo {
    display: flex;
    align-items: center;
    font-size: 20px;
    font-weight: bold;
}

.logo img {
    height: 32px;
    margin-right: 8px;
}

.menu {
    display: flex;
    align-items: center;
    gap: 16px;
}

.menu a {
    color: white;
    text-decoration: none;
}

.menu select.lang {
    padding: 4px 8px;
    border-radius: 4px;
}

.btn-login {
    background: #070172; /* 背景白色 */
    color: #4f46e5; /* 文字深藍色 */
    padding: 6px 12px;
    border-radius: 6px;
    text-decoration: none;
    border: 2px solid #4f46e5; /* 加上深藍色邊框 */
    font-weight: bold;
    transition: background 0.3s, color 0.3s;
}

.btn-login:hover {
    background: #4f46e5;
    color: white;
}

.btn-logout {
    background-color: #a5b4fc;
    border: none;
    color: #1e3a8a;
    padding: 6px 12px;
    border-radius: 6px;
    cursor: pointer;
}

/* Hero */
.hero {
    text-align: center;
    padding: 80px 20px 40px;
    background-color: #ffffff;
    position: relative;
}

.hero h1 {
    font-size: 32px;
    color: #4338ca;
    font-weight: bold;
    margin: 0;
}

/* 評論 */
.testimonials {
    background-color: #e0e7ff;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 24px;
    padding: 60px 20px;
}

.card {
    background: white;
    border: 2px solid #c7d2fe;
    padding: 24px;
    border-radius: 16px;
    max-width: 300px;
    box-shadow: 2px 4px 12px rgba(0, 0, 0, 0.05);
}

.card h3 {
    color: #4338ca;
    font-size: 18px;
    margin-bottom: 12px;
}
p {
    color: black;
}
/* CTA */
.cta {
    background-color: #c7d2fe;
    padding: 40px 0;
    text-align: center;
}

.cta-button {
    display: inline-block;
    background-color: #4f46e5;
    color: white;
    padding: 14px 28px;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
    text-decoration: none;
    transition: background-color 0.3s ease;
}

.cta-button:hover {
    background-color: #3730a3;
}
.footer {
    background-color: #4f46e5;
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
