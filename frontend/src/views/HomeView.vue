<template>
  <h1>{{ add}}</h1>
  <router-link to="/about">go to about page</router-link>
  <br>
  <p>{{ name }}</p>
  <button class="btn btn-primary" v-on:click="add_nums()">click me</button>
  <button class="btn btn-secondary" @click="alert_me()">click me</button>


  <div v-if="num === 0">
    A
  </div>
  <div v-else-if="num === 1">
    B
  </div>
  <div v-else-if="num === 2">
    C
  </div>
  <div v-else>
    Not A/B/C
  </div>

  <div v-show="num === 0">
    given number is 0
  </div>

  <br>

  <div class="card" v-for="student in data">
    <div class="card-body">
      <p>name: {{ student.id }}</p>
      <p>age: {{ student.username }}</p>
      <p>age: {{ student.email }}</p>
    </div>
  </div>

  <form action="">
    <label for="name">name</label>
    <input v-model="name" id="name" type="text" placeholder="Enter name">
    <label for="age">age</label>
    <input v-model="age" id="age" type="text" placeholder="Enter age">
    <button type="submit">submit</button>
  </form>


</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: "shivam",
      age: "21",
      num: 5,
      data: []
    }
  },
  methods: {

  async fetch_users(){
    const response = await axios.get('http://127.0.0.1:5000/user')
    console.log(response)
    this.data = response.data.msg
  },
    add_nums() {
      const a = "app dev "
      const b = "project"
      this.name = a + b
      alert(this.name)
    },
    alert_me() {
      alert(this.name)
      alert(this.age)
    }
  },
  computed: {
    add() {
      return 'shivam'
    }
  },

  created() {
    alert(this.add_nums())
    // alert(this.age)
  },
  mounted() {
    // this.add_nums()
    this.fetch_users()
  }
}

</script>
