<template>
  <div class="card">
    <div class="card-body py-5 px-4">
      <form
        class="d-flex justify-content-center align-items-end"
        @submit.prevent="onSearch"
      >
        <div class="form-group m-0 px-2 w-100">
          <small class="form-label">Make</small>
          <input v-model="make" name="make" type="text" class="form-control" />
        </div>
        <div class="form-group px-2 m-0 w-100">
          <small class="form-label">Model</small>
          <input
            v-model="model"
            name="model"
            type="text"
            class="form-control"
          />
        </div>
        <div class="btn-container px-2 w-100">
          <button type="submit" class="btn btn-success w-100">Search</button>
        </div>
      </form>
    </div>
  </div>

  <div class="row mt-5">
    <car-listing v-bind:results="cars" />
  </div>
</template>


<script>
import CarListing from "./CarListing.vue";

export default {
  components: { CarListing },

  props: ["token"],

  data() {
    return {
      cars: [],
      make: "",
      model: "",
    };
  },

  methods: {
    getAllCars() {
      fetch("/api/cars", {
        method: "GET",
        headers: { Authorization: `Bearer ${this.token}` }
      })
        .then((response) => response.json())
        .then((data) => {
          this.cars = data.cars;
        })
        .catch((error) => alert(error.message));
    },

    onSearch() {
      const params = new URLSearchParams();
      this.make === "" ? null : params.set("make", this.make);
      this.model === "" ? null : params.set("model", this.model);

      fetch(`/api/search?${params.toString()}`, {
        method: "GET"
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.cars) {
            this.cars = data.cars;
          } else {
            this.getAllCars();
          }
        })
        .catch((error) => alert(error.message));
    },
  },

  created() {
    this.getAllCars();
  }
};
</script>
