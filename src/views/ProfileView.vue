<template>
    <div class="carder"> 
    <br>
    <br>
    <div class= "grid-box">
    <img src="https://images.unsplash.com/photo-1617650728468-8581e439c864?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80"
            alt=""
          />
        <div class="wrapper">
        <div class="user_details">
        <h2> Danica Patrick </h2>
        <h4> @dpatrick </h4>
        <p> I am a former racing professional and the most successful woman in the history of 
        American open wheelracing. I love cars and driving fast.</p>
        </div>

        <div class="details">
        <p style="margin:0;display:inline;float:left;"> Email</p>
        <p style="margin:0;display:inline:float:right; ">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; dpatric@example.com </p>

        <p style="margin:0;display:inline;float:left;"> Location </p>
        <p style="margin:0;display:inline:float:right; ">&nbsp;&nbsp;&nbsp;&nbsp; Wisconsin, USA</p>

        <p style="margin:0;display:inline;float:left;"> Joined  </p>
        <p style="margin:0;display:inline:float:right; ">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;April 8, 2021</p>
        </div>
        </div>
        </div>
       
    </div>
    
</template>

<script>
export default {
  data() {
    return { token: null };
  },

  methods: {
    isAuthenticated() {
      const token = window.sessionStorage.getItem("token");
      if (!token) window.location.replace("/");
      if (token) {
        this.token = token;
      }
    },
  },

  created() {
    this.isAuthenticated();
  },
};
</script>


<style>
img{
    height:100%;
    width:80%;
    border-radius:50%;
}

.grid-box{
    display:grid;
    grid-template-columns: 27% 73%;
    grid-template-rows: 50% 50%;
    padding: 5% 5%;
    border-radius:5px;
    background-color:white;
    box-shadow: 1px 1px 1px 1px grey;
}

.carder{
    padding: 5% 15%;
}

.details{
    padding-top: 2%;
}
</style>