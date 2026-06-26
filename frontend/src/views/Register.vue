<template>

    <h1>register page</h1>

    <form @submit.prevent="register">
        <div class="mb-3">
            <label for="InputEmail" class="form-label">Email address</label>
            <input v-model="formdata.email" type="email" class="form-control" id="InputEmail" aria-describedby="emailHelp">
            <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
        </div>
        <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label">Password</label>
            <input v-model="formdata.password" type="password" class="form-control" id="exampleInputPassword1">
        </div>
        <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input v-model="formdata.username" type="text" class="form-control" id="username">
        </div>

        <select v-model="formdata.role" class="form-select" aria-label="Default select example">
            <option selected value="employee">employee</option>
            <option value="manager">manager</option>
        </select>

        <br>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>

</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            formdata: {
                username: '',
                email: '',
                role: 'employee',
                password: ''
            }
        }
    },
    methods: {
        async register() {
            const response = await axios.post('http://127.0.0.1:5000/signup', this.formdata)
            alert(response.data.msg)
        }
    }
}

</script>
