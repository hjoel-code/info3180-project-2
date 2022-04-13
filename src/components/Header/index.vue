<template>
    <auth-header v-if="!isAuthorized" />
    <app-header v-if="isAuthorized" />
</template>



<script>
import AuthHeader from './AuthHeader.vue'
import AppHeader from './AppHeader.vue'

export default {
    data() {
        return {
            isAuthorized: window.sessionStorage.getItem('token') ? true : false
        }
    },
    components: { AuthHeader, AppHeader }
}


</script>