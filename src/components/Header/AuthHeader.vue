<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container-fluid d-flex justify-content-between">
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
              <RouterLink to="/register" class="nav-link">Register</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink to="/login" class="nav-link">Login</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>



<script>
import { RouterLink } from "vue-router";
</script>