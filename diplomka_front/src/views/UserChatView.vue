<template>
    <main class="px-8 py-6 bg-gray-100">
        <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
            <div class="main-left col-span-1">
                <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                    <div class="space-y-4">
                        <div class="flex items-center justify-between" v-for="conversation in conversations" :key="conversation.id" @click="setActiveConversation(conversation.id)">
                            <div class="flex items-center space-x-2">
                                <img src="https://i.pravatar.cc/150?u=fake@pravatar.com" class="w-[40px] rounded-full">
                                <template v-for="user in conversation.users" :key="user.id">
                                    <p class="text-xs" v-if="user.id !== userStore.user.id"><strong>{{ user.name }}</strong></p>
                                </template>
                            </div>
                            <span class="text-xs text-gray-500">online {{ conversation.modified_at_format }} ago</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="main-center col-span-3 space-y-4">
                <div class="bg-white border border-gray-200 rounded-lg">
                    <div class="flex flex-col flex-grow p-4">
                        <template v-for="message in activeConversation.messages" :key="message.id">
                            <div class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end" v-if="message.created_by.id == userStore.user.id">
                                <div>
                                    <div class="bg-blue-600 text-white p-3 rounded-l-lg rounded-br-lg">
                                        <p class="text-sm">{{ message.text }}</p>
                                    </div>
                                    <span class="text-xs text-gray-500 leading-none">{{ message.created_at_format }} ago</span>
                                </div>
                                <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                                    <img src="https://i.pravatar.cc/300?img=70" class="w-[40px] rounded-full">
                                </div>
                            </div>

                            <div class="flex w-full mt-2 space-x-3 max-w-md" v-else>
                                <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                                    <img src="https://i.pravatar.cc/300?img=70" class="w-[40px] rounded-full">
                                </div>
                                <div>
                                    <div class="bg-gray-300 p-3 rounded-r-lg rounded-bl-lg">
                                        <p class="text-sm">{{ message.text }}</p>
                                    </div>
                                    <span class="text-xs text-gray-500 leading-none">{{ message.created_at_format }} ago</span>
                                </div>
                            </div>
                        </template>
                    </div>
                </div>

                <div class="bg-white border border-gray-200 rounded-lg">
                    <form @submit.prevent="submitForm">
                        <div class="p-4">
                            <textarea v-model="text" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What do you want to say?"></textarea>
                        </div>
                        <div class="p-4 border-t border-gray-100 flex justify-between">
                            <button class="inline-block py-4 px-6 bg-blue-600 text-white rounded-lg">Send</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import axios from "axios"
import { useUserStore } from '@/stores/user'

export default {
    name: 'userchat',
    setup() {
        const userStore = useUserStore()
        return {
            userStore
        }
    },

    data() {
        return {
            conversations: [],
            activeConversation: { messages: [] },
            text: ''
        }
    },
    mounted() {
        this.getConversations()
    },
    methods: {
        getConversations() {
            axios
                .get('/api/user_chat/')
                .then(response => {
                    this.conversations = response.data
                    if (this.conversations.length) {
                        this.setActiveConversation(this.conversations[0].id)
                    }
                })
                .catch(error => {
                    console.error('Error getting conversations:', error)
                })
        },
        getMessages(conversationId) {
            axios
                .get(`/api/user_chat/${conversationId}/`)
                .then(response => {
                    this.activeConversation = response.data
                    console.log('Active conversation set:', this.activeConversation)
                })
                .catch(error => {
                    console.error('Error getting messages:', error)
                })
        },
        setActiveConversation(conversationId) {
            console.log('Setting active conversation ID:', conversationId)
            this.getMessages(conversationId)
        },
        submitForm() {
            if (!this.activeConversation || !this.activeConversation.id) {
                console.error('Active conversation ID is not defined.');
                return;
            }

            console.log('Submitting message to conversation ID:', this.activeConversation.id)
            axios
                .post(`/api/user_chat/${this.activeConversation.id}/send/`, {
                    text: this.text
                })
                .then(response => {
                    this.activeConversation.messages.push(response.data);
                    this.text = ''; // Clear the text input after sending the message
                })
                .catch(error => {
                    console.error('Error sending message:', error);
                });
        }
    }
}
</script>
