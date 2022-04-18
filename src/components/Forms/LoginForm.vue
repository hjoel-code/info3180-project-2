<template>
  <form id="login-form" @submit.prevent="onLogin">
    <div class="form-group">
      <small class="form-label">Username</small>
      <input name="username" type="text" class="form-control" />
    </div>
    <div class="form-group">
      <small class="form-label">Password</small>
      <input name="password" type="password" class="form-control" />
    </div>

    <button type="submit" class="btn btn-secondary mt-5 w-100">Login</button>
  </form>

  <div v-if="response" class="mt-5">
    <div v-if="response.errors" class="alert alert-danger">
      <ul>
        <li v-for="error in response.errors" :key="error">{{ error }}</li>
      </ul>
    </div>

    <div v-if="response.success" class="alert alert-success">
      {{ response.success }}
    </div>
  </div>
</template>



<script>
export default {
  data() {
    return {
      csrf_token: "",
      response: null,
      form: null,
    };
  },

  methods: {
    getToken() {
      fetch("/api/csrf-token")
        .then((response) => response.json())
        .then((data) => {
          this.csrf_token = data.csrf_token;
        })
        .catch((error) => alert(error.message));
    },

    onLogin() {
      this.form = document.getElementById("login-form");
      const form_data = new FormData(this.form);
      fetch("/api/auth/login", {
        method: "POST",
        body: form_data,
        headers: {
          "X-CSRFToken": this.csrf_token,
        },
      })
        .then((response) => response.json())
        .then((data) => this.onComplete(data))
        .catch((error) => alert(error.message));
    },

    onComplete(data) {
      this.response = data;
      if (data.success) {
        window.localStorage.setItem('user_session', JSON.stringify( { token: data?.token, user: data?.user } ))
        window.location.replace('/explore')
        this.form.reset();
      } 
    },
  },

  created() {
    this.getToken();
  },
};
</script>





<style>
.form-group {
  margin: 10px 0;
}
</style>