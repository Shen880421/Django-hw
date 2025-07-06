<script setup>
import { useRoute } from "vue-router";

const route = useRoute();
</script>

<template>
    <!-- 顯示子頁面 -->
    <RouterView />

    <!-- 如果不是 login 頁面才顯示導覽列 -->
    <nav v-if="!['/login', '/'].includes(route.path)">
        <Router-link to="/">首頁</Router-link><br />
        <Router-link to="/about">關於</Router-link><br />
        <Router-link to="/login">登入</Router-link><br />
        <Router-link to="/exmp">範例</Router-link><br />
        <Router-link to="/hello">哈摟</Router-link><br />
    </nav>
</template>

<style scoped></style>
