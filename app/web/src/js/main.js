import 'bootstrap'

import { createApp } from 'vue'

import '../sass/main.scss'

console.log('Here we go');

const app = createApp({
    data() {
      return {
        email: 'Enter your email nicely'
      }
    }
  }
).mount('#signup');

