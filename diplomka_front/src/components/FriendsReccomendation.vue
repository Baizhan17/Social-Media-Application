<template>
     <div class="p-4 bg-white border border-gray-200 rounded-lg">
                        <h3 class="mb-6 text-xl">People you may know</h3>

                        <div class="space-y-4">
                            <div class="flex items-center justify-between" v-for="user in users" v-bind:key="user.id">
                                <div class="flex items-center space-x-2">
                                    <img src="https://i.pravatar.cc/300?img=70" class="w-[40px] rounded-full">
                                    
                                    <p class="text-xs"><strong>{user.name}</strong></p>
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