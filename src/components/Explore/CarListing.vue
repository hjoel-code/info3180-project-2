<template>
  <div v-for="car in cars" :key="car.id" class="col-sm-6 col-md-4 py-4">
    <div class="card">
      <div class="card-image">
        <a :href="`/cars/${car.id}`">
          <img
            class="w-100"
            :src="`../../uploads/${car.photo}`"
            alt=""
          />
        </a>
      </div>
      <div class="card-body pt-2">
        <div class="d-flex justify-content-between">
          <div class="description">
            <h6 class="m-0">{{ `${car.year} ${car.make} ${car.model}`}}</h6>
            <small class="text-muted">{{ car.car_type }}</small>
          </div>

          <div class="price-container">
            <div class="badge bg-warning text-dark">{{ formatPrice(car.price) }}</div>
          </div>
        </div>

        <a :href="`/cars/${car.id}`" class="btn btn-secondary w-100 mt-4">
          <small>More Details</small>
        </a>
      </div>
    </div>
  </div>
</template>




<script>
import numeral from 'numeral'


export default {
  props: ['results'],

  data() {
    return { cars: [] }
  },

  methods: {
    formatPrice: (price) => {
      return numeral(price).format('$ 0,0.00')
    }
  },

  updated() {
    this.cars = this.results
  },

  created() {
    this.cars = this.results
  }
}
</script>