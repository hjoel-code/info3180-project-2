<template>
  <div v-for="car in cars" :key="car.id" class="col-sm-6 col-md-4 py-4">
    <div class="card">
      <div class="card-image">
        <a :href="`/cars/${car.id}`">
          <img class="w-100" :src="`/api/uploads/${car.photo}`" alt="" />
        </a>
      </div>
      <div class="card-body pt-2">
        <div class="d-flex justify-content-between">
          <div class="description">
            <h6 class="m-0">{{ `${car.year} ${car.make} ${car.model}` }}</h6>
            <small class="text-muted">{{ car.car_type }}</small>
          </div>

          <div class="price-container ml-3">
            <div class="badge bg-warning text-dark">
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
              {{ formatPrice(car.price) }}
            </div>
          </div>
        </div>

        <a :href="`/cars/${car.id}`" class="btn btn-success w-100 mt-4">
          <small>More Details</small>
        </a>
      </div>
    </div>
  </div>
</template>




<script>
import numeral from "numeral";

export default {
  props: ["results"],

  data() {
    return { cars: [] };
  },

  methods: {
    formatPrice: (price) => {
      return numeral(price).format("$ 0,0.00");
    },
  },

  updated() {
    this.cars = this.results;
  },

  created() {
    this.cars = this.results;
  },
};
</script>