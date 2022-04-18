<template>
    <auth-header v-if="!authorized" />
    <app-header v-if="authorized" v-bind:user="user" />
</template>



<script>
import AuthHeader from './AuthHeader.vue'
import AppHeader from './AppHeader.vue'

export default {
    data() {
        return {
            authorized: null,
            user: null
        }
    },

    methods: {
        isAuthorized() {
            const session = window.sessionStorage.getItem('user_session') ? JSON.parse(window.sessionStorage.getItem('user_session')) : null
            if (session) {
                this.authorized = true
                this.user = session.user
            }
        } 
    },


    created() {
        this.isAuthorized()
    },


    components: { AuthHeader, AppHeader }
}


</script>