<template>
  <form
    enctype="multipart/form-data"
    id="new-car-form"
    @submit.prevent="onSave"
  >
    <div class="row">
      <div class="col-6">
        <div class="form-group">
          <small class="form-label">Make</small>
          <input name="make" type="text" class="form-control" />
        </div>
      </div>
      <div class="col-6">
        <div class="form-group">
          <small class="form-label">Model</small>
          <input name="model" type="text" class="form-control" />
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-6">
        <div class="form-group">
          <small class="form-label">Colour</small>
          <input name="colour" type="text" class="form-control" />
        </div>
      </div>
      <div class="col-6">
        <div class="form-group">
          <small class="form-label">Year</small>
          <input name="year" type="number" class="form-control" />
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-6">
        <div class="form-group">
          <small class="form-label">Price</small>
          <input name="price" type="number" class="form-control" />
        </div>
      </div>
      <div class="col-6">
        <div class="form-group">
          <small class="form-label">Car Type</small>
          <select name="car_type" class="form-control">
            <option v-for="type in options.carTypes" :key="type" :value="type">
              {{ type }}
            </option>
          </select>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-6">
        <div class="form-group">
          <small class="form-label">Transmission</small>
          <select name="trans" class="form-control">
            <option v-for="trans in options.trans" :key="trans" :value="trans">
              {{ trans }}
            </option>
          </select>
        </div>
      </div>

      <div class="col-6"></div>
    </div>

    <div class="form-group">
      <small class="form-label">Description</small>
      <textarea name="description" class="form-control" />
    </div>

    <div class="row">
      <div class="col-6">
        <div class="form-group">
          <small class="form-label">Upload Photo</small>
          <input name="photo" type="file" class="form-control" />
        </div>
      </div>

      <div class="col-6"></div>
    </div>

    <button type="submit" class="btn btn-success mt-5 w-100">Save</button>
    <div v-if="response" class="mt-2">
      <div v-if="response.errors" class="alert alert-danger">
        <ul>
          <li v-for="error in response.errors" :key="error">{{ error }}</li>
        </ul>
      </div>

      <div v-if="response.success" class="alert alert-success">
        {{ response.success }}
      </div>
    </div>
  </form>
</template>




<script>
export default {
  props: ["token"],
  data() {
    return {
      csrf_token: "",
      response: null,
      form: null,
      options: {
        carTypes: ["Sedan", "Hatchback", "SUV", "Mini-van"],
        trans: ["Automatic", "Tiptronic", "Manual"],
      },
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

    onSave() {
      this.form = document.getElementById("new-car-form");
      const form_data = new FormData(this.form);
      fetch("/api/cars", {
        method: "POST",
        body: form_data,
        headers: {
          'X-CSRFToken': this.csrf_token,
          'Authorization': `Bearer ${this.token}`,
        },
      })
        .then((response) => response.json())
        .then((data) => this.onComplete(data))
        .catch((error) => alert(error.message));
    },

    onComplete(data) {
      this.response = data;
      if (data.success) this.form.reset();
    }
  },

  created() {
    this.token ? this.getToken() : null;
  },
};
</script>





<style>
.form-group {
  margin: 10px 0;
}
</style>