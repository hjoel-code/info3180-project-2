<script>
import LoginForm from "../components/Forms/LoginForm.vue";

export default {
  components: { LoginForm },
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
  <div id="login-page">
    <div class="container">
      <div class="row h-100 justify-content-center align-items-center">
        <div class="col-md-4">
          <h1 class="text-center">Login to your account</h1>
          <div class="card">
            <div class="card-body p-5">
              <login-form />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
/* Add any component specific styles here */

#login-page h1 {
  font-size: 190%;
  font-weight: 700;
  margin: 30px 0;
}

#login-page small {
  font-weight: 600;
}

#login-page .btn {
  padding: 5px 60px;
}

#login-page .container {
  min-height: 93.2vh;
  padding-bottom: 40px;
}

#login-page {
  background: whitesmoke;
}

#login-page .card {
  background: rgb(255, 255, 255);
}
</style>