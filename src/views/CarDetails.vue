<template>
<div class="col-sm-6 col-md-4 py-4">
<div class="container ">
    <div class="card d-flex flex-row">
        
        <div class="card-image">
            
            <img
                class=""
                :src="`../../uploads/${cars.photo}`"
                alt=""
            />
            
        </div>
        
        <div class="card-body d-flex flex-column pt-2 ">
            <div class="d-flex justify-content-between flex-column">
                <h1 class="card-title lead">{{cars.year}} {{cars.make}}</h1>
                <h6 class="text-muted">{{cars.model}}</h6>
                <small class="text-muted pt-3">{{ cars.description }}</small>
            </div>
            <div class="d-flex flex-row pt-3">
                <div class="d-flex flex-column">
                    <div class="d-flex flex-row ">
                        <div class="text-muted font-weight-bold px-3 ">Color</div>
                        <div class="font-weight-bold px-3 ">{{ cars.colour }}</div>
                    </div>
                    <br>
                    <div class="d-flex flex-row">
                        <div class="text-muted font-weight-bold px-3">Price</div>
                        <div class="font-weight-bold px-3">{{ formatPrice(cars.price)  }}</div>
                    </div>
                </div>
                <div class="p-4"></div>
                <div class="d-flex flex-column ">
                    <div class="d-flex flex-row">
                        <div class="text-muted font-weight-bold px-3">Body Type</div>
                        <div class="font-weight-bold px-3">{{ cars.car_type }}</div>
                    </div>
                    <br>
                    <div class="d-flex flex-row">
                        <div class="text-muted font-weight-bold px-3">Transmission</div>
                        <div class="font-weight-bold px-3">{{ cars.trans }}</div>
                    </div> 
                </div>
            </div>
            <div class="pt-4">
                <a href="{{url_for('addVehicleToFavourite()')}}" class="btn btn-secondary btn-success mt-4">
                    <small>Email Owner</small>
                </a>
            </div>
        </div>

    </div>
</div>
</div>
</template>

<script>
import numeral from 'numeral'



export default {

  data() {
    return { token: null, cars: [] };
  },

  methods: {
    formatPrice: (price) => {
      return numeral(price).format('$ 0,0.00')
    },

    getData(){
        fetch(`/api/cars/${this.$route.params.car_id}`, {
            method: "GET",
            headers: {
                'Authorization': `Bearer ${this.token}`
            }
        })
        .then((response) => response.json())
        .then((data)=>{
            console.log(data);
            this.cars=data;
        })
        .catch((error) => alert(error.message));
    }
  },

  //updated() {
    //this.cars = this.results
   // this.getData()
 // },

  created() {
      this.getData()
    //this.cars = this.results
  }
}
</script>