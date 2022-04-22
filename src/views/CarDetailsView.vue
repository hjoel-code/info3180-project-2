<template>
  <div v-if="token && uid">
    <car-details v-bind:token="token" />
  </div>
</template>



<script>
import CarDetails from "../components/Explore/CarDetails.vue";

export default {
  components: { CarDetails },

  data() {
    return { token: null, uid: null };
  },

  methods: {
    isAuthenticated() {
      const session = window.localStorage.getItem("user_session")
        ? JSON.parse(window.localStorage.getItem("user_session"))
        : null;
      if (!session) window.location.replace("/");
      if (session) {
        this.token = session.token;
        this.uid = session.user;
      }
    },
  },

  created() {
    this.isAuthenticated();
  },
};
</script>