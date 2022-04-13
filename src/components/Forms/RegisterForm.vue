<template>
  <div v-if="response" class="mb-2">
    <div v-if="response.errors" class="alert alert-danger">
      <ul>
        <li v-for="error in response.errors" :key="error">{{ error }}</li>
      </ul>
    </div>

    <div v-if="response.success" class="alert alert-success">
      {{ response.success }}
    </div>
  </div>

  <form
    enctype="multipart/form-data"
    id="register-form"
    @submit.prevent="onRegister"
  >
    <div class="row">
      <div class="col-6">
        <div class="form-group">
          <small class="form-label">Username</small>
          <input name="username" type="text" class="form-control" />
        </div>
      </div>
      <div class="col-6">
        <div class="form-group">
          <small class="form-label">Password</small>
          <input name="password" type="password" class="form-control" />
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-6">
        <div class="form-group">
          <small class="form-label">Fullname</small>
          <input name="fullname" type="text" class="form-control" />
        </div>
      </div>
      <div class="col-6">
        <div class="form-group">
          <small class="form-label">Email</small>
          <input name="email" type="email" class="form-control" />
        </div>
      </div>
    </div>

    <div class="form-group">
      <small class="form-label">Location</small>
      <input name="location" type="text" class="form-control" />
    </div>

    <div class="form-group">
      <small class="form-label">Biography</small>
      <textarea name="bio" class="form-control" />
    </div>

    <div class="form-group">
      <small class="form-label">Upload Photo</small>
      <input name="photo" type="file" class="form-control" />
    </div>

    <button type="submit" class="btn btn-secondary mt-5 w-100">Register</button>
  </form>
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

    onRegister() {
      this.form = document.getElementById("register-form");
      const form_data = new FormData(this.form);
      fetch("/api/register", {
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
      if (data.success) this.form.reset();
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