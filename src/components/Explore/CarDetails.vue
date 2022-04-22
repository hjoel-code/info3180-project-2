<template>
  <div id="car-details-page">
    <div class="container py-5">
      <div class="row justify-content-center">
        <div class="col-sm-12 col-md-10">
          <div class="card flex-row">
            <div class="card-image">
              <img :src="`../../uploads/${car?.photo}`" alt="" />
            </div>

            <div class="card-body flex-column pt-3">
              <div class="d-flex justify-content-between flex-column">
                <h2 class="card-title">{{ car?.year }} {{ car?.make }}</h2>
                <h5 class="text-muted">{{ car?.model }}</h5>
                <small class="text-muted">{{ car?.description }}</small>
              </div>

              <div class="d-flex flex-row pt-3">
                <div class="d-flex flex-column">
                  <div class="d-flex flex-row">
                    <div class="text-muted fw-bold">Color</div>
                    <div class="fw-bold px-2">{{ car?.colour }}</div>
                  </div>
                  <div class="d-flex flex-row">
                    <div class="text-muted fw-bold">Price</div>
                    <div class="fw-bold px-3">
                      <small>
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="16"
                          height="16"
                          viewBox="0 0 24 24"
                          fill="none"
                          stroke="currentColor"
                          stroke-width="2"
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          class="feather feather-tag"
                        >
                          <path
                            d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"
                          ></path>
                          <line x1="7" y1="7" x2="7.01" y2="7"></line>
                        </svg>

                        {{ formatPrice(car?.price) }}
                      </small>
                    </div>
                  </div>
                </div>
                <div class="p-4"></div>
                <div class="d-flex flex-column justify-column-end">
                  <div class="d-flex flex-row">
                    <div class="text-muted fw-bold">Body Type</div>
                    <div class="fw-bold px-2">{{ car?.car_type }}</div>
                  </div>
                  <div class="d-flex flex-row">
                    <div class="text-muted fw-bold">Transmission</div>
                    <div class="fw-bold px-2">{{ car?.transmission }}</div>
                  </div>
                </div>
              </div>

              <div class="d-flex justify-content-between btn-panel">
                <a href="#" class="btn btn-warning email-btn fw-bold">
                  Email Owner
                </a>
                <button v-on:click="handleFavouriteButton" class="btn favorite">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    width="18"
                    height="18"
                    :fill="isFavourited ? 'red' : 'black'"
                  >
                    <g id="_01_align_center" data-name="01 align center">
                      <path
                        d="M17.5.917a6.4,6.4,0,0,0-5.5,3.3A6.4,6.4,0,0,0,6.5.917,6.8,6.8,0,0,0,0,7.967c0,6.775,10.956,14.6,11.422,14.932l.578.409.578-.409C13.044,22.569,24,14.742,24,7.967A6.8,6.8,0,0,0,17.5.917ZM12,20.846c-3.253-2.43-10-8.4-10-12.879a4.8,4.8,0,0,1,4.5-5.05A4.8,4.8,0,0,1,11,7.967h2a4.8,4.8,0,0,1,4.5-5.05A4.8,4.8,0,0,1,22,7.967C22,12.448,15.253,18.416,12,20.846Z"
                      />
                    </g>
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import numeral from "numeral";

export default {
  props: ['token'],

  data() {
    return { car: null, user: null, isFavourited: false };
  },

  methods: {
    formatPrice(price) {
      return numeral(price).format("$ 0,0.00");
    },

    getData() {
      const self = this;
      fetch(`/api/cars/${self.$route.params.car_id}`, {
        method: "GET",
      })
        .then((response) => response.json())
        .then((data) => {
          this.car = data;
        })
        .catch((error) => alert(error.message));
    },

    handleFavouriteButton() {
      fetch(`/api/cars/${this.car.id}/favourite`, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${this.token}`,
        },
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.state) {
            console.log(data)
            this.isFavourited =  data.state.includes('removed') ? false : true
          }
        })
        .catch((error) => console.log(error.message));
    },

    getFavourites() {
      const user = JSON.parse(window.localStorage.getItem("user_session"));
      
      fetch(`/api/users/${user.user}/favourites`, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${user.token}`,
        },
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.cars) {
            const cars = data.cars
            const favourite = cars.filter( car => car.id === parseInt(this.$route.params.car_id))
            this.isFavourited = favourite.length > 0 ? true
              : false;
          }


        })
        .catch((error) => console.log(error));
    }
  },

  created() {
    this.getData();
    this.getFavourites();
  },
};
</script>




<style>
#car-details-page {
  background: whitesmoke;
  min-height: 100vh;
}

#car-details-page .card-image {
  overflow: hidden;
  display: flex;
  width: 40%;
  justify-content: center;
}

#car-details-page .card {
  max-height: 49vh !important;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 2px 0 10px 0 rgb(200, 200, 200);
}

#car-details-page .card-image img {
  height: 100%;
}

#car-details-page .email-btn {
  border-radius: 15px;
  padding: 10px 30px;
}

#car-details-page .favorite.btn {
  border-radius: 30px;
  border: solid 1px rgb(202, 202, 202);
}

#car-details-page .btn-panel {
  margin-top: 80px;
}
</style>
