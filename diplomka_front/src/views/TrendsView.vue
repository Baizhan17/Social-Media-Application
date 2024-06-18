<template>
    <div class="flex justify-center bg-gray-100 py-6">
        <div class="max-w-7xl grid grid-cols-4 gap-4">
            <div class="main-center col-span-3 space-y-4">
             
                <div class="p-4 bg-white border border-gray-200 rounded-lg" v-for="post in posts" v-bind:key="post.id">
                    <div class="mb-6 flex items-center justify-between">
                        <div class="flex items-center space-x-6">
                            <img src="http://www.placecage.com/250/250">
                            <p><strong>{{ post.created_by.name }}</strong></p>
                        </div>
                        <p class="text-gray-600">{{ post.created_at_format }}</p>
                    </div>

                    <p>{{ post.body }}</p>

                    
                </div>
                 <div class="main-right col-span-1 space-y-4 ml-4">
                    <Trends />
                </div>

            </div>
        </div>
    </div>
</template>


<script>
import axios from "axios"
//import PeopleYouMayKnow from '@/components/PeopleYouMayKnow.vue';
import Trends from '@/components/Trends.vue';
export  default {
    name: "FeedView",
    components:{
  Trends,
    },
    data(){
        return{
            posts:[],
           
        }
    },
    mounted(){
        this.getFeed()
    },
    methods:{
        loadNext(){
            this.currentPage += 1;
            this.getPosts()
        },
        loadPrevious(){
            this.currentPage -= 1;
            this.getPosts()
        },
        
        
    }
}
</script>