<template>
  <div class="card">
    <div class="card-body py-5 px-4">
      <form class="d-flex justify-content-center align-items-end" @submit.prevent="onSearch" >
        <div class="form-group m-0 px-2 w-100">
          <small class="form-label">Make</small>
          <input name="make" type="text" class="form-control" />
        </div>
        <div class="form-group px-2 m-0 w-100">
          <small class="form-label">Model</small>
          <input name="model" type="text" class="form-control" />
        </div>
        <div class="btn-container px-2 w-100">
          <button type="submit" class="btn btn-success w-100">Search</button>
        </div>
      </form>
    </div>
  </div>
</template>


<script>
export default {
  props: ['token'],
  data() {
    return { };
  },

  methods: {

    onSearch() {
      // fetch("/api/register", {
      //   method: "GET",
      //   headers: {
      //     "Authorization": `Bearer ${this.token}`
      //   },
      // })
      //   .then((response) => response.json())
      //   .then((data) => this.onComplete(data))
      //   .catch((error) => alert(error.message));
    }
  }
};
</script>
