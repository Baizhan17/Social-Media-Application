<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        
        
        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div>
                        <label>Old password</label><br>
                        <input type="password" v-model="form.old_password" placeholder="Your old password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                     <div>
                        <label>New password</label><br>
                        <input type="password" v-model="form.new_password1" placeholder="Your new password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>
                     <div>
                        <label>Repeat password</label><br>
                        <input type="password" v-model="form.new_password2" placeholder="Please repeat your new password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <!-- <div>
                        <label>Password</label><br>
                        <input type="password" v-model="form.password1" placeholder="Your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Repeat password</label><br>
                        <input type="password" v-model="form.password2" placeholder="Repeat your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div> -->

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-blue-600 text-white rounded-lg">Save</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
    
</template>
<script>
import axios from 'axios'

import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
     name: 'EditProfileView',

    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore
        }
    },

//     components: {
//         FeedItem
//     },

        data() {
                return {
                    form: {
                        old_password: '',
                        new_password1: '',
                        new_password2: '',
                    },
                    errors: [],
                }
            },

//     mounted() {
//         this.getFeed()
//     },

//     watch: { 
//         '$route.params.id': {
//             handler: function() {
//                 this.getFeed()
//             },
//             deep: true,
//             immediate: true
//         }
//     },

        methods: {
                 submitForm() {
            this.errors = []

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('The password does not match')
            }

            if (this.errors.length === 0) {
                let formData = new FormData()
                formData.append('old_password', this.form.old_password)
                formData.append('new_password1', this.form.new_password1)
                formData.append('new_password2', this.form.new_password2)

                axios
                    .post('/api/editpassword/', formData, {
                        headers: {
                            "Content-Type": "multipart/form-data",
                        }
                    })
                    .then(response => {
                        if (response.data.message === 'new password is setted up') {
                            this.toastStore.showToast(5000, 'The information was saved', 'bg-emerald-500')

                            this.$router.push(`/profile/${this.userStore.user.id}`)
                        } else {
                            const data = JSON.parse(response.data.message)

                            for (const key in data){
                                this.errors.push(data[key][0].message)
                            }
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
            }
}
</script>

