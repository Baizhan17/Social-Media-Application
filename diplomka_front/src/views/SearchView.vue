<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-3 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg">
                <form v-on:submit.prevent="submitForm" class="p-4 flex flex-col space-y-2">  
                    <div class="flex space-x-4">
                        <input v-model="query" type="search" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What are you looking for?" >
                        
                        <button class="inline-block py-4 px-6 bg-blue-600 text-white rounded-lg">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6" required>
                                <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"></path>
                            </svg>
                        </button>
                    </div>
                    <p v-if="error" class="text-red-600">{{ error }}</p>
                </form>
            </div>

            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-4 gap-4"
                v-if="users.length"
            >
                <div 
                    class="p-4 text-center bg-gray-100 rounded-lg conversation-item"
                    v-for="user in users"
                    v-bind:key="user.id"
                >
                    <img src="http://www.placecage.com/250/250">
                    <p>
                        <strong>
                            <RouterLink :to="{name: 'profile', params:{'id': user.id}}">{{ user.name }}</RouterLink>
                        </strong>
                    </p>

                    <div class="mt-6 flex space-x-8 justify-around">
                        <p class="text-xs text-gray-500">{{ user.friends_number }} friends</p>
                        <p class="text-xs text-gray-500">{{user.posts_number}} posts</p>
                    </div>
                </div>
            </div>

            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="post in posts"
                v-bind:key="post.id"
            >
                <FeedItem v-bind:post="post" />
            </div>
        </div>

        <div class="main-right col-span-1 space-y-4">
            <FriendsReccomendation />

            <Trends />
        </div>
    </div>
</template>


<script>
import axios from 'axios'
import FriendsReccomendation from '../components/FriendsReccomendation.vue'
import Trends from '../components/Trends.vue'
import FeedItem from '../components/FeedItem.vue'

export default {
    name: 'SearchView',

    components: {
        FriendsReccomendation,
        Trends,
        FeedItem,
    },

    data() {
        return {
            query: '',
            users: [],
            posts: [],
            error: ''  // Add an error state
        }
    },

    methods: {
        submitForm() {
            if (!this.query.trim()) {
                this.error = 'Please enter users name.'
                return
            }

            this.error = '' // Clear error if there is input

            console.log('submitForm', this.query)

            axios
                .post('/api/search/', {
                    query: this.query
                })
                .then(response => {
                    console.log('response:', response.data)

                    this.users = response.data.users
                    this.posts = response.data.posts
                    if(this.users.length ==0&&this.posts.length ==0) {
                        console.log('Nothing found here')
                    }
                })
                .catch(error => {
                    console.log('error:', error)
                })
        }
    }
}
</script>
<style scoped>
.conversation-item {
    transition: filter 0.3s ease-in-out;
  }
  
  .conversation-item:hover {
    filter: blur(2px);
  }
</style>