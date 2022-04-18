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
            authorized: null,
            user: null
        }
    },

    methods:{
        isAuthorized(){
            const session = window.sessionStorage.getItem('user_session')
            if(session){
                this.authorized =true
                this.user
            }
        }

    }
    components: { AuthHeader, AppHeader }
}


</script>