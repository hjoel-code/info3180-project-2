<script setup>
import { RouterLink, RouterView } from "vue-router";
import Header from "./components/Header/index.vue";
import AppFooter from "@/components/AppFooter.vue";
</script>

<template>
  <Header />
  <RouterView />
</template>

<style>
body {
  padding-top: 50px;
}
</style>