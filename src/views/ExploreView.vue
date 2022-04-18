<script>
import FilterForm from "../components/Explore/FilterForm.vue";


export default {
  components: { FilterForm },

  data() {
    return { token: null };
  },

  methods: {
    isAuthenticated() {
      
      const session = window.sessionStorage.getItem("user_session") ? JSON.parse(window.sessionStorage.getItem("user_session")) : null;
      if (!session) window.location.replace("/");
      if (session) {
        this.token = session.token
      }
    },
  },

  created() {
    this.isAuthenticated();
  },
};
</script>

<template>
  <div id="explore-page" v-if="token">
    <div class="container-fluid">
      <div class="row h-100 justify-content-center align-items-center">
        <div class="col-sm-10 col-md-8 col-sm-7">
          <h1>Explore</h1>
          <filter-form v-bind:token="token" />
        </div>
      </div>
    </div>
  </div>
</template>

<style>
/* Add any component specific styles here */

#explore-page h1 {
  font-size: 190%;
  font-weight: 700;
  margin: 30px 0;
}

#explore-page small {
  font-weight: 600;
}

#explore-page .container-fluid {
  min-height: 93.2vh;
  padding-bottom: 40px;
}

#explore-page {
  background: whitesmoke;
}

#explore-page .card {
  background: rgb(255, 255, 255);
  backdrop-filter: blur(10px);
}
</style>