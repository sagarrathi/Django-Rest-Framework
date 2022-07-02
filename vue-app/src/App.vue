<template>
  <header><h1>My friends</h1></header>
  <new-friend @add-contact="add_contact"></new-friend>

  <ul v-for="friend in friends" :key="friend.key">
    <friend-contact
      :id="friend.id"
      :name="friend.name"
      :phone="friend.phone"
      :email="friend.email"
      :is_missing="friend.is_missing"
      @toggle-missing-event="toggle_missing_main_app"
      @delete-contact="delete_contact"
    ></friend-contact>
  </ul>
  <div id="app"></div>
</template>

<script>
export default {
  data() {
    return {
      friends: [
        {
          id: "ram",
          name: "ram raghuvanshi",
          phone: "0214",
          email: "ram@bharat.in",
          is_missing: true,
        },
        {
          id: "sita",
          name: "sita raghuvanshi",
          phone: "0214",
          email: "sita@janki.in",
          is_missing: true,
        },
      ],
    };
  },

  methods: {
    toggle_missing_main_app(id) {
      // alert("running from app")
      const identified_friend = this.friends.find((friend) => friend.id === id);
      identified_friend.is_missing = !identified_friend.is_missing;
    },

    add_contact(name, phone, email) {
      const new_friend = {
        id: name,
        name: name,
        phone: phone,
        email: email,
        is_missing: true,
      };
      alert(name);
      this.friends.push(new_friend);
    },

    delete_contact(id){
      this.friends=this.friends.filter((friend) => friend.id!== id);
    },


  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Jost&display=swap");
* {
  box-sizing: border-box;
}

html {
  font-family: "Jost", sans-serif;
}

body {
  margin: 0;
}

header {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  margin: 3rem auto;
  border-radius: 10px;
  padding: 1rem;
  background-color: #58004d;
  color: white;
  text-align: center;
  width: 90%;
  max-width: 40rem;
}

#app ul {
  margin: 0;
  padding: 0;
  list-style: none;
}

#app li,
#app form {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  margin: 1rem auto;
  border-radius: 10px;
  padding: 1rem;
  text-align: center;
  width: 90%;
  max-width: 40rem;
}

#app h2 {
  font-size: 2rem;
  border-bottom: 4px solid #ccc;
  color: #58004d;
  margin: 0 0 1rem 0;
}

#app button {
  font: inherit;
  cursor: pointer;
  border: 1px solid #ff0077;
  background-color: #ff0077;
  color: white;
  padding: 0.05rem 1rem;
  box-shadow: 1px 1px 2px rgba(0, 0, 0, 0.26);
}

#app button:hover,
#app button:active {
  background-color: #ec3169;
  border-color: #ec3169;
  box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.26);
}

#app input {
  font: inherit;
  padding: 0.15rem;
}
#app label {
  font-weight: bold;
  margin-right: 1rem;
  width: 7rem;
  display: inline-block;
}
#app form div {
  margin: 1rem 0;
}
</style>
