<template>
    <h1>Todo app</h1>    
    <br>
    <form @submit.prevent="addTodo()">
        <input v-model="new_name" type="text" placeholder="name" required>
        <input v-model="new_description" type="text" placeholder="description" required>
        <button type="submit">submit</button>
    </form>

    <br>
    <table>
        <thead>
            <tr>
                <td>name</td>
                <td>description</td>
            </tr>
        </thead>
        <tbody>
            <tr v-for="todo in todolist">
               <td>{{ todo.name }}</td> 
               <td>{{ todo.description }}</td> 
            </tr>
        </tbody>
    </table>

</template>


<script>
export default{
    data(){
        return{
            todolist:[],
            new_name:'',
            new_description:''
        }
    },
    methods:{
        addTodo(){
            this.todolist.push({name:this.new_name, description:this.new_description})
            console.log(this.todolist)

            this.new_description=""
            this.new_name=""
        }
    }
}
</script>