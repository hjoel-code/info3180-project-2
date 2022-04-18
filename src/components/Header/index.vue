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

<<<<<<< HEAD
    methods:{
        isAuthorized(){
            const session = window.sessionStorage.getItem('user_session')
            if(session){
                this.authorized =true
                this.user
            }
        }

    }
=======
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


>>>>>>> implementation
    components: { AuthHeader, AppHeader }
}


</script>