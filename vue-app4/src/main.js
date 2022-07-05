import { createApp } from 'vue';


import App from './App.vue'
import BaseCard from './components/UI/BaseCard.vue'
import BaseButton from './components/UI/BaseButton.vue'



const app =createApp(App)


//  UI 
app.component('base-card', BaseCard);
app.component('base-button', BaseButton);

// Pages (leaning-resources)
// app.component('stored-resources', StoredResources);
// app.component('add-resource', AddResource);


app.mount('#app');
