<template>
    <ul>
        <transition-group tag="ul" name="user-list">
            <li v-for="user in users" :key="user" @click="removeUser(user)">
                {{ user }}
            </li>
        </transition-group>
    </ul>

    <div>
        <input type="text" ref="userNameInput" />
        <button @click="addUser">Add user</button>
    </div>
</template>


<script>
export default {
    data() {
        return {
            users: ["Ram", "Sita", "Laxman", "Hanuman", "Janki", "Bharat"],

        }
    },

    methods: {
        removeUser(user) {
            this.users = this.users.filter(usr => usr !== user);
        },
        addUser() {
            const enteredUserName = this.$refs.userNameInput.value;
            this.users.push(enteredUserName)
        },
    },
}
</script>


<style>
ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

li {
    border: 1px solid #ccc;
    padding: 1rem;
    text-align: center;
}

.user-list-enter-from{
    opacity: 0;
    transform: translateX(-30px);
}

.user-list-enter-active {
    transition: all 2s ease-out;
}

.user-list-enter-to {
    opacity: 1;
    transform: translateX(0px);
}




.user-list-leave-active {
    transition: all 2s ease-in;
}

.user-list-leave-to{
    opacity: 0;
    transform: translateX(30px);
}



</style>