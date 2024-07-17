<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4 md:grid-cols-4">
        <div class="main-left col-span-1 md:col-span-1">
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <p class="text-xl pb-2  md:text-xs">Conversations:</p>
                <div class="space-y-4">
                    <div 
                        class="flex items-center justify-between conversation-item"
                        v-for="conversation in conversations"
                        v-bind:key="conversation.id"
                        v-on:click="setActiveConversation(conversation.id)"
                    >
                        <div class="flex items-center space-x-2">
                            <img src="https://avatar.iran.liara.run/public/boy?username=Ash" class="w-[40px] rounded-full">
                            <template
                                v-for="user in conversation.users"
                                v-bind:key="user.id"
                            >
                                <p 
                                    class="text-xs font-bold"
                                    v-if="user.id !== userStore.user.id"
                                >{{ user.name }}</p>
                            </template>
                        </div>
                        <span class="text-xs text-gray-500">{{ conversation.modified_at_format }} ago</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="main-center col-span-3  rounded-xl h-screen flex flex-col">

            <div class="bg-yellow-200 border border-gray-200 rounded-lg flex-grow overflow-y-auto">
                <div class="w-full h-10 bg-blue-500 flex items-center space-x-2 p-2 rounded-xl border ">
                    <img src="https://avatar.iran.liara.run/public/boy?username=Ash" class="w-[40px] rounded-full p-1">
                    <p class="users-chatting">Naruto1</p>
                </div>
                <div class="flex flex-col flex-grow p-4">
                    <template
                        v-for="message in activeConversation.messages"
                        v-bind:key="message.id"
                     class="">
                        <div 
                            class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end"
                            v-if="message.created_by.id === userStore.user.id"
                        >
                            <div>
                                <div class="bg-blue-600 text-white p-3 rounded-l-lg rounded-br-lg">
                                    <p class="text-sm">{{ message.text }}</p>
                                </div>
                                <span class="text-xs text-gray-500 leading-none">{{ message.created_at_format }} ago</span>
                            </div>
                            <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                                <img src="https://placebear.com/250/250" class="w-[40px] rounded-full">
                            </div>
                        </div>

                        <div 
                            class="flex w-full mt-2 space-x-3 max-w-md"
                            v-else
                        >
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

            <div class="message-send bg-white border border-gray-200 rounded-lg position: sticky col-span-3">
                <form v-on:submit.prevent="submitForm">
                    <div class="p-4 relative">
                        <textarea ref="textarea" v-model="text" @input="autoResize" class="p-4 w-full bg-gray-100 rounded-lg pl-12" placeholder="What do you want to say?"></textarea>
                        <button type="button" @click="toggleEmojiPicker" class="absolute top-4 left-4">
                            <div class="p-4">😊</div>
                        </button>
                        <div v-if="showEmojiPicker" class="absolute top-12 left-4 z-10">d
                            <EmojiPicker @emoji-click="addEmoji" />
                        </div>
                    </div>

                    <div class="p-4 border-t border-gray-100 flex justify-between">
                        <button class="inline-block py-4 px-6 bg-blue-600 text-white rounded-lg hover:bg-sky-700">Send</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>



<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import EmojiPicker from 'vue3-emoji-picker'
import 'vue3-emoji-picker/css'
import { MdEmojiemotionsOutlined } from "oh-vue-icons/icons";
export default {
    name: 'userchat',
    components: {
        EmojiPicker
    },
    setup() {
        const userStore = useUserStore()
        return {
            userStore
        }
    },
    data() {
        return {
            conversations: [],
            activeConversation: {},
            text: '',
            showEmojiPicker: false
        }
    },
    mounted() {
        this.getConversations()
    },
    methods: {
        setActiveConversation(id) {
            console.log('setActiveConversation', id)
            this.activeConversation = id
            this.getMessages()
        },
        getConversations() {
            console.log('getConversations')
            axios
                .get('/api/userchat/')
                .then(response => {
                    console.log(response.data)
                    this.conversations = response.data
                    if (this.conversations.length) {
                        this.activeConversation = this.conversations[0].id
                        this.getMessages()
                    } else {
                        console.log('No active conversations available.')
                    }
                })
                .catch(error => {
                    console.log(error)
                })
        },
        getMessages() {
            console.log('getMessages')
            axios
                .get(`/api/userchat/${this.activeConversation}/`)
                .then(response => {
                    console.log(response.data)
                    this.activeConversation = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
        autoResize(event) {
            const textarea = event.target
            textarea.style.height = 'auto'
            textarea.style.height = textarea.scrollHeight + 'px'
        },
        toggleEmojiPicker() {
            this.showEmojiPicker = !this.showEmojiPicker
        },
        addEmoji(emoji) {
            const textarea = this.$refs.textarea
            const start = textarea.selectionStart
            const end = textarea.selectionEnd
            const text = this.text.slice(0, start) + emoji.i + this.text.slice(end)
            this.text = text
            textarea.focus()
            textarea.setSelectionRange(start + emoji.i.length, start + emoji.i.length)
        },
        submitForm() {
            console.log('submitForm', this.text)
            axios
                .post(`/api/userchat/${this.activeConversation.id}/send/`, {
                    text: this.text
                })
                .then(response => {
                    console.log(response.data)
                    this.activeConversation.messages.push(response.data)
                    this.text = '' // Clear the text area after sending the message
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>


<style scoped>
/* Custom scrollbar for the main-center container */
.main-center {
    overflow-y: auto;
    overflow-x: hidden;
}

.custom-scrollbar::-webkit-scrollbar {
    width: 8px;
}

.custom-scrollbar::-webkit-scrollbar-track {
    background: #f0f0f0;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
    background-color: #888;
    border-radius: 4px;
}

/* Hide scrollbar in Firefox */
.custom-scrollbar {
    scrollbar-width: thin;
    scrollbar-color: #888 #f0f0f0;
}
.conversation-item {
    transition: filter 0.3s ease-in-out;
  }
  
  .conversation-item:hover {
    filter: blur(2px);
  }
/* Additional styles for the overall chat layout */
textarea {
    resize: none; /* Disable manual resizing */
}
</style>
