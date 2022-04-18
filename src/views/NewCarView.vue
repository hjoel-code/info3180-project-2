<script>
import NewCarForm from "../components/Forms/NewCarForm.vue";

export default {
  components: { NewCarForm },
  data() {
    return { token: null }
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
  }

};
</script>

<template>
  <div id="new-car-page" v-if="token">
    <div class="container">
      <div class="row h-100 justify-content-center align-items-center">
        <div class="col-md-7">
          <h1>Add New Car</h1>
          <div class="card">
            <div class="card-body p-5">
              <new-car-form v-bind:token="token" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
/* Add any component specific styles here */

#new-car-page h1 {
  font-size: 190%;
  font-weight: 700;
  margin: 30px 0;
}

#new-car-page small {
  font-weight: 600;
}

#new-car-page .btn {
  padding: 5px 60px;
}

#new-car-page .container {
  min-height: 93.2vh;
  padding-bottom: 40px;
}

#new-car-page {
  background: whitesmoke;
}

#new-car-page .card {
  background: rgb(255, 255, 255);
  backdrop-filter: blur(10px);
}
</style>