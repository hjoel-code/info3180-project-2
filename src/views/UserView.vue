<template>
  <div id="user-page-container">
    <div class="carder">
      <br />
      <br />
      <div class="card">
        <div class="card-body p-4">
          <div class="row justify-content-center">
            <div
              class="
                col-md-3 col-sm-12
                d-flex
                justify-content-md-center
              "
            >
              <div class="image-container mt-md-3 my-sm-5">
                <img :src="`../../uploads/${details.photo}`" />
              </div>
            </div>

            <div class="col-md-9 col-sm-12 mt-sm-3 mt-md-0">
              <div class="wrapper">
                <div class="user_details">
                  <h2>{{ details.fullName }}</h2>
                  <h4>@{{ details.username }}</h4>
                  <p>
                    {{ details.biography }}
                  </p>
                </div>

                <div class="details">
                  <p style="margin: 0; display: inline; float: left">Email</p>
                  <p style="margin:0;display:inline:float:right; ">
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <b>{{ details.email }}</b>
                  </p>

                  <p style="margin: 0; display: inline; float: left">
                    Location
                  </p>
                  <p style="margin:0;display:inline:float:right; ">
                    &nbsp;&nbsp;&nbsp;&nbsp; <b>{{ details.location }}</b> 
                  </p>

                  <p style="margin: 0; display: inline; float: left">Joined</p>
                  <p style="margin:0;display:inline:float:right; ">
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <b>{{ details.date_joined }}</b>
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <h3 id="spacer">Cars Favourited</h3>

    <div class="row mt-5">
      <car-listing v-bind:results="fave" />
    </div>
  </div>
</template>

<script>
import CarListing from "../components/Explore/CarListing.vue";

export default {
  data() {
    return { token: null, details: [], fave: [] };
  },
  components: { CarListing },
  methods: {
    isAuthenticated() {
      const session = window.localStorage.getItem("user_session")
        ? JSON.parse(window.localStorage.getItem("user_session"))
        : null;
      console.log(session);
      if (!session) window.location.replace("/");
      if (session) {
        this.token = session.token;
      }
    },
    getData() {
      fetch(`/api/users/${this.$route.params.user_id}`, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${this.token}`,
        },
      })
        .then((response) => response.json())

        .then((data) => {
          console.log(data);
          this.details = data;
          this.img = data.photo;
        });
    },
    getfavourite() {
      fetch(`/api/users/${this.$route.params.user_id}/favourites`, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${this.token}`,
        },
      })
        .then((response) => response.json())

        .then((data) => {
          console.log(data);
          this.fave = data;
        });
    },
  },
  created() {
    this.isAuthenticated();
    this.getData();
    this.getfavourite();
    let self = this;
  },
};
</script>


<style>
#user-page-container {
  background: whitesmoke;
  min-height: 100vh;
}

#user-page-container #spacer {
  padding: 0% 15%;
}

#user-page-container .image-container {
  height: 20vh;
  width: 20vh;
  border-radius: 50%;
  overflow: hidden !important;
}

#user-page-container .image-container img {
  max-height: 100%;
  object-fit: cover;
  object-position: center;
}

#user-page-container .card {
  border-radius: 5px;
  background-color: white;
  box-shadow: 1px 1px 1px 1px grey;
  padding-bottom: 80px;
}
#user-page-container .car-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: auto;
  padding: 3% 15%;
  grid-gap: 7%;
  padding-bottom: 7%;
}
#user-page-container .carder {
  padding: 2% 15%;
}
#user-page-container .details {
  padding-top: 2%;
}
</style>