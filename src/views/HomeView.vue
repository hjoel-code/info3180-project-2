<script>
export default {
  data() {
    return {
      message: "Hello World! This is Lab 7",
    };
  },

  methods: {
    isAuthenticated() {
      const session = window.localStorage.getItem("user_session");
      if (session) {
        window.location.replace('/explore')
      }
    },
  },


  created() {
    this.isAuthenticated()
  }
};
</script>

<template>
  <div id="home-page">
    <div class="container">
      <div class="row h-100 justify-content-center align-items-center">
        <div class="col-md-8">
          <div class="content">
            <div class="text-left">
              <h1>Buy and Sell Cars Online</h1>
              <small
                >United Auto Sales provides the fastest, easiest and most
                friendly way to buy or sell cars online. Find a Great Price on
                the Vehicle You Want.</small
              >
            </div>
            <div class="d-flex my-4">
              <div class="px-2">
                <a href="/register" class="btn btn-secondary">Register</a>
              </div>
              <div class="px-2">
                <a href="/login" class="btn btn-light">Login</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
/* Add any component specific styles here */

#home-page h1 {
  font-size: 350%;
  font-weight: 700;
  color: white;
}

#home-page small {
  color: white;
}

#home-page .btn {
  padding: 5px 60px;
}

#home-page .container {
  height: 93.2vh;
}

#home-page {
  background-image: url("https://images.unsplash.com/photo-1494976388531-d1058494cdd8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80");
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
}

#home-page .content {
  background: rgba(0, 0, 0, 0.366);
  backdrop-filter: blur(10px);
  padding: 80px;
}
</style>