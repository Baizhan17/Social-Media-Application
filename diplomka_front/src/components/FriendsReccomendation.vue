<template>
     <div class="p-4 bg-white border border-gray-200 rounded-lg">
                        <h3 class="mb-6 text-xl">Reccomended users</h3>

                        <div class="space-y-4">
                            <div class="flex items-center justify-between conversation-item" v-for="user in users" v-bind:key="user.id">
                                <div class="flex items-center space-x-2">
                                    <img src="https://placebeard.it/250/250" class="w-[40px] rounded-full">
                                    
                                    <p class="text-xs hover:scale-125 transition-transform duration-500 ease-in-out"><strong>{{ user.name }}</strong></p>

                                </div>

                                <RouterLink :to="{name: 'profile',params:{id:user.id}}" class="py-2 px-3 bg-blue-600 text-white text-xs rounded-lg">Show</RouterLink>
                            </div>

                           
                        </div>
                    </div>
</template>

<script>
import axios from 'axios'
export default {
    data(){
       return {
            users: []
        }
    },
    mounted(){
        this.GetFriendReccomendations()
    },
    methods:{
        GetFriendReccomendations(){
            axios
                .get(`/api/friends/reccomended/`)
                .then(response=>{
                    console.log('response', response.data)
                    this.users = response.data
                    if (!response.name){
                        console.log('No user found')
                    }
                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    }
}

</script>
