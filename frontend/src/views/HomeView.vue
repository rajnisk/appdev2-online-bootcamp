<template>
  <h1>home page</h1>
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
      <p>name: {{ student.name }}</p>
      <p>age: {{ student.age }}</p>
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
export default {
  data() {
    return {
      name: "shivam",
      age: "21",
      num: 5,
      data: [
        { name: "shivam", age: 20 },
        { name: "sachin", age: 21 },
        { name: "saurabh", age: 22 },
        { name: "satyam", age: 23 },
      ]
    }
  },
  methods: {
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

  },
  created() {
    alert(this.age)
  },
  mounted() {
    this.add_nums()
  }
}

</script>
