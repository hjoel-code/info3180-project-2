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
                        <div class="text-muted font-weight-bold  ">Color:</div>
                        <div class="font-weight-bold px-3 ">{{ cars.colour }}</div>
                    </div>
                    <br>
                    <div class="d-flex flex-row">
                        <div class="text-muted font-weight-bold ">Price:</div>
                        <div class="font-weight-bold px-3">
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
                            
                            {{ formatPrice(cars.price)  }}
                        </div>
                    </div>
                </div>
                <div class="p-4"></div>
                <div class="d-flex flex-column justify-column-end">
                    <div class="d-flex flex-row">
                        <div class="text-muted font-weight-bold ">Body Type:</div>
                        <div class="font-weight-bold px-3">{{ cars.car_type }}</div>
                    </div>
                    <br>
                    <div class="d-flex flex-row">
                        <div class="text-muted font-weight-bold ">Transmission:</div>
                        <div class="font-weight-bold px-3">{{ cars.trans }}</div>
                    </div> 
                </div>
            </div>
            <br><br><br><br>
            <div class="d-flex row">

                <div class="">
                <a href="" class="btn btn-secondary btn-success mt-4">
                    <small>Email Owner</small>
                </a>
                </div>
                <div class=" d-flex justify-content-end w-100">
               
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" height="16">
                <g id="_01_align_center" data-name="01 align center"><path d="M17.5.917a6.4,6.4,0,0,0-5.5,3.3A6.4,6.4,0,0,0,6.5.917,6.8,6.8,0,0,0,0,7.967c0,6.775,10.956,14.6,11.422,14.932l.578.409.578-.409C13.044,22.569,24,14.742,24,7.967A6.8,6.8,0,0,0,17.5.917ZM12,20.846c-3.253-2.43-10-8.4-10-12.879a4.8,4.8,0,0,1,4.5-5.05A4.8,4.8,0,0,1,11,7.967h2a4.8,4.8,0,0,1,4.5-5.05A4.8,4.8,0,0,1,22,7.967C22,12.448,15.253,18.416,12,20.846Z"/></g>
                </svg>
                <!--p>This one!</p-->
                </div>
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