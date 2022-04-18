<script>
import RegisterForm from "../components/Forms/RegisterForm.vue";

export default {
  components: { RegisterForm },
  methods: {
    isAuthenticated() {
      const session = window.sessionStorage.getItem("user_session");
      if (session) {
        window.location.replace('/explore')
      }
    }
  },
  created() {
    this.isAuthenticated()
  }
};
</script>

<template>
  <div id="register-page">
    <div class="container">
      <div class="row h-100 justify-content-center align-items-center">
        <div class="col-md-7">
          <h1 class="text-center">Register New User</h1>
          <div class="card">
            <div class="card-body p-5">
              <register-form />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
/* Add any component specific styles here */

#register-page h1 {
  font-size: 190%;
  font-weight: 700;
  margin: 30px 0;
}

#register-page small {
  font-weight: 600;
}

#register-page .btn {
  padding: 5px 60px;
}

#register-page .container {
  min-height: 93.2vh;
  padding-bottom: 40px;
}

#register-page {
  background: whitesmoke;
}

#register-page .card {
  background: rgb(255, 255, 255);
  backdrop-filter: blur(10px);
}
</style>