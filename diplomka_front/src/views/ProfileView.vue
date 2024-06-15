<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <img src="https://i.pravatar.cc/300?u=fake@pravatar.com" class="mb-6 rounded-full">
                
                <p><strong>{{ user.name }}</strong></p>

                <div class="mt-6 flex space-x-8 justify-around" v-if="user.id">
                    <RouterLink :to="{name: 'friends', params: {id: user.id}}" class="text-xs text-gray-500">{{ user.friends_number }} friends</RouterLink>
                    <p class="text-xs text-gray-500">{{user.posts_number}} posts</p>
                </div>

                <div class="mt-6 flex flex-col">
                    <button 
                        class="inline-block py-4 px-3 bg-blue-600 text-xs text-white rounded-lg" 
                        @click="sendFriendshipRequest"
                        v-if="userStore.user.id !== user.id"
                    >
                        Send friendship request
                    </button>
                    <button 
                        class="inline-block py-4 px-3 bg-blue-600 text-xs text-white rounded-lg mt-4" 
                        @click="sendMessage"
                        v-if="userStore.user.id !== user.id"
                    >
                        Send Message
                    </button>
                    <button 
                        class="inline-block py-4 px-3 bg-red-600 text-xs text-white rounded-lg pb-4 mb-4" 
                        @click="logout"
                        v-if="userStore.user.id === user.id"
                    >
                        Log out
                    </button>
                    <RouterLink :to="{ name: 'editprofile' }"
                        class="inline-block py-4 px-3 bg-emerald-600 text-xs text-white rounded-lg" 
                        v-if="userStore.user.id === user.id"
                    >
                        Edit profile
                    </RouterLink>
                </div>
            </div>
        </div>

        <div class="main-center col-span-2 space-y-4">
            <div 
                class="bg-white border border-gray-200 rounded-lg"
                v-if="userStore.user.id === user.id"
            >
                <form v-on:submit.prevent="submitForm" method="post">
                    <div class="p-4">  
                        <textarea v-model="body" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What are you thinking about?"></textarea>
                    </div>

                    <div class="p-4 border-t border-gray-100 flex justify-between">
                        <a href="#" class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">Add image</a>
                        <input type="file" ref="file" class=""/>
                        <button class="inline-block py-4 px-6 bg-blue-600 text-white rounded-lg">Post</button>
                    </div>
                </form>
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
            <!-- <PeopleYouMayKnow /> -->

            <!-- <Trends /> -->
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'
import FeedItem from '../components/FeedItem.vue'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
    name: 'FeedView',

    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore
        }
    },

    components: {
        PeopleYouMayKnow,
        Trends,
        FeedItem
    },

    data() {
        return {
            posts: [],
            user: {
                id: null
            },
            body: '',
            url:null
        }
    },

    mounted() {
        this.getFeed()
    },

    watch: { 
        '$route.params.id': {
            handler: function() {
                this.getFeed()
            },
            deep: true,
            immediate: true
        }
    },

    methods: {
        sendMessage(){
            console.log(`the message:  is sent to `)
            axios
                .get(`/api/user_chat/${this.$route.params.id}/get-create/`)
                .then(response => {
                    console.log(response.data)
                    this.$router.push('/user_chat')
                })
                .catch(error => {
                    console.log('error while sending the message', error)
                })

        },
        sendFriendshipRequest() {
            axios
                .post(`/api/friends/${this.$route.params.id}/request/`)
                .then(response => {
                    console.log('data', response.data)

                    if (response.data.message == 'request already sent') {
                        this.toastStore.showToast(5000, 'The request has already been sent!', 'bg-red-300')
                    } else {
                        this.toastStore.showToast(5000, 'The request was sent!', 'bg-emerald-300')
                    }
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        getFeed() {
            axios
                .get(`/api/posts/profile/${this.$route.params.id}/`)
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data.posts
                    this.user = response.data.user
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        submitForm() {
            console.log('submitForm', this.body)
            // let formData =new FormData()
            // formData.append('body', this.body)
            // formData.append('image', this.$refs.file.feiles[0])
            axios
                .post('/api/posts/create/',formData)
                .then(response => {
                    console.log('data', response.data)

                    this.posts.unshift(response.data)
                    this.body = ''
                    this.user.posts_number+=1
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        logout() {
            console.log('Log out')

            this.userStore.removeToken()

            this.$router.push('/')
        }
    }
}
</script>