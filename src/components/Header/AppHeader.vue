<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container-fluid justify-content-between">
        <a class="navbar-brand" href="/"> United Car Sales </a>

        <button
          class="navbar-toggler"
          data-bs-toggle="collapse"
          data-bs-target="#navItemsContainer"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navItemsContainer">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <RouterLink to="/cars/new" class="nav-link">Add Car</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink to="/explore" class="nav-link">Explore</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="`/users/${user_id}`" class="nav-link">My Profile</RouterLink>
            </li>
          </ul>

          <div class="nav-item">
            <RouterLink to="/logout" class="nav-link">Logout</RouterLink>
          </div>
        </div>
      </div>
    </nav>
  </header>
</template>


<script>
import { RouterLink } from "vue-router";
export default {
  props: ['user'],
  data() {
    return { user_id: this.user }
  },
  updated() {
    this.user_id = this.user
  }
}
</script>