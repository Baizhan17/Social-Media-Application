<template>
    <div class="mb-6 flex items-center justify-between">
        <div class="flex items-center space-x-6">
            <img src="https://i.pravatar.cc/150?u=fake@pravatar.com" class="w-[40px] rounded-full">
            
            <p>
                <strong>
                    <RouterLink :to="{ name: 'profile', params: { id: post.created_by.id } }">{{ post.created_by.name }}</RouterLink>
                </strong>
            </p>
        </div>

        <p class="text-gray-600">{{ post.created_at_format }} ago</p>
    </div>

    <p v-html="formattedBody"></p>

    <div v-if="post.attachments && post.attachments.length > 0" class="attachments my-4">
        <img v-for="attachment in post.attachments" :key="attachment.id" :src="attachment.image" class="attachment-image">
    </div>

    <div class="my-6 flex justify-between">
        <div class="flex space-x-6">
            <div class="flex items-center space-x-2" @click="likePost(post.id)">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"></path>
                </svg>  
                
                <span class="text-gray-500 text-xs">{{ post.likes_counter }} likes</span>
            </div>
            
            <div class="flex items-center space-x-2">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z"></path>
                </svg> 

                <RouterLink :to="{ name: 'postview', params: { id: post.id } }" class="text-gray-500 text-xs">{{ post.comments_counter }} comments</RouterLink>
            </div>
        </div>
        
        <div class="relative">
            <svg @click="toggleReportBox" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 menu-b cursor-pointer">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z"></path>
            </svg> 

            <div v-if="showReportBox" class="absolute right-0 mt-2 w-32 bg-white border border-gray-300 rounded-md shadow-lg z-10">
                <RouterLink :to="{ name: 'report' }" class="p-2 text-center text-rose-600 cursor-pointer hover:bg-gray-200">Report</RouterLink>
            </div>
        </div>  
    </div>  
</template>

<script>
import axios from 'axios';
import { RouterLink } from 'vue-router';

export default {
    components: {
        RouterLink,
    },
    props: {
        post: {
            type: Object,
            required: true
        }
    },

    data() {
        return {
            showReportBox: false
        };
    },

    computed: {
        // Splits long words in the post body for better readability
        formattedBody() {
            return this.post.body.split(' ').map(word => 
                word.length > 60 ? word.match(/.{1,60}/g).join('<br>') : word
            ).join(' ');
        }
    },

    methods: {
        // Toggles the visibility of the report box
        toggleReportBox() {
            this.showReportBox = !this.showReportBox;
        },

        // Sends a request to like a post
        async likePost(id) {
            try {
                const response = await axios.post(`/api/posts/${id}/like/`);
                console.log('Response:', response.data); // Debugging
                if (response.data.message === 'The post has been liked') {
                    // Update likes_counter directly
                    this.post.likes_counter += 1;
                } else {
                    console.log('Unexpected response message:', response.data.message);
                }
            } catch (error) {
                if (error.response) {
                    // The request was made and the server responded with a status code
                    // that falls out of the range of 2xx
                    console.error('Error response data:', error.response.data);
                    console.error('Error response status:', error.response.status);
                    console.error('Error response headers:', error.response.headers);
                } else if (error.request) {
                    // The request was made but no response was received
                    console.error('Error request data:', error.request);
                } else {
                    // Something happened in setting up the request that triggered an Error
                    console.error('Error message:', error.message);
                }
                console.error('Error config:', error.config);
            }
        },
    }
}
</script>

<style>
.attachment-image {
    max-width: 100%;
    margin-top: 10px;
}
</style>
