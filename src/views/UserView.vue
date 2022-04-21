<template>
  <div class="carder">
    <br />
    <br />
    <div class="grid-box">
      <img :src="`../../uploads/${details.photo}`"/>
      <div class="wrapper">
        <div class="user_details">
          
          <h2>{{details.fullName}}</h2>
          <h4>@{{details.username}}</h4>
          <p>
            {{details.biography}}
          </p>
        </div>

        <div class="details">
          <p style="margin: 0; display: inline; float: left">Email</p>
          <p style="margin:0;display:inline:float:right; ">
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            {{details.email}}
          </p>

          <p style="margin: 0; display: inline; float: left">Location</p>
          <p style="margin:0;display:inline:float:right; ">
            &nbsp;&nbsp;&nbsp;&nbsp; {{details.location}}
          </p>

          <p style="margin: 0; display: inline; float: left">Joined</p>
          <p style="margin:0;display:inline:float:right; ">
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{details.date_joined}}
          </p>
        </div>
      </div>
    </div>
  </div>
  <h3 id="spacer"> Cars Favourited</h3>
  <div class="car-grid">
      <div class="card" style="width: 100%;">
        <img class="card-img-top" src="..." alt="Card image cap">
        <div class="card-body">
        <h5 class="card-title">{{fave.year}}&nbsp;&nbsp;{{fave.make}}</h5>
        <p class="card-text">{{fave.model}}</p>
        <a href="#" class="btn btn-primary">View more details</a>
      </div>
    </div>
  </div>

  

</template>

<script>
export default {
  data() {
    return { token: null, details: [], fave:[]  };
  },
  methods: {
    isAuthenticated() {
      const session = window.localStorage.getItem("user_session")
        ? JSON.parse(window.localStorage.getItem("user_session"))
        : null;
      console.log(session)
      if (!session) window.location.replace("/");
      if (session) {
        this.token = session.token;
      }
    },
    getData() {
      fetch(`/api/users/${this.$route.params.user_id}`, {
        method: "GET",
        headers: {
          'Authorization': `Bearer ${this.token}`
        }
      })
        .then((response) => response.json())
        
        .then((data) => {
          console.log(data);
          this.details=data;
          this.img = data.photo;
        });
    },
      getfavourite() {
      fetch(`/api/users/${this.$route.params.user_id}/favourites`, {
        method: "GET",
        headers: {
          'Authorization': `Bearer ${this.token}`
        }
      })
        .then((response) => response.json())
        
        .then((data) => {
          console.log(data);
          this.fave=data;
        });
    }
  },
  created() {
    this.isAuthenticated();
    this.getData();
    this.getfavourite();
    let self = this
  }
};
</script>


<style>
#spacer{
  padding: 0% 15%;
}
img {
  height: 100%;
  width: 80%;
  border-radius: 50%;
}
.grid-box {
  display: grid;
  grid-template-columns: 27% 73%;
  grid-template-rows: 50% 50%;
  padding: 5% 5%;
  border-radius: 5px;
  background-color: white;
  box-shadow: 1px 1px 1px 1px grey;
}
.car-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: auto;
  padding: 3% 15%;
  grid-gap:7%;
  padding-bottom: 7%;
}
.carder {
  padding: 2% 15%;
}
.details {
  padding-top: 2%;
}
</style>