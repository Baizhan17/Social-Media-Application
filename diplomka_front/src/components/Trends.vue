<template>
    <div class="p-4 bg-white border border-gray-200 rounded-lg">
                        <h3 class="mb-6 text-xl">Recent trends</h3>

                        <div class="space-y-4 py-2" v-for="trend in trends" v-bind:key="trends.id">
                            <div class="flex items-center justify-between">
                                <div class="flex items-center space-x-2">
                                    <p class="text-s">
                                        <strong class="text-red-400">{{trend.hashtags}}</strong>
                                        <br>
                                        <span class="text-gray-500">{{trend.hashtags_counter}} posts</span>
                                    </p>
                                </div>

                                <!-- <RouterLink :to="{name:'trendsview',params:{id:trend.hashtags}}" class="py-2 px-3 bg-blue-600 text-white text-xs rounded-lg">Explore</RouterLink> -->
                            </div>
<!-- 
                            <div class="flex items-center justify-between">
                                <div class="flex items-center space-x-2">
                                    <p class="text-xs">
                                        <strong>#trend1</strong><br>
                                        <span class="text-gray-500">180 posts</span>
                                    </p>
                                </div>

                                <a href="#" class="py-2 px-3 bg-blue-600 text-white text-xs rounded-lg">Explore</a>
                            </div> -->

                            
                        </div>
                    </div>
</template>

<script>
import axios from 'axios'
export default {
    name:'trends',
    data(){
        return{
            trends:[]
        }
    },
    mounted(){
        this.getTrends()
    },
    methods:{
        getTrends(){
            axios
                .get(`/api/posts/trends/`)
                .then(response=>{
                    console.log('data',response.data.data)
                    this.trends=response.data
                })
                .catch(error=>{
                    console.log('error',error)
                })
        }
    }

}



</script>